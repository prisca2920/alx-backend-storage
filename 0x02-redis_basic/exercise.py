#!/usr/bin/env python3
"""writing str to redis"""
import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """how many times the cache class was called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """the decorated function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ store the history of inputs and outputs for a particular function"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """defines call history method"""
        input = str(args)
        self._redis.rpush(key + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(key + ":outputs", output)
        return output
    return wrapper


class Cache:
    """writing str to redis"""
    def __init__(self):
        """initializing a class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates a random key"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str,
            fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
        """convert the data back to the desired format"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """automatically parametrize to str"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """automatically parametrize to int"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
