# """SoftliQ Sensor Platform."""
# import logging
# import voluptuous as vol

# from homeassistant.components.sensor import (
#     PLATFORM_SCHEMA,
#     SensorDeviceClass, 
#     SensorEntity, 
#     SensorStateClass
# )
# from homeassistant.cure import HomeAssistant
# from homeassistant.helpers.entity_platform import AddEntitiesCallback
# from homeassistant.helpers.typing import ConfigType, DisoveryInfoType

# from homeassistant.const import (
#     CONF_NAME,
#     CONF_ADDR
# )

# DEFAULT_NAME = "SoftliQ - Watersoftener"

# PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
#     {
#         vol.Required(CONF_NAME, default=DEFAULT_NAME): cv.string,
#         vol.Required(CONF_ADDR): cv.string
#     }
# )

# _LOGGER = logging.getLogger(__name__)
# # Time between updating data from softliq
# SCAN_INTERVAL = timedelta(seconds=10)