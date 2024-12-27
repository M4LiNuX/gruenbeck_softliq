import logging
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import DOMAIN, PARAMS
import aiohttp

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=5)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up Gruenbeck sensors."""
    _LOGGER.debug("Setting up Gruenbeck sensors")
    data = hass.data[DOMAIN]
    host = data["host"]
    password = data["password"]

    _LOGGER.debug("Host: %s, Password: %s", host, password)

    coordinator = GruenbeckDataUpdateCoordinator(hass, host, password)
    await coordinator._async_update_data()  # Initiales Update

    sensors = [
        GruenbeckSensor(coordinator, sensor_id, sensor_config)
        for sensor_id, sensor_config in PARAMS.items()
    ]
    async_add_entities(sensors)


class GruenbeckDataUpdateCoordinator(DataUpdateCoordinator):
    """Handle fetching data from Gruenbeck water softener."""

    def __init__(self, hass, host, password):
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=SCAN_INTERVAL,
        )
        self.host = host
        self.password = password
        self.data = {}

    async def _async_update_data(self):
        """Fetch data from the Gruenbeck API."""
        _LOGGER.debug("Fetching data from Gruenbeck API")
        payload = f"id=673&show={'|'.join(PARAMS.keys())}&code={self.password:03d}~"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(self.host, data=payload) as response:
                    if response.status != 200:
                        raise UpdateFailed(f"HTTP error {response.status}")
                    result = await response.text()
                    self.data = self._parse_response(result)
                    _LOGGER.debug("Fetched data: %s", self.data)
            except aiohttp.ClientError as err:
                raise UpdateFailed(f"Error communicating with API: {err}")

    def _parse_response(self, response):
        """Parse API response."""
        from xml.etree import ElementTree as ET
        parsed_data = {}
        try:
            root = ET.fromstring(response)
            for child in root:
                value = child.text
                # Konvertiere numerische Werte
                try:
                    value = float(value) if "." in value else int(value)
                except ValueError:
                    pass  # Belasse Strings als solche
                parsed_data[child.tag] = value
        except ET.ParseError as e:
            _LOGGER.error("Failed to parse API response: %s", e)
        return parsed_data


class GruenbeckSensor(SensorEntity):
    """Representation of a Gruenbeck sensor."""

    def __init__(self, coordinator, sensor_id, sensor_config):
        """Initialize the sensor."""
        self.coordinator = coordinator
        self.sensor_id = sensor_id
        self._attr_name = f"gruenbeck_{sensor_config['name']}"  # Name mit Präfix
        self._attr_unique_id = f"{DOMAIN}_{sensor_id}"  # Eindeutige ID mit Präfix
        self._attr_device_class = sensor_config.get("device_class", None)  # Gerätetyp
        self._attr_unit_of_measurement = sensor_config.get("unit_of_measurement", None)  # Einheit
        self._attr_native_unit_of_measurement = sensor_config.get("unit_of_measurement", None)  # Einheit für native Werte
        self._attr_state_class = sensor_config.get("state_class", None)  # Statusklasse
        self._attr_suggested_display_precision = sensor_config.get("suggested_display_precision", None)  # Vorschlag für Präzision
        self._attr_suggested_unit_of_measurement = sensor_config.get("suggested_unit_of_measurement", None)  # Vorschlag für Einheit
        self._options = sensor_config.get("options", None)  # Diskrete Optionen als Liste von Strings

    async def async_update(self):
        """Force an update of the sensor."""
        _LOGGER.debug("Manually triggering update for sensor: %s", self._attr_name)
        await self.coordinator._async_update_data()

    @property
    def state(self):
        """Return the state of the sensor."""
        value = self.coordinator.data.get(self.sensor_id)
        if isinstance(value, (int, float)):
            return value
        return None  # Rückgabe von None, wenn der Wert kein numerischer ist

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        return self.state  # In diesem Fall ist der native Wert identisch zum State

    @property
    def last_reset(self):
        """Return the time when the sensor was last reset, if applicable."""
        return None  # Kann angepasst werden, falls der Wert zurückgesetzt wird

    @property
    def available(self):
        """Return True if sensor data is available."""
        return self.sensor_id in self.coordinator.data

    @property
    def options(self):
        """Return a list of available options for the sensor, if applicable."""
        return self._options
