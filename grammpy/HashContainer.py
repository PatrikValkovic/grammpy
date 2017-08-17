#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 22.07.2017 13:19
:Licence GNUv3
Part of grammpy

"""
from collections import Iterable


class HashContainer:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.__items = {}
        self.add(items)

    # Helpers
    @staticmethod
    def is_iterable(param: Iterable) -> bool:
        return isinstance(param, Iterable)

    @staticmethod
    def to_iterable(param: Iterable):
        # standardize it to iterable object
        if not HashContainer.is_iterable(param):
            return [param]
        return param

    def add(self, item):
        items = HashContainer.to_iterable(item)
        # iterace throught items
        for t in items:
            self.__items[hash(t)] = t
        return items

    def remove(self, item=None):
        if item is None:
            all = self.__items.values()
            self.__items.clear()
            return all
        item = HashContainer.to_iterable(item)
        deleted = []
        # iterate through items
        for t in item:
            h = hash(t)
            if h in self.__items:
                deleted.append(self.__items[h])
                del self.__items[h]
        return deleted

    def have(self, item):
        item = HashContainer.to_iterable(item)
        for t in item:
            if hash(t) not in self.__items:
                return False
        return True

    def get(self, item=None):
        # if no parameter is passed than return all terminals
        if item is None:
            # Maybe lazy evaluation, but it cannot be combined with return
            return self.all()
        # else return relevant to parameter
        transformed = HashContainer.to_iterable(item)
        ret = []
        for t in transformed:
            ret.append(t if hash(t) in self.__items else None)
        if not HashContainer.is_iterable(item):
            return ret[0]
        return ret

    def all(self):
        return [item for _, item in self.__items.items()]

    def count(self):
        return len(self.__items)
