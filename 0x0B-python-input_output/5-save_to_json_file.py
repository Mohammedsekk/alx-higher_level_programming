#!/usr/bin/python3
""" module that contains save_to_json_file module """
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text
    file, using a JSON representation:
    """
    with open(filename, mode="w") as a_file:
        json.dump(my_obj, a_file)