#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.09.2017 10:46
:Licence MIT
Part of grammpy

"""
from collections import deque
from typing import TYPE_CHECKING

from .transform_to_chomsky_normal_form import *
from ..Manipulations import Manipulations
from ..Traversing import Traversing

if TYPE_CHECKING:  # pragma: no cover
    from ... import Nonterminal


def transform_from_chomsky_normal_form(root):
    # type: (Nonterminal) -> Nonterminal
    """
    Transform the tree created by grammar in the Chomsky Normal Form to original rules.
    :param root: Root of parsed tree.
    :return: Modified tree.
    """
    # Transforms leaves
    items = Traversing.post_order(root)
    items = filter(lambda x: isinstance(x, (ChomskyTermRule, ChomskyTerminalReplaceRule)), items)
    de = deque(items)
    while de:
        rule = de.popleft()
        if isinstance(rule, ChomskyTermRule):
            upper_nonterm = rule.from_symbols[0]  # type: Nonterminal
            term = rule.to_symbols[0]
            Manipulations.replaceNode(upper_nonterm, term)
        elif isinstance(rule, ChomskyTerminalReplaceRule):
            created_rule = rule.from_rule()  # type: Rule
            Manipulations.replaceRule(rule, created_rule)
            de.append(created_rule)

    # Transform inner nodes
    items = Traversing.post_order(root)
    items = filter(lambda x: isinstance(x, ChomskySplitRule), items)
    de = deque(items)
    while de:
        rule = de.popleft()
        if isinstance(rule, ChomskySplitRule):
            created_rule = rule.from_rule()  # type: Rule
            # parent nonterminals
            for p in rule.from_symbols:  # type: Nonterminal
                p._set_to_rule(created_rule)
                created_rule._from_symbols.append(p)
            # left child
            left_child = rule.to_symbols[0]  # type: Nonterminal
            left_child._set_from_rule(created_rule)
            created_rule._to_symbols.append(left_child)
            # right children
            for ch in rule.to_symbols[1].to_rule.to_symbols:  # type: Nonterminal
                ch._set_from_rule(created_rule)
                created_rule.to_symbols.append(ch)
            # add back if the rules is ChomskySplitRule again
            de.appendleft(created_rule)
    return root
