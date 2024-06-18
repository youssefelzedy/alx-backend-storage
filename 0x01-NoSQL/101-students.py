#!/usr/bin/env python3
"""
Returns all students sorted by average score:
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    cursor = mongo_collection.aggregate([
        {
            "$project":
            {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort":
            {
                "averageScore": -1
            }
        }
    ])
    return cursor
