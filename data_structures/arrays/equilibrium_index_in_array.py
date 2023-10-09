"""
Find the Equilibrium Index of an Array.
Reference: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

Python doctests can be run with the following command:
python -m doctest -v equilibrium_index.py

Given a sequence arr[] of size n, this function returns
an equilibrium index (if any) or -1 if no equilibrium index exists.

The equilibrium index of an array is an index such that the sum of
elements at lower indexes is equal to the sum of elements at higher indexes.



Example Input:
arr = [-7, 1, 5, 2, -4, 3, 0]
Output: 3

"""


def equilibrium_index(arr: list[int], size: int) -> int:
    """
    Find the equilibrium index of an array.

    Args:
        arr : The input array of integers.
        size : The size of the array.

    Returns:
        int: The equilibrium index or -1 if no equilibrium index exists.

    Examples:
        >>> equilibrium_index([-7, 1, 5, 2, -4, 3, 0], 7)
        3
        >>> equilibrium_index([1, 2, 3, 4, 5], 5)
        -1
        >>> equilibrium_index([1, 1, 1, 1, 1], 5)
        2
        >>> equilibrium_index([2, 4, 6, 8, 10, 3], 6)
        -1
    """
    total_sum = sum(arr)
    left_sum = 0

    for i in range(size):
        total_sum -= arr[i]
        if left_sum == total_sum:
            return i
        left_sum += arr[i]

    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
