#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 24.01.2019 13:04
:Licence GPLv3
Part of grammpy

"""
from collections import Iterable

from .. import Grammar as NewGrammar, Terminal


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
        return self._get_term(term)

    def _get_term(self, term=None):
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

    # Non term part
    def add_nonterm(self, nonterms):
        """
        Add nonterminal or nonterminals into grammar
        :param nonterms: Nonterminal or sequence of Nonterminal classes representing nonterminals
        :return: Sequence of nonterminals added into grammar
        """
        return self._gr.add_nonterm(nonterms)

    def remove_nonterm(self, nonterms=None):
        """
        Remove nonterminal or nonterminals from the grammar
        :param nonterms: Nonterminal or sequence of Nonterminal classes representing nonterminals
        :return: Sequence of nonterminals removed from the grammar
        """
        return self._gr.remove_nonterm(nonterms)

    def have_nonterm(self, nonterms):
        """
        Check if nonterminal or nonterminals are in the grammar
        :param nonterms: Rule or sequence of Rule classes representing nonterminals
        :return: True if all nonterminals in parameter are in the grammar, false otherwise
        """
        return self._gr.have_nonterm(nonterms)

    def get_nonterm(self, nonterms=None):
        """
        Get nonterminals from the grammar
        :param nonterms: Nonterminal or sequence of Nonterminal classes representing nonterminals
        :return: Sequence of nonterminals in the grammar
        """
        return self._gr.get_nonterm(nonterms)

    def nonterm(self, nonterms=None):
        return self._gr.nonterm(nonterms)

    def nonterms(self):
        return self._gr.nonterms()

    def nonterms_count(self):
        return self._gr.nonterms_count()

    def nonterms_clear(self):
        return self._gr.nonterms_clear()

    # Rules part
    def add_rule(self, rules):
        """
        Add rule or sequence of rules into grammar
        :param rules: Object or sequence of objects representing rules
        :return: Sequence of rules added into grammar
        """
        return self._gr.add_rule(rules)

    def remove_rule(self, rules=None, *, _validate=True):
        """
        Remove rule or sequence of rules from the grammar
        :param rules: Object or sequence of objects representing rules
        :param _validate: Flag if validate removing rules, only for internal use
        :return: Sequence of rules removed from the grammar
        """
        return self._gr.remove_rule(rules, _validate=_validate)

    def have_rule(self, rules):
        """
        Check if rule or sequence of rules are in the grammar
        :param rules: Object or sequence of objects representing rules
        :return: True if all rules in parameter are in the grammar, false otherwise
        """
        return self._gr.have_rule(rules)

    def get_rule(self, rules=None):
        """
        Get rule or sequence of rules stored in the grammar
        :param rules: Object or sequence of objects representing rules
        :return: Sequence of rules that are stored in the grammar
        """
        return self._gr.get_rule(rules)

    def rule(self, rules=None):
        return self._gr.rule(rules)

    def rules(self):
        return self._gr.rules()

    def rules_count(self):
        return self._gr.rules_count()

    def rules_clear(self):
        return self._gr.rules_clear()

    # StartSymbol
    def start_get(self):
        return self._gr.start_get()

    def start_set(self, nonterminal):
        return self._gr.start_set(nonterminal)

    def start_isSet(self):
        return self._gr.start_isSet()

    def start_is(self, nonterminal):
        return self._gr.start_is(nonterminal)

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
