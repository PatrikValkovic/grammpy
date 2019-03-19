#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.03.2019 13:20
:Licence MIT
Part of grammpy

"""
from typing import Iterable, Any, AbstractSet


class _BaseSet(set):
    def update(self, *s):
        # type: (Iterable[Any]) -> _BaseSet
        """
        Add elements from all the parameters.
        :param s: Iterable objects with elements to add.
        :return: Current instance with inserted elements.
        """
        for iterable in s:
            self.add(*iterable)
        return self

    def __ior__(self, s):
        # type: (AbstractSet[Any]) -> _BaseSet
        """
        Add elements from all the parameters.
        :param s: Iterable objects with elements to add.
        :return: Current instance with inserted elements.
        """
        return self.update(s)

    def symmetric_difference_update(self, other):
        # type: (Iterable[Any]) -> _BaseSet
        """
        Update the TerminalSet.
        Keep elements from self and other, but discard elements that are in both.
        :param other: Iterable object with elements to compare with.
        :return: Current instance with updated state.
        """
        intersect = self.intersection(other)
        self.remove(*intersect)
        for elem in set(other).difference(intersect):
            self.add(elem)
        return self

    def __ixor__(self, s):
        # type: (Iterable[Any]) -> _BaseSet
        """
        Update the TerminalSet.
        Keep elements from self and other, but discard elements that are in both.
        :param other: Iterable object with elements to compare with.
        :return: Current instance with updated state.
        """
        return self.symmetric_difference_update(s)

    def discard(self, *elements):
        # type: (Any) -> None
        """
        Remove elements from the set.
        In case of terminals and nonterminals, remove rules using them as well.
        Unlike remove doesn't throw exception if the element is not inside the container.
        :param elements: Elements to remove
        """
        for el in elements:
            try:
                self.remove(el)
            except KeyError:
                continue

    def size(self):
        # type: () -> int
        """
        Get number of elements in the container.
        :return: Number of elements in the container.
        """
        return len(self)
