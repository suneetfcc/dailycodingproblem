'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

from bisect import bisect_left


def binary_search(alist, item):
        'Locate the leftmost value exactly equal to item'
        i = bisect_left(alist, item)
        if i != len(alist) and alist[i] == item:
            return i
        raise ValueError


def k_sum_1(numbers, k):
    '''
    O(n^2)
    iterate over list for all possible pairs and return those with sum k
    :param numbers:
    :param k:
    :return:
    '''
    return ((a, abs(k-a)) for a in numbers if abs(k-a) in numbers)

def k_sum_2(numbers, k):
    """
    O(nlogn) algorithm to return any pair from the list with sum k or None
    :param numbers: list of numbers
    :param k: int target sum
    :return: tuple pair or None
    """
    numbers.sort()
    for a in numbers:
        try:
            b_index = binary_search(numbers, abs(k-a))
            b = numbers[b_index]
            yield (a,b)
        except:
            pass
    return None

def k_sum_3(numbers, k):
    '''
    O(n) dictionary approach
    :param numbers:
    :param k:
    :return:
    '''
    numbers_lookup = set(numbers)
    return ((a, abs(a-k)) for a in numbers_lookup if abs(a-k) in numbers_lookup)

if __name__ == '__main__':
    nums = [10, 15, 3, 7]
    k = 17

    print(list(k_sum_1(nums, k)))
    print(list(k_sum_2(nums, k)))
    print(list(k_sum_3(nums, k)))