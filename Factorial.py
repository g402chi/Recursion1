__author__ = 'chiragmirani'

# This is my first program in Python. It has a factorial function in Python and it tests whether it works
import math

def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)



print factorial(5)
