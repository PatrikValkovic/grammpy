#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
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
    def to_iterable(param):
        # standardize it to iterable object
        if isinstance(param, str) or not isinstance(param, Iterable):
            return (param,)
        return param

    def add(self, item):
        items = HashContainer.to_iterable(item)
        # iterace throught items
        for t in items:
            self.__items[hash(t)] = t

    def remove(self, item=None):
        if item is None:
            return self.__items.clear()
        item = HashContainer.to_iterable(item)
        # iterate throught items
        for t in item:
            del self.__items[hash(t)]

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
            return [item for _, item in self.__items.items()]
        # else return relevant to parameter
        transformed = HashContainer.to_iterable(item)
        ret = []
        for t in transformed:
            ret.append(t if hash(t) in self.__items else None)
        if isinstance(item, str) or not isinstance(item, Iterable):
            return ret[0]
        return ret

    def all(self):
        for _, item in self.__items.items():
            yield item

    def count(self):
        return len(self.__items)
