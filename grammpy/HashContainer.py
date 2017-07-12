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

    # Helpers
    def to_iterable(param):
        # standardize it to iterable object
        if isinstance(param, str) or not isinstance(param, Iterable):
            return (param,)
        return param

    def add(self, item):
        term = HashContainer.to_iterable(item)
        # iterace throught items
        for t in term:
            self.__items[hash(t)] = t

    def remove(self, term=None):
        if term is None:
            return self.__items.clear()
        term = HashContainer.to_iterable(term)
        # iterate throught items
        for t in term:
            del self.__items[hash(t)]

    def have(self, term):
        term = HashContainer.to_iterable(term)
        for t in term:
            if hash(t) not in self.__items:
                return False
        return True

    def get(self, term=None):
        # if no parameter is passed than return all terminals
        if term is None:
            # Maybe lazy evaluation, but it cannot be combined with return
            return [item for _, item in self.__items.items()]
        # else return relevant to parameter
        transformed = HashContainer.to_iterable(term)
        ret = []
        for t in transformed:
            ret.append(t if hash(t) in self.__items else None)
        if isinstance(term, str) or not isinstance(term, Iterable):
            return ret[0]
        return ret

    def term(self, term=None):
        return self.get(term)

    def terms(self):
        for _, item in self.__items.items():
            yield item

    def terms_count(self):
        return len(self.__items)
