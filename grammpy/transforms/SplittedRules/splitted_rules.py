#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.12.2017 16:05
:Licence GNUv3
Part of grammpy-transforms

"""

from ...old_api import Nonterminal, Rule, EPSILON
from ...representation.grammars.MultipleRulesGrammar import SplitRule
from ..Manipulations import Manipulations, Traversing

def splitted_rules(root: Nonterminal):
    """
    Replace SplittedRules by their original rule.
    :param root: Root of the AST
    :return: Modified AST
    """
    items = Traversing.postOrder(root)
    items = filter(lambda x: isinstance(x, Rule), items)
    for i in items:
        if not isinstance(i, SplitRule):
            continue
        newRule = i.from_rule()
        Manipulations.replace(i, newRule)
    return root
