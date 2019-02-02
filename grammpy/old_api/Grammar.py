#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 24.01.2019 13:04
:Licence GPLv3
Part of grammpy

"""
from collections import Iterable
from copy import copy
from typing import List, Union, Type, Optional, TYPE_CHECKING, Any, Generator

from deprecated import deprecated

from ._support import RulesClass
from .. import Grammar as NewGrammar, Terminal, Rule

if TYPE_CHECKING:  # pragma: no-cover
    from .. import Nonterminal
    from ..representation.support._NonterminalSet import _NonterminalSet
    from ..representation.support._TerminalSet import _TerminalSet


@deprecated(version='2.0.0', reason='Use new API')
class Grammar:
    """
    Provide base interface for manipulating with the grammar.
    This grammar is deprecated and it's only bridge between the old and new API.
    You should use new API, implementation of this class is less efficient.
    """

    def __init__(self,
                 terminals=None,
                 nonterminals=None,
                 rules=None,
                 start_symbol=None):
        # type: (Optional[Iterable[Any]], Optional[Iterable[Type[Nonterminal]]], Optional[Iterable[Type[Rule]]], Optional[Type[Nonterminal]]) -> Grammar
        """
        Create instance of grammar.
        :param terminals: Sequence of terminals to add, empty sequence by default.
        :param nonterminals: Sequence of nonterminals to add, empty sequence by default.
        :param rules: Sequence of rules to add, empty sequence by default.
        :param start_symbol: Start symbol of the grammar, start symbol must be in nonterminals.
        """
        self._gr = NewGrammar(terminals=terminals,
                              nonterminals=nonterminals,
                              rules=rules,
                              start_symbol=start_symbol)
        self.rules = RulesClass(self)

    # Term part
    def add_term(self, term):
        # type: (Union[Iterable[Any], Any]) -> List[Terminal]
        """
        Add terminal or terminals into grammar.
        :param term: Object or sequence of objects representing terminals.
        :return: List terminals added into grammar as sequence of Terminal instances.
        """
        return list(self._add_term(term))

    def _add_term(self, term):
        # type: (Union[Iterable[Any], Any]) -> Generator[Terminal]
        """
        Add terminal or terminals into grammar.
        :param term: Object or sequence of objects representing terminals.
        :return: List terminals added into grammar as sequence of Terminal instances.
        """
        term = [] if term is None else term
        if not isinstance(term, Iterable) or isinstance(term, str):
            term = [term]
        for t in term:
            if t not in self._gr.terminals:
                self._gr.terminals.add(t)
                yield Terminal(t)

    def remove_term(self, term=None):
        # type: (Optional[Union[Iterable[Any], Any]]) -> List[Terminal]
        """
        Delete terminal or terminals from grammar.
        :param term: Object or sequence of objects representing terminals.
        :return: List of terminals removed from the grammar as sequence of Terminal instances.
        """
        term = self._gr.terminals if term is None else term
        if not isinstance(term, Iterable) or isinstance(term, str):
            term = [term]
        tmp = []
        for t in list(term):
            for i in self._gr.terminals:
                if i == t:
                    tmp.append(Terminal(i))
            self._gr.terminals.remove(t)
        return tmp

    def have_term(self, term):
        # type: (Union[Iterable[Any], Any]) -> bool
        """
        Check if terminal or terminals are in the grammar.
        :param term: Object or sequence of objects representing terminals.
        :return: True if all objects in the parameter are in the grammar, false otherwise.
        """
        term = [] if term is None else term
        if not isinstance(term, Iterable) or isinstance(term, str):
            term = [term]
        for t in term:
            if t not in self._gr.terminals:
                return False
        return True

    def get_term(self, term=None):
        # type: (Optional[Union[Iterable[Any], Any]]) -> Union[Optional[Terminal], List[Optional[Terminal]]]
        """
        Get terminals stored in grammar that match terminal or terminals passed as parameter.
        :param term: Object or sequence of objects representing terminals.
        :return: List of terminals in the grammar as sequence of Terminal object.
        Terminal or terminals that weren't in the grammar are replaced with None value.
        Return single value if parameter is single value, return list if parameter is iterable.
        If the parameter is None (default), return all terminals.
        """
        if term is None:
            return [Terminal(i) for i in self._gr.terminals]
        is_single = False
        if not isinstance(term, Iterable) or isinstance(term, str):
            term = [term]
            is_single = True
        tmp = []
        for t in term:
            handled = False
            for i in self._gr.terminals:
                if t == i and is_single is not True:
                    handled = True
                    tmp.append(Terminal(i))
                elif t == i:
                    return Terminal(i)
            if not handled and is_single is not True:
                tmp.append(None)
            elif not handled:
                return None
        return tmp

    def term(self, term=None):
        # type: (Optional[Union[Iterable[Any], Any]]) -> Union[Optional[Terminal], List[Optional[Terminal]]]
        """
        Get terminals stored in grammar that match terminal or terminals passed as parameter.
        :param term: Object or sequence of objects representing terminals.
        :return: List of terminals in the grammar as sequence of Terminal object.
        Terminal or terminals that weren't in the grammar are replaced with None value.
        Return single value if parameter is single value, return list if parameter is iterable.
        If the parameter is None (default), return all terminals.
        """
        return self.get_term(term)

    def terms(self):
        # type: () -> List[Terminal]
        """
        Get all terminals within the grammar.
        :return: List of terminals in the grammar as Terminal instances.
        """
        return self.get_term(None)

    def terms_count(self):
        # type: () -> int
        """
        Get number of terminals within the grammar.
        :return: Number of terminals within the grammar.
        """
        return len(self._gr.terminals)

    def terms_clear(self):
        # type: () -> List[Terminal]
        """
        Delete all terminals from grammar.
        :return: List of terminals removed from the grammar as list of Terminal instances.
        """
        return self.remove_term(None)

    # Nonterm part
    def add_nonterm(self, nonterm):
        # type: (Union[Iterable[Type[Nonterminal]], Type[Nonterminal]]) -> List[Type[Nonterminal]]
        """
        Add nonterminal or nonterminals into grammar.
        :param nonterm: Single or sequence of nonterminals.
        :return: List of nonterminals added into the grammar.
        """
        return list(self._add_nonterm(nonterm))

    def _add_nonterm(self, nonterm):
        # type: (Union[Iterable[Type[Nonterminal]], Type[Nonterminal]]) -> Generator[Type[Nonterminal]]
        """
        Add nonterminal or nonterminals into grammar.
        :param nonterm: Single or sequence of nonterminals.
        :return: List of nonterminals added into the grammar.
        """
        nonterm = [] if nonterm is None else nonterm
        if not isinstance(nonterm, Iterable):
            nonterm = [nonterm]
        for t in nonterm:
            if t not in self._gr.nonterminals:
                self._gr.nonterminals.add(t)
                yield t

    def remove_nonterm(self, nonterm=None):
        # type: (Optional[Union[Iterable[Type[Nonterminal]], Type[Nonterminal]]]) -> List[Type[Nonterminal]]
        """
        Delete nonterminal or nonterminals from the grammar.
        :param nonterm: Single or sequence of nonterminals to remove.
        :return: List of nonterminals removed from the grammar.
        """
        nonterm = self._gr.nonterminals if nonterm is None else nonterm
        if not isinstance(nonterm, Iterable):
            nonterm = [nonterm]
        tmp = []
        for t in list(nonterm):
            if t in self._gr.nonterminals:
                tmp.append(t)
                self._gr.nonterminals.remove(t)
        return tmp

    def have_nonterm(self, nonterm):
        # type: (Union[Iterable[Type[Nonterminal]], Type[Nonterminal]]) -> bool
        """
        Check if nonterminal or nonterminals are in the grammar.
        :param nonterm: Single or sequence of nonterminals to check.
        :return: True if all nonterminals in the parameter are in the grammar, false otherwise.
        """
        nonterm = [] if nonterm is None else nonterm
        if not isinstance(nonterm, Iterable):
            nonterm = [nonterm]
        contains = True
        for t in nonterm:
            contains = t in self._gr.nonterminals and contains
        return contains

    def get_nonterm(self, nonterm=None):
        # type: (Optional[Union[Iterable[Type[Nonterminal]], Type[Nonterminal]]]) -> Union[Optional[Type[Nonterminal]], List[Optional[Type[Nonterminal]]]]
        """
        Get nonterminals stored in grammar that match nonterminal or nonterminals passed as parameter.
        :param nonterm: Single or sequence of nonterminals.
        :return: List of nonterminals in the grammar.
        Nonterminal or nonterminals that weren't in the grammar are replaced with None value.
        Return single value if parameter is single value, return list if parameter is iterable.
        If the parameter is None (default), return all nonterminals.
        """
        if nonterm is None:
            return list(self._gr.nonterminals)
        is_single = False
        if not isinstance(nonterm, Iterable):
            nonterm = [nonterm]
            is_single = True
        tmp = []
        for t in nonterm:
            if t in self._gr.nonterminals and is_single is not True:
                tmp.append(t)
            elif t in self._gr.nonterminals:
                return t
            elif is_single is not True:
                tmp.append(None)
            else:
                return None
        return tmp

    def nonterm(self, nonterm=None):
        # type: (Optional[Union[Iterable[Type[Nonterminal]], Type[Nonterminal]]]) -> Union[Optional[Type[Nonterminal]], List[Optional[Type[Nonterminal]]]]
        """
        Get nonterminals stored in grammar that match nonterminal or nonterminals passed as parameter.
        :param nonterm: Single or sequence of nonterminals.
        :return: List of nonterminals in the grammar.
        Nonterminal or nonterminals that weren't in the grammar are replaced with None value.
        Return single value if parameter is single value, return list if parameter is iterable.
        If the parameter is None (default), return all nonterminals.
        """
        return self.get_nonterm(nonterm)

    def nonterms(self):
        # type: () -> List[Type[Nonterminal]]
        """
        Get all nonterminals within the grammar.
        :return: List of nonterminals in the grammar.
        """
        return self.get_nonterm(None)

    def nonterms_count(self):
        # type: () -> int
        """
        Get number of nonterminals in the grammar.
        :return: Number of nonterminals in the grammar.
        """
        return len(self._gr.nonterminals)

    def nonterms_clear(self):
        # type: () -> List[Type[Nonterminal]]
        """
        Delete all nonterminals from grammar.
        :return: List of nonterminals removed from the grammar.
        """
        return self.remove_nonterm(None)

    # Rules part
    def add_rule(self, rules):
        # type: (Union[Iterable[Type[Rule]], Type[Rule]]) -> List[Type[Rule]]
        """
        Add rule or rules into grammar.
        :param rules: Single or sequence of rules.
        :return: List of rules added into the grammar.
        """
        rules = [] if rules is None else rules
        if not isinstance(rules, Iterable):
            rules = [rules]
        return list(self._gr.rules.add(*rules))

    def remove_rule(self, rules=None, *, _validate=True):
        # type: (Optional[Union[Iterable[Type[Rule]], Type[Rule]]], None, bool) -> List[Type[Rule]]
        """
        Delete rule or rules from the grammar.
        :param rules: Single or sequence of rules to remove.
        :param _validate: True if the rule should be validated before deleting.
        This parameter is only for internal use.
        :return: List of rules removed from the grammar.
        """
        rules = self._gr.rules if rules is None else rules
        if not isinstance(rules, Iterable):
            rules = [rules]
        tmp = []
        for t in list(rules):
            if t in self._gr.rules:
                tmp.append(t)
                self._gr.rules.remove(t)
        return tmp

    def have_rule(self, rules):
        # type: (Union[Iterable[Type[Rule]], Type[Rule]]) -> bool
        """
        Check if rule or rules are in the grammar.
        :param rules: Single or sequence of rules to check.
        :return: True if all rules in the parameter are in the grammar, false otherwise.
        """
        rules = [] if rules is None else rules
        if not isinstance(rules, Iterable):
            rules = [rules]
        contains = True
        for t in rules:
            contains = t in self._gr.rules and contains
        return contains

    def get_rule(self, rules=None):
        # type: (Optional[Union[Iterable[Type[Rule]], Type[Rule]]]) -> Union[Optional[Type[Rule]], List[Optional[Type[Rule]]]]
        """
        Get rules stored in grammar that match rule or rules passed as parameter.
        :param rules: Single or sequence of rules.
        :return: List of rules in the grammar.
        Rule or rules that weren't in the grammar are replaced with None value.
        Return single value if parameter is single value, return list if parameter is iterable.
        If the parameter is None (default), return all rules.
        """
        if rules is None:
            return list(self._gr.rules)
        is_single = False
        if not isinstance(rules, Iterable):
            rules = [rules]
            is_single = True
        result = []
        for rule in rules:
            rule.validate(self._gr)
            result = result + self._gr.rules.get(rule)
        return result[0] if is_single and len(result) == 1 else result

    def rule(self, rules=None):
        # type: (Optional[Union[Iterable[Type[Rule]], Type[Rule]]]) -> Union[Optional[Type[Rule]], List[Optional[Type[Rule]]]]
        """
        Get rules stored in grammar that match rule or rules passed as parameter.
        :param rules: Single or sequence of rules.
        :return: List of rules in the grammar.
        Rule or rules that weren't in the grammar are replaced with None value.
        Return single value if parameter is single value, return list if parameter is iterable.
        If the parameter is None (default), return all rules.
        """
        return self.get_rule(rules)

    def _rules(self):
        # type: () -> List[Type[Rule]]
        """
        Get all rules within the grammar.
        :return: List of rules in the grammar.
        """
        return self.get_rule()

    def rules_count(self):
        # type: () -> int
        """
        Get number of rules in the grammar.
        :return: Number of rules in the grammar.
        """
        return len(self._gr.rules)

    def rules_clear(self):
        # type: () -> List[Type[Rule]]
        """
        Delete all rules from grammar.
        :return: List of rules removed from the grammar.
        """
        return self.remove_rule(None)

    # StartSymbol
    def start_get(self):
        # type: () -> Optional[Type[Nonterminal]]
        """
        Get start symbol of the grammar. Default value is None.
        :return: Start symbol of the grammar.
        """
        return self._gr.start

    def start_set(self, nonterminal):
        # type: (Optional[Type[Nonterminal]]) -> None
        """
        Set start symbol of the grammar.
        You can set start symbol to None to clear the start symbol.
        :param nonterminal: New start symbol.
        The start symbol needs to be in the nonterminals.
        :raise NonterminalDoesNotExistsException: If the start symbol is not in nonterminals.
        """
        self._gr.start = nonterminal

    def start_isSet(self):
        # type: () -> bool
        """
        Check if the start symbol is set. That mean if the start symbol is not None.
        :return: True if the start symbol is set, false otherwise.
        """
        return self._gr.start is not None

    def start_is(self, nonterminal):
        # type: (Type[Nonterminal]) -> bool
        """
        Check if start symbol is nonterminal passed as parameter.
        :param nonterminal: Nonterminal to check.
        :return: True if start symbol is parameter, false otherwise.
        """
        return self._gr.start is nonterminal

    # Copy
    def __copy__(self):
        # type: () -> Grammar
        """
        Create shallow copy of the grammar.
        :return: Shallow copy of the grammar.
        """
        new_grammar = copy(self._gr)
        i = Grammar()
        i._gr = new_grammar
        return i

    # New API
    @property
    def terminals(self):
        # type: () -> _TerminalSet
        """
        Get set representing terminals.
        :return: Set representing terminals.
        """
        return self._terminals

    @property
    def nonterminals(self):
        # type: () -> _NonterminalSet
        """
        Get set representing nonterminals.
        :return: Set representing nonterminals.
        """
        return self._nonterminals

    @property
    def start(self):
        # type: () -> Optional[Type[Nonterminal]]
        """
        Get start symbol of the grammar.
        :return: Start symbol of the grammar, or None if it isn't defined.
        """
        return self._gr.start

    @start.setter
    def start(self, s):
        # type: (Optional[Type[Nonterminal]]) -> None
        """
        Set start symbol of the grammar.
        :param s: Start symbol to set.
        :raise NonterminalDoesNotExistsException: If the start symbol is not in nonterminals.
        """
        self._gr.start = s

    @start.deleter
    def start(self):
        # type: () -> None
        """
        Unset start symbol and set it to None.
        """
        del self._gr.start
