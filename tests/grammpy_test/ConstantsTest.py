#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 22.12.2024 15:44
:Licence MIT
Part of grammpy

"""
import tempfile
import pickle
from unittest import TestCase, main

from grammpy import EPSILON, END_OF_INPUT


class ConstantsTest(TestCase):
    def test_serializeEpsilon(self):
        s = { EPSILON }
        loaded = self.serialize_and_deserialize(s)
        self.assertIn(EPSILON, loaded)

    def test_serializeEndOfInput(self):
        s = { END_OF_INPUT }
        loaded = self.serialize_and_deserialize(s)
        self.assertIn(END_OF_INPUT, loaded)

    @staticmethod
    def serialize_and_deserialize(value):
        with tempfile.NamedTemporaryFile("wb", delete_on_close=False) as f:
            pickle.dump(value, f)
            f.close()
            with open(f.name, "rb") as f:
                loaded = pickle.load(f)
        return loaded

    def test_epsilonString(self):
        self.assertEqual(str(EPSILON),  "EPSILON")

    def test_endOfInputString(self):
        self.assertEqual(str(END_OF_INPUT), "END_OF_INPUT")

    def test_epsilonRepresentation(self):
        self.assertEqual(repr(EPSILON), "EPSILON")

    def test_endOfInputRepresentation(self):
        self.assertEqual(repr(END_OF_INPUT), "END_OF_INPUT")

if __name__ == '__main__':
    main()