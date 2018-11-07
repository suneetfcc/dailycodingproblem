"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def solve(numbers):

    L = len(numbers)
    left = [1] * L
    right = [1] * L

    for i in range(1, L):
        left[i] = left[i-1] * numbers[i-1]

    for i in range(L-2,-1,-1):
        right[i] = right[i+1] * numbers[i+1]

    return [a*b for a,b in zip(left, right)]


# Test Cases
numbers = list(range(1,6))
assert(solve(numbers)) == [120, 60, 40, 30, 24]
