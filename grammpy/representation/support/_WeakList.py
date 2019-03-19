#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 12:11
:Licence MIT
Part of grammpy


Original implementation: https://github.com/apieum/weakreflist
Changes: List raise TreeDeletedException instead of reducing its size
"""

import weakref
from typing import List, Optional, Any, Iterator, Iterable, Callable

from ...exceptions import TreeDeletedException


class _WeakList(list):
    """
    Class that behave like list, but store just weakref of items.
    """

    def __init__(self, items=None):
        # type: (Optional[List[object]]) -> _WeakList
        """
        Create instance of _Weaklist.
        :param items: Optional iterable object with values to add.
        """
        list.__init__(self, self._refs(items or []))

    def value(self, item):
        # type: (Any) -> Any
        """
        Return value stored in weakref.
        :param item: Object from which get the value.
        :return: Value stored in the weakref, otherwise original value.
        :raise TreeDeletedException: when weakref is already deleted.
        """
        if isinstance(item, weakref.ReferenceType):
            if item() is None:
                raise TreeDeletedException()
            return item()
        return item

    def ref(self, item):
        # type: (Any) -> weakref.ReferenceType
        """
        Create weakref for the parameter.
        :param item: Object from which make the weak ref.
        :return: Weakref of parameter, parameter if exception occurs.
        """
        try:
            item = weakref.ref(item)
        finally:
            return item

    def __contains__(self, item):
        # type(Any) -> bool
        """
        Check if is parameter in WeakList.
        :param item: Object to check the existence.
        :return: True if is parameter in WeakList, false otherwise.
        """
        return list.__contains__(self, self.ref(item))

    def __getitem__(self, index):
        # type: (int) -> Any
        """
        Return item on index.
        :param index: Index of item.
        :return: Element at specific index.
        """
        items = list.__getitem__(self, index)
        return type(self)(self._values(items)) if isinstance(index, slice) else self.value(items)

    def __setitem__(self, index, item):
        # type: (int, Any) -> None
        """
        Set value at specific index.
        :param index: Index where to store item.
        :param item: Item to store.
        """
        items = self._refs(item) if isinstance(index, slice) else self.ref(item)
        return list.__setitem__(self, index, items)

    def __iter__(self):
        # type: () -> Iterator[Any]
        """
        Get iterator fot WeakList.
        :return: Iterator of the list.
        """
        return iter(self[index] for index in range(len(self)))

    def __reversed__(self):
        # type: () -> _WeakList
        """
        Reverse items in WeakList.
        The original list is unmodified.
        :return: Reversed list.
        """
        reversed_self = type(self)(self)
        reversed_self.reverse()
        return reversed_self

    def append(self, item):
        # type: (Any) -> None
        """
        Add parameter to the end of the WeakList.
        :param item: Item to add.
        """
        list.append(self, self.ref(item))

    def remove(self, item):
        # type: (Any) -> None
        """
        Remove first occurrence of the parameter.
        :param item: Value to delete from the WeakList.
        """
        return list.remove(self, self.ref(item))

    def remove_all(self, item):
        # type: (Any) -> None
        """
        Remove all occurrence of the parameter.
        :param item: Value to delete from the WeakList.
        """
        item = self.ref(item)
        while list.__contains__(self, item):
            list.remove(self, item)

    def index(self, item, **kwargs):
        # type: (Any, dict) -> int
        """
        Get index of the parameter.
        :param item: Item for which get the index.
        :return: Index of the parameter in the WeakList.
        """
        return list.index(self, self.ref(item), **kwargs)

    def count(self, item):
        # type: (Any) -> int
        """
        Get count of items that match the parameter.
        :param item: Item for which search occurrence.
        :return: Count of items in the WeakList.
        """
        return list.count(self, self.ref(item))

    def pop(self, index=-1):
        # type: (int) -> Any
        """
        Delete item at specific position (last by default) and return it.
        :param index: Index where to delete the item, last item by default.
        :return: Deleted item.
        """
        return self.value(list.pop(self, index))

    def insert(self, index, item):
        # type: (int, Any) -> None
        """
        Insert item at the specific index.
        :param index: Index where to insert the item.
        :param item: Item to insert.
        """
        return list.insert(self, index, self.ref(item))

    def extend(self, items):
        # type: (Iterable[Any]) -> None
        """
        Add items to the end of the WeakList.
        :param items: Iterable object of items to insert.
        """
        return list.extend(self, self._refs(items))

    def __iadd__(self, other):
        # type: (Iterable[Any]) -> _WeakList
        """
        Join WeakList with another iterable.
        :param other: Iterable to join with.
        """
        return list.__iadd__(self, self._refs(other))

    def _refs(self, items):
        # type: (Iterable[Any]) -> Iterable[weakref.ReferenceType]
        """
        Call ref on every item in the parameter.
        :param items: Iterable of items.
        :return: Iterable of weakrefs.
        """
        return map(self.ref, items)

    def _values(self, items):
        # type: (Iterable[weakref.ReferenceType]) -> Iterable[Any]
        """
        Call value on every item.
        :param items: Iterable of items.
        :return: Iterable of values.
        """
        return map(self.value, items)

    def _sort_key(self, key=None):
        return self.value if key is None else lambda item: key(self.value(item))

    def sort(self, *, key: Optional[Callable[[Any], Any]] = None, reverse: bool = False) -> None:
        """
        Sort _WeakList.
        :param key: Key by which to sort, default None.
        :param reverse: True if return reversed WeakList, false by default.
        """
        return list.sort(self, key=self._sort_key(key), reverse=reverse)
