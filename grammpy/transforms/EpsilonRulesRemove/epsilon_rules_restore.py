#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.09.2017 10:47
:Licence MIT
Part of grammpy

"""
from typing import TYPE_CHECKING, Type, Dict, Any, Union

from .remove_rules_with_epsilon import EpsilonRemovedRule
from ..Manipulations import Traversing
from ... import EPSILON, Terminal

if TYPE_CHECKING:  # pragma: no cover
    from ... import Nonterminal, Rule


def _restore_tree_for(root, translate):
    # type: (Any, Dict[Type[Nonterminal], Type[Rule]]) -> Union[Nonterminal, Terminal]
    """
    Create part of AST that generate epsilon.
    :param root: Symbol in the original rule that results in epsilon.
    Can be Nonterminal or epsilon itself.
    :param translate: Dictionary where key is nonterminal and value is rule which is next to generate epsilon.
    :return: Nonterminal instance with part of AST generating epsilon.
    """
    # the symbol is epsilon directly, just return Terminal.
    if root is EPSILON:
        return Terminal(EPSILON)
    # create nonterminal
    created_nonterm = root()  # type: Nonterminal
    created_rule = translate[root]()  # type: Rule
    created_nonterm._set_to_rule(created_rule)
    created_rule._from_symbols.append(created_nonterm)
    # all symbols from the right are rewritable to epsilon, so we need to restore them as well
    for ch in created_rule.right:
        p = _restore_tree_for(ch, translate)  # type: Nonterminal
        p._set_from_rule(created_rule)
        created_rule._to_symbols.append(p)
    return created_nonterm


def epsilon_rules_restore(root):
    # type: (Nonterminal) -> Nonterminal
    """
    Transform parsed tree to contain epsilon rules originally removed from the grammar.
    :param root: Root of the parsed tree.
    :return: Modified tree including epsilon rules.
    """
    items = Traversing.postOrder(root)
    items = filter(lambda x: isinstance(x, EpsilonRemovedRule), items)
    for rule in items:
        # create original rule
        created_rule = rule.from_rule()  # type: Rule
        # attach parrents parents
        for s in rule.from_symbols:  # type: Nonterminal
            s._set_to_rule(created_rule)
            created_rule._from_symbols.append(s)
        # attach children up to replace index (that will contain epsilon)
        for i in range(rule.replace_index):
            ch = rule.to_symbols[i]  # type: Nonterminal
            ch._set_from_rule(created_rule)
            created_rule._to_symbols.append(ch)
        # add symbols originally rewrote to epsilon
        symb = _restore_tree_for(created_rule.right[rule.replace_index], rule.backtrack)  # type: Nonterminal
        created_rule._to_symbols.append(symb)
        symb._set_from_rule(created_rule)
        # attach rest of children
        for i in range(rule.replace_index, len(rule.to_symbols)):
            ch = rule.to_symbols[i]  # type: Nonterminal
            ch._set_from_rule(created_rule)
            created_rule._to_symbols.append(ch)
    return root
