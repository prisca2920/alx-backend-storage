#!/usr/bin/env python3
"""lists all docs in py"""
import pymongo


def list_all(mongo_collection):
    """lists all docs in py"""
    docs = mongo_collection.find()
    return docs
