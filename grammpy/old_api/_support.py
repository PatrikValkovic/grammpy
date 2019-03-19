#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.02.2019 20:17
:Licence MIT
Part of grammpy

"""

from typing import TYPE_CHECKING, List, Type

if TYPE_CHECKING:  # pragma: no cover
    from .Grammar import Grammar
    from .. import Rule


class RulesClass:
    """
    Class that help old API Grammar to distinguish between call of rules method and access to rule property.
    """

    def __init__(self, gr):
        # type: (Grammar) -> None
        """
        Return new instance of RulesClass.
        This class is only for internal use.
        :param gr: Grammar to reference.
        """
        self._gr = gr
        super().__init__()

    def __call__(self):
        # type: () -> List[Type[Rule]]
        """
        Get all rules within the grammar.
        :return: List of rules in the grammar.
        """
        return self._gr._rules()

    def __iter__(self):
        return self._gr._gr.rules.__iter__()

    def __getattribute__(self, item):
        if item in {'__call__', '_gr'}:
            return object.__getattribute__(self, item)
        return getattr(self._gr._gr.rules, item)
