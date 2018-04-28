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

    # Nonterminals
    def nonterm(self, nonterms=None):
        """
        Shortcut for get_nonterm method
        """
        return self.get_nonterm(nonterms)

    def nonterms(self):
        """
        Get all nonterminals in the gramamr
        """
        return self.nonterm()

    def nonterms_count(self):
        """
        Get count of nonterminals in the grammar
        :return: Count of nonterminals
        """
        return len(self.nonterms())

    def nonterms_clear(self):
        """
        Delete all nonterminals in the grammar
        :return: Sequence of nonterminals stored in the grammar
        """
        return self.remove_nonterm()

    # Terminals
    def term(self, term=None):
        """
        Shortcut for get_term method
        """
        return self.get_term(term)

    def terms(self):
        """
        Get all terminals in the grammar
        :return: Sequence of terminals
        """
        return self.term()

    def terms_count(self):
        """
        Get count of terminals stored in the grammar
        :return: Count of terminals
        """
        return len(self.terms())

    def terms_clear(self):
        """
        Delete all terminals from the grammar
        :return: Sequence of deleted terminals
        """
        return self.remove_term()
