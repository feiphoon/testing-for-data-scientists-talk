"""
You can auto-discover and run all tests with this command (meaning it will 
find all filenames starting and ending with `test_` in that folder 
and subfolders under that folder):

    py.test

OR
    pytest

OR run just this file.

    pytest tests/test_math_functions.py

Documentation: https://docs.pytest.org/en/latest/
"""

# This is here to set paths in this file, 
# so these tests can find the math_functions.py file we want to test.
import sys
sys.path.append("..")

import math_functions as mf

import pytest
from pytest import raises # You'll need this to test raises.


# Basic testing and a direct translation from what we wrote in doctest
# def test_addition():
#     assert mf.addition(1, 2) == 3


# The Given-When-Then pattern
# def test_addition():
#     # Given
#     expected_result = 3
#     # When
#     result = mf.addition(1, 2)
#     # Then
#     assert result == expected_result


# Introducing parametrization, which handles multiple test cases
# The way pytest handles parametrization is much more readable than in unittest.
# The Given-When-Then pattern makes it really easy to plug these test cases in.
#
# @pytest.mark.parametrize("input1, input2, expected_result", 
#     [
#         (1, 2, 3),
#         (0, 0, 0),
#         (-2, 2, 0),
#         (2, -2, 0),
#         (-2, -2, -4)
#     ])
# def test_addition(input1, input2, expected_result):
#     # When
#     result = mf.addition(input1, input2)

#     # Then
#     assert result == expected_result


# Here is the pattern to test errors/exceptions in pytest.
# The function mf.division(0,0) that you want to test, is inside a
# raises Context Manager (the "with").
#
# For comparison, unittest has the same structure but with a different function:
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
#
# def test_division_zero_division_error(self):
#     with raises(ZeroDivisionError): # You can test Exceptions, too.
#         mf.division(0, 0)


# def test_division_type_error(self):
#     with raises(TypeError):
#         mf.division("a", 1)


# You can also test custom Exceptions.
# You can either just test that the exception occurred:
# with raises(BananaException):
#     mf.a_function_that_asks_for_bananas(True)
# OR specify the message in your test, as below - it's optional.
#
# from math_functions import BananaException
# def test_a_function_that_asks_for_bananas():
#     with raises(BananaException, match="ABSOLUTELY NOT!"):
#         mf.a_function_that_asks_for_bananas(True)


# We can group tests which are testing the same function, using a Test class.
# You will need to add a new first argument of your test functions, `self`,
# to all the test functions under this Test class, e.g. def test_thing(self).
# Below, we have also parametrized our errors/exceptions test cases.
#
# You can run this group of tests at the command line with:
# pytest tests/test_math_functions.py::TestDivision
# or just one function:
# pytest tests/test_math_functions.py::TestDivision::test_division_error
#
# class TestDivision:
#     @pytest.mark.parametrize("input1, input2, expected_result", 
#         [
#             (1, 1, 1),
#             (4, 2, 2),
#             (0, 1, 0),
#             (-6, 3, -2),
#             (6, -3, -2)
#         ])
#     def test_division(self, input1, input2, expected_result):
#         # When
#         result = mf.division(input1, input2)

#         # Then
#         assert result == expected_result

#     @pytest.mark.parametrize("input1, input2, expected_result", 
#         [
#             (0, 0, ZeroDivisionError),
#             ("a", 1, TypeError)
#         ])
#     def test_division_error(self, input1, input2, expected_result):
#         with raises(expected_result):
#             mf.division(input1, input2)