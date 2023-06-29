from django_enhanced.settings.base import *

MIDDLEWARE.append(
    "silk.middleware.SilkyMiddleware",
)

INSTALLED_APPS.append(
    "silk",
)

ROOT_URLCONF = 'django_enhanced.urls_silk'

SILKY_PYTHON_PROFILER = True

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SILK", MIDDLEWARE)