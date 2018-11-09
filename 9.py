"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def max_subarray_sum(A):
    # M[i] = max( M[i-1], M[i-2] + A[i]), M[-1] = 0, M[0] = A[0] 1 <=i <= N
    A[1] = max(A[0], A[1])
    i = 2
    while i < len(A):
        A[i] = max(A[i-1], A[i-2] + A[i])
        i += 1
    return A[-1]

assert(max_subarray_sum([2, 4, 6, 2, 5]) == 13)
assert(max_subarray_sum([5, 1, 1, 5]) == 10)
