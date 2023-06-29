from django_enhanced.settings.base import *

MIDDLEWARE.append(
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)

INSTALLED_APPS.append(
    "debug_toolbar",
)

INTERNAL_IPS = [
    '127.0.0.1',
]

# STATIC_URL = "static/"

ROOT_URLCONF = 'django_enhanced.urls_toolbar'

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TOOLBAR", MIDDLEWARE)