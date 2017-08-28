#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.08.2017 20:29
:Licence GNUv3
Part of grammpy

"""

from copy import deepcopy
from inspect import isclass
from .RulesRemovingGrammar import RulesRemovingGrammar as Grammar
from ..Nonterminal import Nonterminal
from ..Rules import Rule
from ..Constants import EPSILON

# TODO Optimize

class CopyableGrammar(Grammar):
    class _CopyContainer:
        def __init__(self, new_terms, new_terms_dict,
                     new_nonterms, new_nonterms_dict,
                     new_rules, new_rules_dict,
                     start):
            self.start = start
            self.new_rules_dict = new_rules_dict
            self.new_nonterms = new_nonterms
            self.new_nonterms_dict = new_nonterms_dict
            self.new_rules = new_rules
            self.new_terms_dict = new_terms_dict
            self.new_terms = new_terms

    def _copy_terminals(self, _copy=False):
        new_terms = set()
        new_terms_dict = dict()
        # if not copy just fill into set and dict to self
        if not _copy:
            new_terms = set(t.s for t in self.terms())
            for t in new_terms: new_terms_dict[t] = t
        else:
            for t in [t.s for t in self.terms()]:
                created = deepcopy(t)
                new_terms.add(created)
                new_terms_dict[t] = created
        return (new_terms, new_terms_dict)

    def _copy_nonterminals(self, _copy=False):
        new_nonterms = set()
        new_nonterms_dict = dict()
        # if not copy just fill into set and dict to self
        if not _copy:
            new_nonterms = set(self.nonterms())
            for n in new_nonterms: new_nonterms_dict[n] = n
        else:
            for n in self.nonterms():
                created = type("Copy" + n.__name__, (Nonterminal,), dict(n.__dict__))
                new_nonterms.add(created)
                new_nonterms_dict[n] = created
        return (new_nonterms, new_nonterms_dict)

    def _copy_rules(self, terminals, nonterminals, _copy=False):
        new_rules = set()
        new_rules_dict = dict()
        # if not copy just fill into set and dict to self
        if not _copy:
            new_rules = set(self.rules())
            for r in new_rules: new_rules_dict[r] = r
        else:
            for r in self.rules():
                copy_rules = []
                for rule in r.rules:
                    leftPart = []
                    rightPart = []
                    # Copy left side
                    for symbol in rule[0]:
                        if symbol is EPSILON:
                            leftPart.append(EPSILON)
                        elif isclass(symbol) and issubclass(symbol, Nonterminal):
                            leftPart.append(nonterminals[symbol])
                        else:
                            leftPart.append(terminals[symbol])
                    # Copy right side
                    for symbol in rule[1]:
                        if symbol is EPSILON:
                            rightPart.append(EPSILON)
                        elif isclass(symbol) and issubclass(symbol, Nonterminal):
                            rightPart.append(nonterminals[symbol])
                        else:
                            rightPart.append(terminals[symbol])
                    # Merge sides
                    copy_rules.append((leftPart, rightPart))
                # Delete info about previous rules
                old_dict = r.__dict__.copy()  # type: dict
                if 'rules' in old_dict: del old_dict['rules']
                if 'rule' in old_dict: del old_dict['rule']
                if 'left' in old_dict: del old_dict['left']
                if 'right' in old_dict: del old_dict['right']
                if 'fromSymbol' in old_dict: del old_dict['fromSymbol']
                if 'toSymbol' in old_dict: del old_dict['toSymbol']
                # Create new rule
                created = type("Copy" + r.__name__, (Rule,), old_dict)
                created.rules = copy_rules
                new_rules.add(created)
                new_rules_dict[r] = created
        return (new_rules, new_rules_dict)

    def _copy(self, terminals=False, nonterminals=False, rules=False) -> _CopyContainer:
        # Copy terminals
        (new_terms, new_terms_dict) = self._copy_terminals(_copy=terminals)
        rules = terminals if rules is False else True

        # Copy nonterminals
        (new_nonterms, new_nonterms_dict) = self._copy_nonterminals(_copy=nonterminals)
        rules = nonterminals if rules is False else True

        # Copy rules
        (new_rules, new_rules_dict) = self._copy_rules(new_terms_dict, new_nonterms_dict, _copy=rules)

        # Solve start symbol
        start = self.start_get()
        if self.start_isSet() and nonterminals:
            start = new_nonterms_dict[self.start_get()]

        return CopyableGrammar._CopyContainer(new_terms, new_terms_dict,
                                              new_nonterms, new_nonterms_dict,
                                              new_rules, new_rules_dict,
                                              start)
