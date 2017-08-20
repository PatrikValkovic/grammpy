#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 16.08.2017 19:25
:Licence GNUv3
Part of grammpy

"""
from copy import deepcopy
from inspect import isclass
from .RulesRemovingGrammar import RulesRemovingGrammar as _G
from ..Nonterminal import Nonterminal
from ..Rules import Rule
from ..Constants import EPSILON


class Grammar(_G):
    def __copy__(self):
        return Grammar(terminals=(t.s for t in self.terms()),
                       nonterminals=self.nonterms(),
                       rules=self.rules(),
                       start_symbol=self.start_get())


    def __deepcopy__(self, memodict={}):
        # Copy terminals
        new_terms = set()
        new_terms_dict = dict()
        for t in [t.s for t in self.terms()]:
            created = deepcopy(t)
            new_terms.add(created)
            new_terms_dict[t] = created
        # Copy nonterminals
        new_nonterms = set()
        new_nonterms_dict = dict()
        for n in self.nonterms():
            created = type("Copy" + n.__name__, (Nonterminal,), dict(n.__dict__))
            new_nonterms.add(created)
            new_nonterms_dict[n] = created
        # Copy rules
        new_rules = set()
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
                        leftPart.append(new_nonterms_dict[symbol])
                    else:
                        leftPart.append(new_terms_dict[symbol])
                # Copy right side
                for symbol in rule[1]:
                    if symbol is EPSILON:
                        rightPart.append(EPSILON)
                    elif isclass(symbol) and issubclass(symbol, Nonterminal):
                        rightPart.append(new_nonterms_dict[symbol])
                    else:
                        rightPart.append(new_terms_dict[symbol])
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
        # Solve start symbol
        start_symbol = None if not self.start_isSet() else new_nonterms_dict[self.start_get()]
        # Create copy of grammar
        return Grammar(terminals=list(new_terms),
                       nonterminals=list(new_nonterms),
                       rules=list(new_rules),
                       start_symbol=start_symbol)
