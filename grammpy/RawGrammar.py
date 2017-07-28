#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .Terminal import Terminal
from . import Nonterminal
from .HashContainer import HashContainer
from .exceptions import NotNonterminalException

class RawGrammar:
    def __init__(self, terminals=None, nonterminals=None, rules=None):
        terminals = [] if terminals is None else terminals
        nonterminals = [] if nonterminals is None else nonterminals
        rules = [] if rules is None else rules
        # TODO fill and add tests
        self.__terminals = HashContainer(terminals)
        self.__nonterminals = HashContainer(nonterminals)

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
    @staticmethod
    def __controll_nonterms(nonterms):
        nonterms = HashContainer.to_iterable(nonterms)
        for nonterm in nonterms:
            if not issubclass(nonterm, Nonterminal):
                raise NotNonterminalException(nonterm)
        return nonterms

    def add_nonterm(self, nonterms):
        nonterms = RawGrammar.__controll_nonterms(nonterms)
        return self.__nonterminals.add(nonterms)

    def remove_nonterm(self, nonterms=None):
        if nonterms is None:
            return self.__nonterminals.remove()
        nonterms = RawGrammar.__controll_nonterms(nonterms)
        return self.__nonterminals.remove(nonterms)

    def have_nonterm(self, nonterms):
        nonterms = RawGrammar.__controll_nonterms(nonterms)
        return self.__nonterminals.have(nonterms)

    def get_nonterm(self, nonterms = None):
        if nonterms is None:
            return self.__nonterminals.get()
        nonterms = RawGrammar.__controll_nonterms(nonterms)
        return self.__nonterminals.get(nonterms)

    def nonterm(self, nonterms = None):
        return self.get_nonterm(nonterms)

    def nonterms(self):
        for nonterm in self.__nonterminals.get():
            yield nonterm

    def nonterms_count(self):
        return self.__nonterminals.count()

    pass
