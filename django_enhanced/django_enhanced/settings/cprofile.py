from django_enhanced.settings.base import *

MIDDLEWARE.append(
    "django_cprofile_middleware.middleware.ProfilerMiddleware",
)

DEBUG = True

DJANGO_CPROFILE_MIDDLEWARE_REQUIRE_STAFF = False


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CPROFILE", MIDDLEWARE)