#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import Rule


class Single(Rule):
    rule = ([0], [1])


class TwoRight(Rule):
    rule = ([0], [1, 2])


class ThreeLeft(Rule):
    rule = ([0, 1, 'a'], [2])


class Multiple(Rule):
    rule = ([0, 1, 2], [3, 4])


class FromRuleComputeTest(TestCase):
    pass


if __name__ == '__main__':
    main()
