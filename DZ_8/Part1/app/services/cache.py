import redis
import json

class RedisCache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis = redis.Redis(host=host, port=port, db=db)

    def set(self, key, value, expiration=3600):
        self.redis.set(key, json.dumps(value), ex=expiration)

    def get(self, key):
        result = self.redis.get(key)
        return json.loads(result) if result else None

    def delete(self, key):
        self.redis.delete(key)
