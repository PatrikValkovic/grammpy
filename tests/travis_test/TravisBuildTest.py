import unittest as ut


class TravisBuildTest(ut.TestCase):
    def test_success(self):
        self.assertEqual(1, 1, "1 is not equal to 1?!")