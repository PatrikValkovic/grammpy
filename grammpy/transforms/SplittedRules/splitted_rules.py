#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.12.2017 16:05
:Licence MIT
Part of grammpy

"""
from typing import TYPE_CHECKING

from ..Manipulations import Manipulations
from ..Traversing import Traversing
from ...representation.support.SplitRule import SplitRule

if TYPE_CHECKING:  # pragma: no cover
    from ... import Nonterminal


def splitted_rules(root):
    # type: (Nonterminal) -> Nonterminal
    """
    Replace SplittedRules in the parsed tree with the original one.
    This method is mandatory if you insert Rule class with multiple rules into the grammar.
    :param root: Root of the parsed tree.
    :return: Modified tree.
    """
    items = Traversing.post_order(root)
    items = filter(lambda x: isinstance(x, SplitRule), items)
    for i in items:
        # create the original rule
        newRule = i.from_rule()
        # replace it with the node in the tree
        Manipulations.replace(i, newRule)
    return root
