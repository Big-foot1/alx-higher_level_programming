#!/usr/bin/python3
"""
Base Module
"""
import json
import csv


class Base:
    """
    The Base Class
    Attributes:
        __nb_object : private class atribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init
        Attributes:
            id (): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def to_json_string(list_dictionaries):
        """
            Return A JSON STRING a representation list_dict..
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Save Dict To Json
        """
        d = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    d.append(obj.to_dictionary())
            f.write(cls.to_json_string(d))
