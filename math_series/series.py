# function to see if pytest is working
def pre_test():
  pass

print('testing terminal')
# The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two. This gives us:

# 0, 1, 1, 2, 3, 5, 8, 13, ...


# recursive solution

def fibonacci(n):
  '''
  Fibonacci numbers are the sum of it's two previous numbers. 
  First two terms are 0 and 1.
  Base numbers must be set to reflect those terms.
  n is the number.
  n - 1 refers to it's previous number. 
  n - 2 refers to it's second previous number.
  Then we add those calculated values
  '''
  if n == 0 or n == 1:
    return n
  elif n >= 2:
    return fibonacci(n - 1) + fibonacci(n - 2)

 
# The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:

# 2, 1, 3, 4, 7, 11, 18, 29, ...

# add a new function lucas that returns the nth value in the lucas numbers Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring.


# recursive solution

def lucas(n):
  '''
  Lucas numbers are the sum of it's two previous numbers.
  The first two terms are 2 and 1.
  Base numbers must be set to reflect those terms. 
  n is the number. 
  n - 1 refers to it's previous number. 
  n - 2 refers to it's second previous number.
  Then we add those calculated values
  '''
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    return lucas(n - 1) + lucas(n - 2)


# Both the fibonacci series and the lucas numbers are based on an identical formula. 
# Add a third function called sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. 
# The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

# Calling this function with no optional parameters will produce numbers from the fibonacci series. 
# Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. 
# Other values for the optional parameters will produce other series.

def sum_series(n, parameter1 = 0, parameter2 = 1):
  '''
  n is a required parameter
  parameter 1 and two are optional, they determine first two values in the series
  assign n to 0 for the base case of fibonacci
  assign optional parameters as 2 and 1 as base case of lucas
  '''
  if n == 0:
    return fibonacci(n)
  elif parameter1 == 2 and parameter2 == 1:
    return lucas(parameter1, parameter2)