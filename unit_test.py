
from add_test import Count
import unittest

class TestCount(unittest.TestCase):
    def setUp(self):
        print("start_hello world !!")

    def test_add(self):
        res = Count(3,5)
        self.assertEqual(res.add(),8)

    def test_add2(self):
        res = Count(24,33)
        print("test_2")
        self.assertEqual(res.add(),57)

    def tearDown(self):
        print("end_hello world !!")

if __name__ == '__main__':
    # unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(TestCount("test_add2"))
    #
    # runner = unittest.TestRunner()
    # runner.run(suite)

    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add"))

    runner = unittest.TestRunner()
    runner.run(suite)