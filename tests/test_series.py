import pytest

from math_series.series import pre_test, fibonacci

# function to see if pytest is working
def test_function():
  assert pre_test() == None

# make a test
# call function to test
# provide the expected test result
# "assert" - make sure the test function and expected result match


# tests for fibonacci

def test_one():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_two():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_three():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_four():
  actual = fibonacci(6)
  expected = 8
  assert actual == expected


# tests for lucas numbers







