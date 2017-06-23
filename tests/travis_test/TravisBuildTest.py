import unittest as ut


class TravisBuildTest(ut.TestCase):
    def test_success(self):
        self.assertEqual(1, 1, "1 is not equal to 1?!")

    def test_failing(self):
        self.assertEqual(1, 2, "1 is not equal to 2")


def main():
    ut.main()


if __name__ == '__main__':
    main()
