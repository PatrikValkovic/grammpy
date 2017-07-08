#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
import collections

from .Terminal import Terminal


class Grammar:
    def __init__(self, terminals=None, nonterminals=None, rules=None):
        # Ensure that parameters are immutable
        if rules is None:
            rules = []
        if nonterminals is None:
            nonterminals = []
        if terminals is None:
            terminals = []
        # TODO fill and add tests
        self.__terminals = {}
        self.__nonterminals = {}

    # Helpers
    def __to_iterable(self, param):
        # standardize it to iterable object
        if isinstance(param, str) or not isinstance(param, collections.Iterable):
            return (param,)
        return param

    # Term part
    def add_term(self, term):
        term = self.__to_iterable(term)
        # iterace throught items
        for t in term:
            self.__terminals[hash(t)] = t

    def remove_term(self, term=None):
        if term is None:
            return self.__terminals.clear()
        term = self.__to_iterable(term)
        # iterate throught items
        for t in term:
            del self.__terminals[hash(t)]

    def have_term(self, term):
        term = self.__to_iterable(term)
        for t in term:
            if hash(t) not in self.__terminals:
                return False
        return True

    def get_term(self, term=None):
        # if no parameter is passed than return all terminals
        if term is None:
            # Maybe lazy evaluation, but it cannot be combined with return
            return [Terminal(item, self) for _, item in self.__terminals.items()]
        # else return relevant to parameter
        transformed = self.__to_iterable(term)
        ret = []
        for t in transformed:
            ret.append(Terminal(t, self) if hash(t) in self.__terminals else None)
        if isinstance(term, str) or not isinstance(term, collections.Iterable):
            return ret[0]
        return ret

    def term(self, term=None):
        return self.get_term(term)

    def terms(self):
        for _, item in self.__terminals.items():
            yield Terminal(item, self)

    def terms_count(self):
        return len(self.__terminals)

    # Non term part
    def add_nonterm(self, nonterm):
        raise NotImplementedError()

    def remove_nonterm(self, nonterm=None):
        raise NotImplementedError()

    def have_nonterm(self, nonterm):
        raise NotImplementedError()

    def get_nonterm(self, nonterm):
        raise NotImplementedError()

    def nonterms(self):
        raise NotImplementedError()

    def nonterms_count(self):
        raise NotImplementedError()

    pass
