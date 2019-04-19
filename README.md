# simsim

[![Build Status](https://travis-ci.org/kidig/simsim.svg?branch=master)](https://travis-ci.org/kidig/simsim) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/simsim.svg) ![PyPI](https://img.shields.io/pypi/v/simsim.svg)

SIMple SIMilarity is a tool by which you can check the similarity of two sources written in Python. 
The tool is created for checking small pieces of source code that students submit as solutions for the task. 
It's a way to catch plagiarism. ;-)


## Installing

Install and update using pip:

  ```
  pip install simsim
  ```

It has no dependencies and supports Python 3.4 and newer.

## Example

1. You can use it as a python library. Here is an example:

```python
import simsim

CODE_A = """
a = 3

def foo(bar):
   return bar
"""

CODE_B = """
b = 3

def foo2(bar):
   return bar
"""

result = simsim.compare(CODE_A, CODE_B)
print('Ratio:', result['ratio'])
# prints Ratio: 1.0
```

2. Or from command line:

```
$ simsim examples/tiny1.py examples/tiny2.py
Similarity: 1.00

examples/tiny1.py:__main__
--------------------------
examples/tiny2.py:__main__: 0.99
examples/tiny2.py:__main__.Point.__init__: 0.23
examples/tiny2.py:__main__.Point: 0.23
examples/tiny2.py:__main__.Point.export: 0.17
examples/tiny2.py:__main__.foo: 0.13

examples/tiny1.py:__main__.Point
--------------------------------
examples/tiny2.py:__main__.Point: 1.00
examples/tiny2.py:__main__.Point.__init__: 0.38
examples/tiny2.py:__main__.foo: 0.25
examples/tiny2.py:__main__: 0.23
examples/tiny2.py:__main__.Point.export: 0.22

examples/tiny1.py:__main__.Point.__init__
-----------------------------------------
examples/tiny2.py:__main__.Point.__init__: 1.00
examples/tiny2.py:__main__.Point.export: 0.67
examples/tiny2.py:__main__.foo: 0.53
examples/tiny2.py:__main__.Point: 0.38
examples/tiny2.py:__main__: 0.23

examples/tiny1.py:__main__.Point.export
---------------------------------------
examples/tiny2.py:__main__.Point.export: 1.00
examples/tiny2.py:__main__.Point.__init__: 0.67
examples/tiny2.py:__main__.foo: 0.64
examples/tiny2.py:__main__.Point: 0.22
examples/tiny2.py:__main__: 0.17

examples/tiny1.py:__main__.foo
------------------------------
examples/tiny2.py:__main__.foo: 1.00
examples/tiny2.py:__main__.Point.export: 0.64
examples/tiny2.py:__main__.Point.__init__: 0.53
examples/tiny2.py:__main__.Point: 0.25
examples/tiny2.py:__main__: 0.13
```
(it shows similarity between different scopes in the files)
