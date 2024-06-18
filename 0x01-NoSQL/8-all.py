#!/usr/bin/env python3
"""
Lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Use find() to retrieve all documents in the collection
    """
    cursor = mongo_collection.find()

    return cursor
