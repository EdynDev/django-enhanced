from django_enhanced.settings.silk import *

CACHES = { 
     "default": {
         "BACKEND": "django_redis.cache.RedisCache",
         "LOCATION": "redis://edyndev-cache:6379/0",
         "OPTIONS": { 
             "CLIENT_CLASS": "django_redis.client.DefaultClient"
         },
         "KEY_PREFIX": "testApp"
     }
}


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> REDIS", MIDDLEWARE)