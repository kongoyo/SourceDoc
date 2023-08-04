import unittest


# Functions to be tested
def add(x, y):
    return x + y

x = 1
y = 3
print(add(x, y))

class AddTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (100, 99)

    def tearDown(self):
        self.args = None

    def test_add(self):
        expected = 199;
        result = add(*self.args);
        self.assertEqual(expected, result);
        
suite = unittest.TestSuite()
suite.addTest(AddTestCase('test_add'))

unittest.TextTestRunner(verbosity=2).run(suite)