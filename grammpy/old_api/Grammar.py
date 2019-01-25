#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 24.01.2019 13:04
:Licence GPLv3
Part of grammpy

"""
from collections import Iterable
from typing import List, Union, Type, Optional

from .. import Grammar as NewGrammar, Terminal, Rule


class Grammar:
    """
    Provide base interface for manipulating with the grammar
    """

    def __init__(self,
                 terminals=None,
                 nonterminals=None,
                 rules=None,
                 start_symbol=None):
        self._gr = NewGrammar(terminals=terminals,
                              nonterminals=nonterminals,
                              rules=rules,
                              start_symbol=start_symbol)

    # Term part
    def add_term(self, term):
        """
        Add terminal or terminals into grammar
        :param term: Object or sequence of objects representing terminals
        :return: List terminals added into grammar as sequence of Terminal instances
        """
        return list(self._add_term(term))

    def _add_term(self, term):
        if term is None:
            term = []
        if not isinstance(term, Iterable) or isinstance(term, str):
            term = [term]
        for t in term:
            if t not in self._gr.terminals:
                self._gr.terminals.add(t)
                yield Terminal(t, self._gr)

    def remove_term(self, term=None):
        """
        Delete terminal or terminals from grammar
        :param term: Object or sequence of objects representing terminals
        :return: List of terminals removed from the grammar as sequence of Terminal instances
        """
        if term is None:
            term = self._gr.terminals
        if not isinstance(term, Iterable) or isinstance(term, str):
            term = [term]
        tmp = []
        for t in list(term):
            for i in self._gr.terminals:
                if i == t:
                    tmp.append(Terminal(i, self._gr))
            self._gr.terminals.remove(t)
        return tmp

    def have_term(self, term):
        """
        Check if terminal or terminals are in the grammar
        :param term: Object or sequence of objects representing terminals
        :return: True if all objects in the parameter are in the grammar, false otherwise
        """
        if term is None:
            term = []
        if not isinstance(term, Iterable) or isinstance(term, str):
            term = [term]
        for t in term:
            if t not in self._gr.terminals:
                return False
        return True

    def get_term(self, term=None):
        """
        Get terminals stored in grammar that match terminal or terminals passed as parameter
        :param term: Object or sequence of objects representing terminals
        :return: List of terminals in the grammar as sequence of Terminal object
        """
        if term is None:
            return [Terminal(i, self._gr) for i in self._gr.terminals]
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
                    tmp.append(Terminal(i, self._gr))
                elif t == i:
                    return Terminal(i, self._gr)
            if not handled and is_single is not True:
                tmp.append(None)
            elif not handled:
                return None
        return tmp

    def term(self, term=None):
        return self.get_term(term)

    def terms(self):
        return self.get_term(None)

    def terms_count(self):
        return len(self._gr.terminals)

    def terms_clear(self):
        return self.remove_term(None)

    # Nonterm part
    def add_nonterm(self, nonterm):
        return list(self._add_nonterm(nonterm))

    def _add_nonterm(self, nonterm):
        if nonterm is None:
            nonterm = []
        if not isinstance(nonterm, Iterable):
            nonterm = [nonterm]
        for t in nonterm:
            if t not in self._gr.nonterminals:
                self._gr.nonterminals.add(t)
                yield t

    def remove_nonterm(self, nonterm=None):
        """
        Delete terminal or terminals from grammar
        :param nonterm: Object or sequence of objects representing terminals
        :return: List of terminals removed from the grammar as sequence of Terminal instances
        """
        if nonterm is None:
            nonterm = self._gr.nonterminals
        if not isinstance(nonterm, Iterable):
            nonterm = [nonterm]
        tmp = []
        for t in list(nonterm):
            if t in self._gr.nonterminals:
                tmp.append(t)
                self._gr.nonterminals.remove(t)
        return tmp

    def have_nonterm(self, nonterm):
        """
        Check if terminal or terminals are in the grammar
        :param nonterm: Object or sequence of objects representing terminals
        :return: True if all objects in the parameter are in the grammar, false otherwise
        """
        if nonterm is None:
            nonterm = []
        if not isinstance(nonterm, Iterable):
            nonterm = [nonterm]
        contains = True
        for t in nonterm:
            contains = t in self._gr.nonterminals and contains
        return contains

    def get_nonterm(self, nonterm=None):
        """
        Get terminals stored in grammar that match terminal or terminals passed as parameter
        :param nonterm: Object or sequence of objects representing terminals
        :return: List of terminals in the grammar as sequence of Terminal object
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
        return self.get_nonterm(nonterm)

    def nonterms(self):
        return self.get_nonterm(None)

    def nonterms_count(self):
        return len(self._gr.nonterminals)

    def nonterms_clear(self):
        return self.remove_nonterm(None)

    # Rules part
    def add_rule(self, rules):
        if rules is None:
            rules = []
        if not isinstance(rules, Iterable):
            rules = [rules]
        return list(self._gr.rules.add(*rules))

    def remove_rule(self, rules=None, *, _validate=True):
        if rules is None:
            rules = self._gr.rules
        if not isinstance(rules, Iterable):
            rules = [rules]
        tmp = []
        for t in list(rules):
            if t in self._gr.rules:
                tmp.append(t)
                self._gr.rules.remove(t)
        return tmp

    def have_rule(self, rules):
        """
        Check if rule or sequence of rules are in the grammar
        :param rules: Object or sequence of objects representing rules
        :return: True if all rules in parameter are in the grammar, false otherwise
        """
        if rules is None:
            rules = []
        if not isinstance(rules, Iterable):
            rules = [rules]
        contains = True
        for t in rules:
            contains = t in self._gr.rules and contains
        return contains

    def get_rule(self, rules=None):
        # type: (Optional[Iterable[Type[Rule]]]) -> Union[Type[Rule], List[Type[Rule]]]
        """
        Get rule or sequence of rules stored in the grammar
        :param rules: Object or sequence of objects representing rules
        :return: Sequence of rules that are stored in the grammar
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
        return self.get_rule(rules)

    def rules(self):
        return self.get_rule()

    def rules_count(self):
        return len(self._gr.rules)

    def rules_clear(self):
        return self.remove_rule(None)

    # StartSymbol
    def start_get(self):
        return self._gr.start

    def start_set(self, nonterminal):
        self._gr.start = nonterminal

    def start_isSet(self):
        return self._gr.start is not None

    def start_is(self, nonterminal):
        return self._gr.start is nonterminal

    # Copy
    def __copy__(self):
        return self.copy()

    def copy(self, terminals=False, nonterminals=False, rules=False):
        newGr = self._gr.copy(terminals, nonterminals, rules)
        i = Grammar()
        i._gr = newGr
        return i

    def __deepcopy__(self, memodict={}):
        return self.copy(True, True, True)
