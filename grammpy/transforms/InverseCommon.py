#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.12.2017 16:03
:Licence GNUv3
Part of grammpy

"""
from typing import TYPE_CHECKING

from .SplittedRules import splitted_rules

if TYPE_CHECKING:  # pragma no cover
    from .. import Nonterminal


class InverseCommon:
    """
    Class that aggregates functions transforming common parsed tree.
    """

    @staticmethod
    def splitted_rules(root):
        # type: (Nonterminal) -> Nonterminal
        """
        Replace SplittedRules in the parsed tree with the original one.
        This method is mandatory if you insert Rule class with multiple rules into the grammar.
        :param root: Root of the parsed tree.
        :return: Modified tree.
        """
        # TODO should by done automatically
        return splitted_rules(root)
