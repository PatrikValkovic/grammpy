#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 12:34
:Licence GNUv3
Part of grammpy

"""

from grammpy import Grammar as _G, Nonterminal as _N


class TFirst:
    pass


class TSecond:
    pass


class TThird:
    pass


TInstFirst = object()
TInstSecond = object()
TInstThird = object()


class NFirst(_N):
    pass


class NSecond(_N):
    pass


class NThird(_N):
    pass


class NFourth(_N):
    pass


class NFifth(_N):
    pass


grammar = _G(terminals=[0, 1, 2,
                        'a', 'b', 'c',
                        TFirst, TSecond, TThird,
                        TInstFirst, TInstSecond, TInstThird],
             nonterminals=[NFirst, NSecond, NThird, NFourth, NFifth])
