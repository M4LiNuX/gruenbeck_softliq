import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PASSWORD
from .const import DOMAIN, DEFAULT_URL, DEFAULT_CODE

class GruenbeckConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Gruenbeck Water Softener."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            try:
                await self._test_connection(user_input[CONF_HOST], user_input[CONF_PASSWORD])
                return self.async_create_entry(title="Gruenbeck Water Softener", data=user_input)
            except ConnectionError:
                errors["base"] = "cannot_connect"
            except Exception:
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_HOST, default=DEFAULT_URL): str,
                    vol.Required(CONF_PASSWORD, default=DEFAULT_CODE): int,
                }
            ),
            errors=errors,
        )

    async def _test_connection(self, host, password):
        """Test the connection to the Gruenbeck device."""
        from aiohttp import ClientSession

        payload = f"id=673&show=D_A_1_1&code={password:03d}~"
        async with ClientSession() as session:
            async with session.post(host, data=payload) as response:
                if response.status != 200:
                    raise ConnectionError("Cannot connect to Gruenbeck device.")
                result = await response.text()
                if "<code>wrong</code>" in result:
                    raise ConnectionError("Invalid code.")
