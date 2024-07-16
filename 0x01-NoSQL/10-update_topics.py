#!/usr/bin/env python3
"""changing topic on docs"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """changing topic on docs"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
