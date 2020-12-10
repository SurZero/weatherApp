
import unittest
def add(a, b):
    if type(a) == 'str'  or type(b) == 'str':
        raise TypeError
    return a  + b

class AddTestCase(unittest.TestCase):
    def test_add_returns_sum_of_two_numbers(self):
        # arrange
        # act ====> call add
        result = add(10, 20)
        self.assertEqual(30, result)

    def test_throws_errors_when_one_or_both_is_string(self):
        result = add("abc", "xyz")
        self.assertRaises(TypeError)

def multiply(a, b):
    return a * b

class MultiplyTestCase(unittest.TestCase):
    def test_muplity_function_returns_mulitplication_of_two_integer(self):
        result = multiply(10, 20)
        self.assertEqual(200, result)


def isAuthenticated():
    return True

class IsAuthenticationTestCase(unittest.TestCase):
    def test_current_user_is_authenticated(self):\
        self.assertTrue(isAuthenticated())




