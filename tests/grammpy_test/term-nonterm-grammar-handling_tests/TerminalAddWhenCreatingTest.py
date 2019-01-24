#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 12:28
:Licence GNUv3
Part of grammpy

"""
from unittest import TestCase, main
from grammpy.old_api import Grammar


class TerminalAddWhenCreatingTest(TestCase):
    def test_addOneInArray(self):
        gr = Grammar(terminals=['A'])
        self.assertTrue(gr.have_term('A'))

    def test_addTwoInArray(self):
        gr = Grammar(terminals=['A', 0])
        self.assertTrue(gr.have_term('A'))
        self.assertTrue(gr.have_term(0))
        self.assertTrue(gr.have_term([0, 'A']))

    def test_addOneSeparate(self):
        gr = Grammar(terminals='A')
        self.assertTrue(gr.have_term('A'))

    def test_addThreeInString(self):
        gr = Grammar(terminals='ABC')
        self.assertTrue(gr.have_term('A'))
        self.assertTrue(gr.have_term('B'))
        self.assertTrue(gr.have_term('C'))
        self.assertTrue(gr.have_term(('A','B','C')))
        self.assertFalse(gr.have_term('D'))

    def test_addThreeInTuple(self):
        gr = Grammar(terminals=('A', 'B', 'C'))
        self.assertTrue(gr.have_term('A'))
        self.assertTrue(gr.have_term('B'))
        self.assertTrue(gr.have_term('C'))
        self.assertTrue(gr.have_term(['A', 'B', 'C']))
        self.assertFalse(gr.have_term('D'))

    def test_addThreeOneDelete(self):
        gr = Grammar(terminals=('A', 'B', 'C'))
        self.assertTrue(gr.have_term('A'))
        self.assertTrue(gr.have_term('B'))
        self.assertTrue(gr.have_term('C'))
        self.assertTrue(gr.have_term(['A', 'B', 'C']))
        self.assertFalse(gr.have_term('D'))
        gr.remove_term('B')
        self.assertTrue(gr.have_term('A'))
        self.assertFalse(gr.have_term('B'))
        self.assertTrue(gr.have_term('C'))
        self.assertTrue(gr.have_term(['A', 'C']))
        self.assertFalse(gr.have_term('D'))


if __name__ == '__main__':
    main()