import unittest

def setUpModule():
    print("test_start_module...")

def tearDownModule():
    print("test_end_module...")

class Test(object):

    @classmethod
    def setUpclass(self):
        print("test_start_class...")

    @classmethod
    def tearDownclass(self):
        print("test_end_class")

    def setUp(self):
        print("test_start_up")

    def tearDown(self):
        print("test_end_down")
    
    def test_a(self):
        print("test_a_...")

    def test_b(self):
        print("test_b_...")

if __name__ == '__main__':
    unittest.main()