#!/usr/bin/env python3
"""inserts doc in py"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """inserts docs in py"""
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
