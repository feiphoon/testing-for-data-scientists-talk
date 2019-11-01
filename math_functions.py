"""
You can run doctests on this file with this command:

    python -m doctest -v math_functions.py

You can also run pytest AND doctest on the same file with this command:
    
    pytest -v --doctest-modules "math_functions.py tests/test_math_functions.py"


Documentation: https://docs.python.org/3.7/library/doctest.html
"""
# A smooth-sailing doctest example
def addition(x, y):
    """Returns the value of x plus y.

    >>> addition(1, 2)
    3
    >>> addition(0, 0)
    0
    >>> addition(-2, 2)
    0
    """
    return x + y


# A not-so-nice doctest example
# def division(x, y):
#     """Returns the value of x divided by y.

#     >>> division(1, 1)
#     1.0
#     >>> division(4, 2)
#     2.0
#     >>> division(0, 1)
#     0.0
#     >>> division(0, 0)
#     Traceback (most recent call last):
#       File "/usr/local/Cellar/python/3.7.4_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/doctest.py", line 1329, in __run
#         compileflags, 1), test.globs)
#       File "<doctest math_functions.division[3]>", line 1, in <module>
#         division(0, 0)
#       File "/Users/fei.phoon/Dropbox/talks/testing-talk/math_functions.py", line 35, in division
#         return x/y
#     ZeroDivisionError: division by zero
#     >>> division(1, 0)
#     Traceback (most recent call last):
#     ...
#     ZeroDivisionError: division by zero
#     >>> division("a", 1)
#     Traceback (most recent call last):
#     ...
#     TypeError: unsupported operand type(s) for /: 'str' and 'int'
#     """
#     return x/y

# Here's a custom exception example
# class BananaException(Exception):
#     """Raises an exception when you ask for bananas."""

# def a_function_that_asks_for_bananas(true_or_false):
#     """Takes requests for bananas but gets mad if you actually want any.

#     >>> a_function_that_asks_for_bananas(False)
#     Good choice.
#     >>> a_function_that_asks_for_bananas(True)
#     Traceback (most recent call last):
#     ...
#     math_functions.BananaException: ABSOLUTELY NOT!
#     """
#     if true_or_false == False:
#         print("Good choice.")
#     else:
#         raise BananaException("ABSOLUTELY NOT!")