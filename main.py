import redis


redis_client = redis.Redis(host="localhost", port=6379, db=0)


print(redis_client.set(name="test_key", value=10))

redis_client.close()