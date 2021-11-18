"""
Puzzle 13:

Write a binary search function to determine if a value is in a
sorted list of values.
"""


def binary_search(sorted_list, val):
    if not sorted_list:
        return False

    index = len(sorted_list) // 2
    if sorted_list[index] == val:
        return True
    elif sorted_list[index] > val:
        return binary_search(sorted_list[:index], val)
    else:
        return binary_search(sorted_list[index + 1 :], val)


def binary_search_index(sorted_list, val, offset=0):
    if not sorted_list:
        return False

    index = len(sorted_list) // 2
    if sorted_list[index] == val:
        return index + offset
    elif sorted_list[index] > val:
        return binary_search_index(sorted_list[:index], val, offset)
    else:
        return binary_search_index(sorted_list[index + 1 :], val, index + 1 + offset)


if __name__ == "__main__":

    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))

    print(binary_search_index([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    print(binary_search_index([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))
