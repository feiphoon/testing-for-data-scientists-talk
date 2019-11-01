"""
Run this file exactly the same way as the last:

    py.test

OR

    pytest

OR run just this file.

You can inspect the sequence in which your fixtures are set up by running:

    pytest -v --setup-show tests/test_dictionary_functions.py

"""

import sys
sys.path.append("..")

import dictionary_functions as df

import pytest
from pytest import raises

# Fixtures are super nice for testing the 
# structures you expect your functions to process.
# The @pytest.fixture() decorator flags the immediately
# following function as a fixture.
# Prefixing this fixture function name with "fixture_",
# is only my personal choice, but good naming makes your 
# code easier to read.
#
# The second remarkable thing here is being able 
# to define fixture scope.
# There are 4 options for the scope parameter.
# In increasing order of specificity:
# session, module, class, function.
#
# If you have a very large code base to test, 
# and lots of tests with lots of fixtures,
# you don't want to load fixtures if they're not needed,
# because this can slow down the tests.
#
# At this tiny scale though, explicit scoping is just 
# a tidy practice that helps you keep track of how
# useful your fixture is. And that helps with refactoring!
@pytest.fixture()
def fixture_catalogue_1(scope="class"):
    CATALOGUE_1 = {
        "Book name 1": {
            "author": "Author 1",
            "pages": 0
        },
        "Book name 2": {
            "author": "Author 2",
            "pages": 10
        },
    }
    return CATALOGUE_1


# This decorator is a request to use a certain fixture.
# If you want to make more fixtures available to a Test class or function, 
# just pass more fixtures like this, comma-separated:
# @pytest.mark.usefixtures("fixture_catalogue_1", "fixture_catalogue_2")
@pytest.mark.usefixtures("fixture_catalogue_1")
class TestGetBookAuthor:
    @pytest.mark.parametrize("input1, expected_result", 
        [
            ("Book name 1", "Author 1"),
            ("Book name 2", "Author 2"),
        ])
    def test_get_book_author(self, fixture_catalogue_1, input1, expected_result):
        result = df.get_book_author(fixture_catalogue_1, input1)

        assert result == expected_result

    def test_get_book_author_key_error(self, fixture_catalogue_1):
        with raises(KeyError): 
            df.get_book_author(fixture_catalogue_1, "Book name 3") # a book name that doesn't exist


@pytest.mark.usefixtures("fixture_catalogue_1")
class TestGetBookPages:
    pass