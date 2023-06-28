from django.core.cache.backends.base import BaseCache
from cachetools import LRUCache

class CachetoolsCache(BaseCache):
    def __init__(self, name, params):
        super().__init__(params)
        self.cache = LRUCache(maxsize=128)

    def add(self, key, value, timeout=None, version=None):
        return self.cache.setdefault(key, value, timeout)

    def get(self, key, default=None, version=None):
        return self.cache.get(key, default)

    def set(self, key, value, timeout=None, version=None):
        self.cache[key] = value

    def delete(self, key, version=None):
        del self.cache[key]