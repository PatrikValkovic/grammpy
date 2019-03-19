#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 19.03.2019 12:21
:Licence MIT
Part of grammpy

"""
from string import ascii_lowercase
from grammpy import *
from grammpy.transforms import ContextFree, InverseContextFree, InverseCommon
from grammpy.parsers import cyk


class BaseNonterminal(Nonterminal):
    @property
    def get(self):
        return self.to_rule.get()


class Symb(BaseNonterminal): pass
class Concat(BaseNonterminal): pass
class Iterate(BaseNonterminal): pass
class Or(BaseNonterminal): pass


class SymbRule(Rule):
    rules = [([Symb], [ch]) for ch in ascii_lowercase]
    def get(self):
        yield self.to_symbols[0].s


class Bracket(Rule):
    rule = ([Symb], ['(', Or, ')'])
    def get(self):
        return self.to_symbols[1].get


class IterateRewrite(Rule):
    rule = ([Iterate], [Symb])
    def get(self):
        return self.to_symbols[0].get


class IterateRule(Rule):
    MAX_ITERATIONS = 6
    FILL_SYMBOL = ''
    rule = ([Iterate], [Symb, '*'])
    def get(self):
        values = self.to_symbols[0].get
        for v in values:
            for i in range(IterateRule.MAX_ITERATIONS):
                yield v * i
            last_iter = str(v * int(IterateRule.MAX_ITERATIONS / 2))
            yield last_iter + IterateRule.FILL_SYMBOL + last_iter


class ConcatRewrite(Rule):
    rule = ([Concat], [Iterate])
    def get(self):
        return self.to_symbols[0].get


class ConcatRule(Rule):
    rule = ([Concat], [Iterate, Concat])
    def get(self):
        for l in self.to_symbols[0].get:
            for r in self.to_symbols[1].get:
                yield l + r


class OrRewrite(Rule):
    rule = ([Or], [Concat])
    def get(self):
        return self.to_symbols[0].get

class OrRule(Rule):
    rule = ([Or], [Or, '+', Or])
    def get(self):
        yield from self.to_symbols[0].get
        yield from self.to_symbols[2].get


g = Grammar(terminals=list(ascii_lowercase + '()*+'),
            nonterminals=[Symb, Concat, Or, Iterate],
            rules=[SymbRule, Bracket, ConcatRewrite, ConcatRule, OrRewrite, OrRule, IterateRewrite, IterateRule],
            start_symbol=Or)


if __name__ == '__main__':
    gr = ContextFree.prepare_for_cyk(g)

    while True:
        read = input("Type regex or exit to quit: ").strip()
        if read == "exit":
            break
        if len(read) == 0:
            continue

        root = cyk(gr, read)
        root = InverseContextFree.reverse_cyk_transforms(root)
        root = InverseCommon.splitted_rules(root)
        for form in root.get:
            print(form)

    print("Quiting the application")
