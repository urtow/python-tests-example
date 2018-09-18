import unittest


def setUpModule():
    print("Here we setup module")


def tearDownModule():
    print("Here we teardown module")


class TestCaseWithSetup(unittest.TestCase):

    @staticmethod
    def setUpClass():
        print("Here we setup TestCase")

    @staticmethod
    def tearDownClass():
        print("\nHere we teardown class")

    def setUp(self):
        print("Here we setup each test")

    def tearDown(self):
        print("\nHere we teardown each test")

    def test_one(self):
        print("test one")
        self.assertEqual(1,2)

    def test_two(self):
        print("test two")
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
