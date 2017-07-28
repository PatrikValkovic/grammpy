#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
import collections

from .Terminal import Terminal
from .HashContainer import HashContainer


class RawGrammar:
    def __init__(self, terminals=[], nonterminals=None, rules=None):
        # Ensure that parameters are immutable
        if rules is None:
            rules = []
        if nonterminals is None:
            nonterminals = []
        # TODO fill and add tests
        self.__terminals = HashContainer(terminals)
        self.__nonterminals = {}

    # Term part
    def add_term(self, term):
        return self.__terminals.add(term)

    def remove_term(self, term=None):
        return self.__terminals.remove(term)

    def have_term(self, term):
        return self.__terminals.have(term)

    def get_term(self, term=None):
        if term is not None and not HashContainer.is_iterable(term):
            item = self.__terminals.get(term)
            return Terminal(item, self) if item is not None else None
        vals = []
        for t in self.__terminals.get(term):
            vals.append(Terminal(t,self) if t is not None else None)
        return vals

    def term(self, term=None):
        return self.get_term(term)

    def terms(self):
        for item in self.__terminals.all():
            yield Terminal(item, self)

    def terms_count(self):
        return self.__terminals.count()

    # Non term part
    def add_nonterm(self, nonterm):
        raise NotImplementedError()

    def remove_nonterm(self, nonterm=None):
        raise NotImplementedError()

    def have_nonterm(self, nonterm):
        raise NotImplementedError()

    def get_nonterm(self, nonterm = None):
        raise NotImplementedError()

    def nonterm(self, nonterm):
        raise NotImplementedError()

    def nonterms(self):
        raise NotImplementedError()

    def nonterms_count(self):
        raise NotImplementedError()

    pass
