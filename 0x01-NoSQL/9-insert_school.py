#!/usr/bin/env python3
"""
Insert a document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a document in a collection
    """
    cursor = mongo_collection.insert_one(kwargs).inserted_id

    return cursor
