#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """Using __dict__"""
    return obj.__dict__.copy()

