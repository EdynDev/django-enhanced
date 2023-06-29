import redis
from decouple import config

HOST = config('REDIS_HOST', default='localhost')
PORT = config('REDIS_PORT', default=6379, cast=int)

print("HOST", HOST)

r = redis.Redis(
    host=HOST,
    port=PORT,
    charset="utf-8",
    decode_responses=True
)

connection = r.ping()

print(connection)

# https://medium.com/@bhupender.rawat4/python-redis-using-docker-45643af090db