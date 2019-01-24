#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 07:33
:Licence GNUv3
Part of grammpy

"""
import inspect

from grammpy.exceptions import NotNonterminalException, NotRuleException, TerminalDoesNotExistsException, \
    NonterminalDoesNotExistsException
from grammpy.representation.HashContainer import HashContainer
from ..Nonterminal import Nonterminal
from ..rules import Rule
from ._TerminalSet import _TerminalSet


class RawGrammar:
    """
    Provide base interface for manipulating with the grammar
    """
    def __init__(self,
                 terminals=None,
                 nonterminals=None,
                 rules=None,
                 start_symbol=None):
        """
        Create instance of grammar
        :param terminals: Sequence of terminals to add, empty sequence by default
        :param nonterminals: Sequence of nonterminals to add, empty sequence by default
        :param rules: Sequence of rules to add, empty sequence by default
        :param start_symbol: Start symbol of the grammar, start symbol must be in nonterminals.
        None by default
        """
        terminals = [] if terminals is None else terminals
        self._terminals = _TerminalSet(self, terminals)

        nonterminals = [] if nonterminals is None else nonterminals
        rules = [] if rules is None else rules
        self.__nonterminals = HashContainer()
        self.__rules = HashContainer()
        self.__start_symbol = None
        self.add_nonterm(nonterminals)
        self.add_rule(rules)
        self.start_set(start_symbol)

    @property
    def terminals(self):
        return self._terminals


    # Non term part
    @staticmethod
    def _controll_nonterms(nonterms):
        """
        Transform parameter into sequence and check if all objects are nonterminals
        :param nonterms: Nonterminal or sequence of Nonterminal classes representing nonterminals
        :return: Sequence of nonterminals
        """
        nonterms = HashContainer.to_iterable(nonterms)
        for nonterm in nonterms:
            if not inspect.isclass(nonterm) or not issubclass(nonterm, Nonterminal):
                raise NotNonterminalException(nonterm)
        return nonterms

    def add_nonterm(self, nonterms):
        """
        Add nonterminal or nonterminals into grammar
        :param nonterms: Nonterminal or sequence of Nonterminal classes representing nonterminals
        :return: Sequence of nonterminals added into grammar
        """
        nonterms = RawGrammar._controll_nonterms(nonterms)
        return self.__nonterminals.add(nonterms)

    def remove_nonterm(self, nonterms=None):
        """
        Remove nonterminal or nonterminals from the grammar
        :param nonterms: Nonterminal or sequence of Nonterminal classes representing nonterminals
        :return: Sequence of nonterminals removed from the grammar
        """
        if nonterms is None:
            return self.__nonterminals.remove()
        nonterms = RawGrammar._controll_nonterms(nonterms)
        return self.__nonterminals.remove(nonterms)

    def have_nonterm(self, nonterms):
        """
        Check if nonterminal or nonterminals are in the grammar
        :param nonterms: Rule or sequence of Rule classes representing nonterminals
        :return: True if all nonterminals in parameter are in the grammar, false otherwise
        """
        nonterms = RawGrammar._controll_nonterms(nonterms)
        return self.__nonterminals.have(nonterms)

    def get_nonterm(self, nonterms=None):
        """
        Get nonterminals from the grammar
        :param nonterms: Nonterminal or sequence of Nonterminal classes representing nonterminals
        :return: Sequence of nonterminals in the grammar
        """
        if nonterms is None:
            return self.__nonterminals.get()
        converted = RawGrammar._controll_nonterms(nonterms)
        if not HashContainer.is_iterable(nonterms):
            return self.__nonterminals.get(converted)[0]
        return self.__nonterminals.get(converted)

    # Rules part
    def _control_rules(self, rules):
        """
        Transform parameter into sequence, check if all objects are rules and if are valid
        :param rules: Object or sequence of objects representing rules
        :return: Sequence of rules
        """
        rules = HashContainer.to_iterable(rules)
        for rule in rules:
            if not inspect.isclass(rule) or not issubclass(rule, Rule):
                raise NotRuleException(rule)
            rule.validate(self)
        return rules

    def add_rule(self, rules):
        """
        Add rule or sequence of rules into grammar
        :param rules: Object or sequence of objects representing rules
        :return: Sequence of rules added into grammar
        """
        rules = self._control_rules(rules)
        return self.__rules.add(rules)

    def remove_rule(self, rules=None, *, _validate=True):
        """
        Remove rule or sequence of rules from the grammar
        :param rules: Object or sequence of objects representing rules
        :param _validate: Flag if validate removing rules, only for internal use
        :return: Sequence of rules removed from the grammar
        """
        if rules is None:
            return self.__rules.remove()
        if _validate:
            rules = self._control_rules(rules)
        return self.__rules.remove(rules)

    def have_rule(self, rules):
        """
        Check if rule or sequence of rules are in the grammar
        :param rules: Object or sequence of objects representing rules
        :return: True if all rules in parameter are in the grammar, false otherwise
        """
        try:
            rules = self._control_rules(rules)
            return self.__rules.have(rules)
        except (TerminalDoesNotExistsException, NonterminalDoesNotExistsException):
            return False

    def get_rule(self, rules=None):
        """
        Get rule or sequence of rules stored in the grammar
        :param rules: Object or sequence of objects representing rules
        :return: Sequence of rules that are stored in the grammar
        """
        if rules is None:
            return self.__rules.get()
        converted = self._control_rules(rules)
        obtain = self.__rules.get(converted)
        if not HashContainer.is_iterable(rules):
            return obtain[0]
        return obtain

    # StartSymbol
    def start_get(self):
        """
        Get start symbol
        :return: Start symbol, None if start symbol is not set
        """
        return self.__start_symbol

    def start_set(self, nonterminal):
        """
        Set start symbol
        :param nonterminal: Nonterminal to be the start symbol
        """
        if nonterminal is None:
            self.__start_symbol = None
            return
        if not inspect.isclass(nonterminal) or not issubclass(nonterminal, Nonterminal):
            raise NotNonterminalException(nonterminal)
        if not self.have_nonterm(nonterminal):
            raise NonterminalDoesNotExistsException(None, nonterminal, self)
        self.__start_symbol = nonterminal
