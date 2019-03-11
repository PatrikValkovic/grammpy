#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 23:39
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import Grammar
from grammpy.exceptions import NotRuleException


class GetTest(TestCase):
    def test_NotRule(self):
        gr = Grammar()
        with self.assertRaises(NotRuleException):
            gr.rules.get(4)


if __name__ == '__main__':
    main()
