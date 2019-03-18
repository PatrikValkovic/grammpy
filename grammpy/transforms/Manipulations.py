#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 24.12.2017 11:31
:Licence MIT
Part of grammpy

"""
from typing import TYPE_CHECKING, Union
from .. import Nonterminal, Terminal, Rule

if TYPE_CHECKING:  # pragma: no cover
    from ..representation.support._RuleConnectable import _RuleConnectable


class Manipulations:
    """
    Class that aggregate functions modifying the parsed tree.
    """

    @staticmethod
    def replaceRule(oldRule, newRule):
        # type: (Rule, Rule) -> Rule
        """
        Replace instance of Rule with another one.
        :param oldRule: Instance in the tree.
        :param newRule: Instance to replace with.
        :return: New instance attached to the tree.
        """
        for par in oldRule.from_symbols:
            par._set_to_rule(newRule)
            newRule._from_symbols.append(par)
        for ch in oldRule.to_symbols:
            ch._set_from_rule(newRule)
            newRule._to_symbols.append(ch)
        return newRule

    @staticmethod
    def replaceNode(oldNode, newNode):
        # type: (_RuleConnectable, _RuleConnectable) -> _RuleConnectable
        """
        Replace instance of Nonterminal or Terminal in the tree with another one.
        :param oldNode: Old nonterminal or terminal already in the tree.
        :param newNode: Instance of nonterminal or terminal to replace with.
        :return: Instance `newNode` in the tree.
        """
        if oldNode.from_rule is not None and len(oldNode.from_rule.to_symbols) > 0:
            indexParent = oldNode.from_rule.to_symbols.index(oldNode)
            oldNode.from_rule.to_symbols[indexParent] = newNode
            newNode._set_from_rule(oldNode.from_rule)
        if oldNode.to_rule is not None and len(oldNode.to_rule.from_symbols) > 0:
            indexChild = oldNode.to_rule.from_symbols.index(oldNode)
            oldNode.to_rule._from_symbols[indexChild] = newNode
            newNode._set_to_rule(oldNode.to_rule)
        return newNode

    @staticmethod
    def replace(oldEl, newEl):
        # type: (Union[Rule, _RuleConnectable], Union[Rule, _RuleConnectable]) -> Union[Rule, _RuleConnectable]
        """
        Replace element in the parsed tree. Can be nonterminal, terminal or rule.
        :param oldEl: Element already in the tree.
        :param newEl: Element to replace with.
        :return: New element attached to the tree.
        """
        if isinstance(oldEl, Rule):
            return Manipulations.replaceRule(oldEl, newEl)
        if isinstance(oldEl, (Nonterminal, Terminal)):
            return Manipulations.replaceNode(oldEl, newEl)
