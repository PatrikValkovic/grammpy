#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 22.07.2017 13:19
:Licence GNUv3
Part of grammpy

"""
from collections import Iterable


class HashContainer:
    """
    Represent container that store items based on their hashes.
    Class modify interface of set to standardize parameters.
    """

    def __init__(self, items=None):
        """
        Create new instance of HashContainer
        :param items: Items to add by default
        """
        if items is None:
            items = []
        self.__items = {}
        self.add(items)

    # Helpers
    @staticmethod
    def is_iterable(param: Iterable) -> bool:
        """
        Check if parameter is instance of Iterable
        :param param: Object to check
        :return: True if parameter is Iterable, false otherwise
        """
        return isinstance(param, Iterable)

    @staticmethod
    def to_iterable(param: Iterable):
        """
        Standardize parameter to be iterable.
        Return original sequence, if param is Iterable.
        Otherwise create Iterable object from parameter.
        :param param: Item to standardize
        :return: Iterable sequence
        """
        if not HashContainer.is_iterable(param):
            return [param]
        return param

    def add(self, item):
        """
        Add items into HashContainer
        :param item: Item or items to insert
        :return: List of added items
        """
        items = HashContainer.to_iterable(item)
        # iterace throught items
        add = []
        for t in items:
            h = hash(t)
            if h not in self.__items:
                self.__items[h] = t
                add.append(t)
        return add

    def remove(self, item=None):
        """
        Remove items from the HashContainer
        :param item: Item or items to remove
        :return: Sequence of removed items
        """
        if item is None:
            all = list(self.__items.values())
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
        """
        Check if parameter is in the container
        :param item: Item or items for which check existence
        :return: True if all items in the parameter is in the HashContainer, false otherwise.
        """
        item = HashContainer.to_iterable(item)
        for t in item:
            if hash(t) not in self.__items:
                return False
        return True

    def get(self, item=None):
        """
        Return items stored in the HashContainer
        :param item: Item or items to get
        :return: Sequence of items occurred in the HashContainer
        """
        # if no parameter is passed than return all terminals
        if item is None:
            # Maybe lazy evaluation, but it cannot be combined with return
            return self.all()
        # else return relevant to parameter
        transformed = HashContainer.to_iterable(item)
        ret = []
        for t in transformed:
            ret.append(self.__items[hash(t)] if hash(t) in self.__items else None)
        if not HashContainer.is_iterable(item):
            return ret[0]
        return ret

    def all(self):
        """
        Get all items in the container
        :return: Sequence of all items
        """
        return [item for _, item in self.__items.items()]

    def count(self):
        """
        Get count of items in the HashContainer
        :return: Count of items in the HashContainer
        :rtype Number
        """
        return len(self.__items)
