import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.discovery import async_load_platform
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up Gruenbeck from configuration.yaml."""
    conf = config.get(DOMAIN)
    if conf is None:
        _LOGGER.error("Gruenbeck configuration not found in configuration.yaml")
        return False

    # Host und Passwort prüfen
    host = conf.get("host")
    password = conf.get("password")

    if not host or not password:
        _LOGGER.error("Gruenbeck configuration missing host or password")
        return False

    # Daten im Home Assistant speichern
    hass.data[DOMAIN] = {
        "host": host,
        "password": password,
    }
    _LOGGER.info("Gruenbeck integration successfully loaded with host %s", host)

    # Sensor-Plattform laden
    await async_load_platform(hass, "sensor", DOMAIN, {}, config)

    return True
