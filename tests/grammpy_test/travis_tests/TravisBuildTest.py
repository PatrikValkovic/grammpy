#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 17:13
:Licence MIT
Part of grammpy

"""

import unittest as ut


class TravisBuildTest(ut.TestCase):
    def test_success(self):
        self.assertEqual(1, 1, "1 is not equal to 1?!")


if __name__ == '__main__':
    ut.main()
