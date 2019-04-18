from unittest import TestCase

from simsim import parse


TEST_CODE_BASIC = """
a = 1
"""

TEST_CODE_FUNC = """
n = 'test'

def func_one(x):
    return x*2
"""

TEST_CODE_CLASS = """
class Foo(object):
    def bar(self):
        return True
"""

TEST_CODE_MODULE_DOCSTRING = '""" module docstring """\nx = 10\n'

TEST_CODE_FUNC_DOCSTRING = \
    'def foo(bar):\n' \
    '    """ func docstring """\n' \
    '    return bar\n'

TEST_CODE_CLASS_DOCSTRING = \
    'class Foo(object):\n' \
    '    """ class docstring """\n' \
    '    def bar(self):\n' \
    '        pass\n'


class TestParser(TestCase):
    def test_basic(self):
        expected = {
            '__main__': ['Assign', 'Name', 'Store', 'Num']
        }
        self.assertDictEqual(parse(TEST_CODE_BASIC).scope_nodes, expected)

    def test_func(self):
        expected = {
            '__main__': ['Assign', 'Name', 'Store', 'Str', 'FunctionDef'],
            '__main__.func_one': ['FunctionDef', 'arguments', 'arg',
                                  'Return', 'BinOp', 'Name',
                                  'Load', 'Mult', 'Num'],
        }
        self.assertDictEqual(parse(TEST_CODE_FUNC).scope_nodes, expected)

    def test_class(self):
        expected = {
            '__main__': ['ClassDef'],
            '__main__.Foo': ['ClassDef', 'Name', 'Load', 'FunctionDef'],
            '__main__.Foo.bar': ['FunctionDef', 'arguments', 'arg',
                                 'Return', 'NameConstant'],
        }
        self.assertDictEqual(parse(TEST_CODE_CLASS).scope_nodes, expected)

    def test_docstring(self):
        nodes = parse(TEST_CODE_MODULE_DOCSTRING).scope_nodes
        expected = {
            '__main__': ['Assign', 'Name', 'Store', 'Num']
        }
        self.assertDictEqual(nodes, expected)

        nodes = parse(TEST_CODE_FUNC_DOCSTRING).scope_nodes
        expected = {
            '__main__': ['FunctionDef'],
            '__main__.foo': ['FunctionDef', 'arguments', 'arg',
                             'Return', 'Name', 'Load']
        }
        self.assertDictEqual(nodes, expected)

        nodes = parse(TEST_CODE_CLASS_DOCSTRING).scope_nodes
        expected = {
            '__main__': ['ClassDef'],
            '__main__.Foo': ['ClassDef', 'Name', 'Load', 'FunctionDef'],
            '__main__.Foo.bar': ['FunctionDef', 'arguments', 'arg', 'Pass'],
        }
        self.assertDictEqual(nodes, expected)
