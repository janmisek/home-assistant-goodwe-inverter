"""Constants for the Goodwe component."""
from homeassistant.const import Platform

DOMAIN = "goodwe"

PLATFORMS = [Platform.BUTTON, Platform.NUMBER, Platform.SELECT, Platform.SENSOR]

DEFAULT_NAME = "GoodWe"
DEFAULT_SCAN_INTERVAL = 5
DEFAULT_NETWORK_RETRIES = 10
DEFAULT_NETWORK_TIMEOUT = 1

CONF_MODEL_FAMILY = "model_family"
CONF_NETWORK_RETRIES = "network_retries"
CONF_NETWORK_TIMEOUT = "network_timeout"

KEY_INVERTER = "inverter"
KEY_COORDINATOR = "coordinator"
KEY_DEVICE_INFO = "device_info"