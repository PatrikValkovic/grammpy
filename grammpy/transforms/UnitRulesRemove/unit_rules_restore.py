#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.09.2017 10:48
:Licence MIT
Part of grammpy

"""
from typing import TYPE_CHECKING

from .remove_unit_rules import ReducedUnitRule
from ..Traversing import Traversing

if TYPE_CHECKING:  # pragma: no cover
    from ... import Nonterminal, Rule


def unit_rules_restore(root):
    # type: (Nonterminal) -> Nonterminal
    """
    Transform parsed tree for grammar with removed unit rules.
    The unit rules will be returned back to the tree.
    :param root: Root of the parsed tree.
    :return: Modified tree.
    """
    items = Traversing.post_order(root)
    items = filter(lambda x: isinstance(x, ReducedUnitRule), items)
    for rule in items:
        parent_nonterm = rule.from_symbols[0]  # type: Nonterminal
        # restore chain of unit rules
        for r in rule.by_rules:
            created_rule = r()  # type: Rule
            parent_nonterm._set_to_rule(created_rule)
            created_rule._from_symbols.append(parent_nonterm)
            created_nonterm = r.toSymbol()  # type: Nonterminal
            created_rule._to_symbols.append(created_nonterm)
            created_nonterm._set_from_rule(created_rule)
            parent_nonterm = created_nonterm
        # restore last rule
        last_rule = rule.end_rule()  # type: Rule
        last_rule._from_symbols.append(parent_nonterm)
        parent_nonterm._set_to_rule(last_rule)
        for ch in rule.to_symbols:  # type: Nonterminal
            ch._set_from_rule(last_rule)
            last_rule._to_symbols.append(ch)
    return root
