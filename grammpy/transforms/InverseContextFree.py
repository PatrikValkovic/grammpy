#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.09.2017 10:49
:Licence MIT
Part of grammpy

"""
from typing import TYPE_CHECKING

from .ChomskyForm import transform_from_chomsky_normal_form
from .EpsilonRulesRemove import epsilon_rules_restore
from .UnitRulesRemove import unit_rules_restore

if TYPE_CHECKING:
    from .. import Nonterminal

__all__ = ['InverseContextFree']


class InverseContextFree:
    """
    Class that aggregates functions transforming Context-Free parsed tree.
    """

    @staticmethod
    def unit_rules_restore(root):
        # type: (Nonterminal) -> Nonterminal
        """
        Transform parsed tree for grammar with removed unit rules.
        The unit rules will be returned back to the tree.
        :param root: Root of the parsed tree.
        :return: Modified tree.
        """
        return unit_rules_restore(root)

    @staticmethod
    def epsilon_rules_restore(root):
        # type: (Nonterminal) -> Nonterminal
        """
        Transform parsed tree to contain epsilon rules originally removed from the grammar.
        :param root: Root of the parsed tree.
        :return: Modified tree including epsilon rules.
        """
        return epsilon_rules_restore(root)

    @staticmethod
    def transform_from_chomsky_normal_form(root):
        # type: (Nonterminal) -> Nonterminal
        """
        Transform the tree created by grammar in the Chomsky Normal Form to original rules.
        :param root: Root of parsed tree.
        :return: Modified tree.
        """
        return transform_from_chomsky_normal_form(root)
