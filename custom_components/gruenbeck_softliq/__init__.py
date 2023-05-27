
from homeassistant.components.sensor import (
    PLATFORM_SCHEMA,
    SensorDeviceClass, 
    SensorEntity, 
    SensorStateClass
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DisoveryInfoType

from homeassistant.const import (
    CONF_NAME,
    CONF_ADDR
)

DEFAULT_NAME = "SoftliQ - Watersoftener"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Required(CONF_ADDR): cv.string
    }
)

async def async_setup_platform(
                                hass: HomeAssistant,
                                config: ConfigType,
                                add_entities: AddEntitiesCallback,
                                discovery_info: DiscoveryInfoType | None = None) -> None:
    """Set up the sensor platform."""
    name = config[CONF_NAME]
    addr = config[CONF_ADDR]

    add_entities([SoftliQSensor(name, addr)], True)

class SoftliQSensor(SensorEntity):
    """Representation of a SoftliQSensor Sensor."""

    def __init__(self, name, addr) -> None:
        super().__init__()
        self._name = name
        self._addr = addr
        self._attr_name = name
        # self._attr_native_unit_of_measurement = TEMP_CELSIUS
        # self._attr_device_class = SensorDeviceClass.TEMPERATURE
        # self._attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def name(self) -> str:
        """Return the name of the switch."""
        return self._name

    @property
    def unique_id(self) -> str:
        """Return a unique, Home Assistant friendly identifier for this entity."""
        return self._mac.replace(":", "")

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._attr_native_value = 23