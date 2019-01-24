#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 07:33
:Licence GNUv3
Part of grammpy

"""

from .MultipleRulesGrammar import MultipleRulesGrammar


class PrettyApiGrammar(MultipleRulesGrammar):
    """
    Extend interface of the grammar
    """

    # Start symbol
    def start_isSet(self):
        """
        Check if start symbol is setted
        :return: True if start symbol is setted, false otherwise
        """
        return self.start_get() is not None

    def start_is(self, nonterminal):
        """
        Check if start symbol is nonterminal
        :param nonterminal: Nonterminal to check
        :return: True if start symbol is parameter, false otherwise
        """
        return self.start_get() is nonterminal

    # Rules
    def rule(self, rules=None):
        """
        Shortcut for get_rule method
        """
        return self.get_rule(rules)

    def rules(self):
        """
        Get all rules in the grammar
        """
        return self.rule()

    def rules_count(self):
        """
        Get count of rules stored in the grammar
        :return: Count of rules
        """
        return len(self.rules())

    def rules_clear(self):
        """
        Delete all rules in the grammar
        :return: Sequence of deleted rules
        """
        return self.remove_rule()