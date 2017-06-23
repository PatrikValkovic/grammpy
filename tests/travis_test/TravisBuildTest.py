import unittest as ut


class TravisBuildTest(ut.TestCase):
    def success_test(self):
        self.assertEqual(1, 1, "1 is not equal to 1?!")

    def failed_test(self):
        self.assertEqual(1, 2, "1 is not equal to 2")


def main():
    ut.main()


if __name__ == '__main__':
    main()
