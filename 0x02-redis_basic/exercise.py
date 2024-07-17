#!/usr/bin/env python3
"""writing str to redis"""
import redis
from typing import Union, Optional, Callable
from uuid import uuid4


class Cache:
    """writing str to redis"""
    def __init__(self):
        """initializing a class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates a random key"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
