import unittest

class Test(unittest.TestCase):
    def setUp(self):
        num = input("输入：")
        self.num = int(num)

    def test_a(self):
        self.assertEqual(self.num,10,msg="输入错误！")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()