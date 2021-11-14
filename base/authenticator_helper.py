from base.utils.settings import *

settings = Settings()

cookies = [
    {
        'name': settings.get(SettingKeys.COOKIE_TOKEN_NAME),
        'value': settings.get(SettingKeys.TOKEN),
        'domain': settings.get(SettingKeys.COOKIE_DOMAIN)
    },
    {
        'name': settings.get(SettingKeys.COOKIE_SESSION_NAME),
        'value': settings.get(SettingKeys.SESSION),
        'domain': settings.get(SettingKeys.COOKIE_DOMAIN)
    }
]

header = {
    "user-agent": settings.get(SettingKeys.USER_AGENT)
}
