#!/usr/bin/env python3
"""sort by average score"""
import pymongo


def top_students(mongo_collection):
    """sort by average score"""
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
