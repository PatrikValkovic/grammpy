#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 17:06
:Licence GNUv3
Part of grammpy

"""

import unittest as ut
from grammpy import factory

class RawStringRegularTest(ut.TestCase):
    def test_one_rule(self):
        factory.create('A => a b')

    def test_more_rules(self):
        factory.create('A => a B; B => b c')

    def test_one_rule_missing_one_rule(self):
        factory.create('A => a B')

    def test_one_rule_spaces(self):
        factory.create('  A      =>    a     b  ')

    def test_more_rules_spaces(self):
        factory.create('    A    =>   a   B;B=>b c')

