#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 07:33
:Licence GNUv3
Part of grammpy

"""
import inspect
from typing import Type, Optional

from grammpy.exceptions import NotNonterminalException, NotRuleException, TerminalDoesNotExistsException, \
    NonterminalDoesNotExistsException
from grammpy.representation.HashContainer import HashContainer
from ..Nonterminal import Nonterminal
from ..rules import Rule
from ._TerminalSet import _TerminalSet
from ._NonterminalSet import _NonterminalSet


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
        self._nonterminals = _NonterminalSet(self, nonterminals)

        self._start_symbol = None
        self.start = start_symbol

        rules = [] if rules is None else rules
        self.__rules = HashContainer()
        self.add_rule(rules)

    @property
    def terminals(self):
        # type: () -> _TerminalSet
        return self._terminals

    @property
    def nonterminals(self):
        # type: () -> _NonterminalSet
        return self._nonterminals

    @property
    def start(self):
        # type: () -> Optional[Type[Nonterminal]]
        return self._start_symbol

    @start.setter
    def start(self, s):
        # type: (Optional[Type[Nonterminal]]) -> None
        if s is not None and s not in self.nonterminals:
            raise NonterminalDoesNotExistsException(None, s, self)
        self._start_symbol = s

    @start.deleter
    def start(self):
        # type: () -> None
        self.start = None


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
