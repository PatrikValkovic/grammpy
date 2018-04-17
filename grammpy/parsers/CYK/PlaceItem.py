#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 21:56
:Licence GNUv3
Part of pyparsers

"""


class PlaceItem:
    def __init__(self, r, t1, t2):
        self.to_rule = [t1, t2]
        self.rule = r

    def __hash__(self):
        return hash(self.rule)

    @property
    def fromSymbol(self):
        return self.rule.fromSymbol
