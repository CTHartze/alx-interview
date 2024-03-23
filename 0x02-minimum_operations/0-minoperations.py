#!/usr/bin/python3
"""Script calculates prime factors for minimum operations"""


import math


def factors(n):
    """calculates prime factors of given number n"""
    mylist = []
    while n % 2 == 0:
        mylist.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            mylist.append(i)
            n = n / i
    if n > 2:
        mylist.append(n)
    return mylist


def minOperations(n):
    """calculate the minimum operations to reach n"""
    if type(n) != int or n < 2:
        return 0
    else:
        numOperations = sum(factors(n))
        return int(numOperations)
