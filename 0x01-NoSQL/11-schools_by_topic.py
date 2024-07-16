#!/usr/bin/env python3
"""returns a list of topics in school"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """returns a list of topics in school"""
    return mongo_collection.find({"topic": topic})
