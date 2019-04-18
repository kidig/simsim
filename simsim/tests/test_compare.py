from unittest import TestCase
from simsim.cmd import compare


TEST_FUNC_A = """
def func_one(x):
    return x*2
"""

TEST_FUNC_B = """
def func_two(x):
    return x*2
"""


TEST_FUNC_REORDER_A = """
def func_one(x):
    return x*3

def func_two(x, y):
    return bool(x) and bool(y)
"""


TEST_FUNC_REORDER_B = """
def func_two(x, y):
    return bool(x) and bool(y)

def func_one(x):
    return x*3
"""

TEST_CODE_3_A = """
a = 1
b = 3

print(a + b)
"""

TEST_CODE_3_B = """
a = 1 + 0
b = 3

print(a + b)
"""


class TestCompare(TestCase):
    @classmethod
    def assert_compare(cls, a, b, ratio):
        assert compare(a, b)['ratio'] == ratio

    def test_vars(self):
        self.assert_compare('a = 1', 'b = 1', 1)

    def test_funcs(self):
        self.assert_compare(TEST_FUNC_A, TEST_FUNC_B, 1)
        self.assert_compare(TEST_FUNC_REORDER_A, TEST_FUNC_REORDER_B, 1)

    def test_less_one(self):
        assert compare(TEST_CODE_3_A, TEST_CODE_3_B)['ratio'] < 1
