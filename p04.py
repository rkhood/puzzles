"""
Puzzle 04:

Write a function that takes two lists as input,
and returns True if one list is a rotation of the other.
"""

def is_rotate_trivial(lst_1, lst_2):

    if len(lst_1) != len(lst_2):
        return False

    checklist = lst_1 * 2
    for i, num in enumerate(checklist):
        if num == lst_2[0]:
            index_list = checklist[i:i+len(lst_1)]
            if lst_2 == index_list:
                return True

    return False


def is_rotate(lst_1, lst_2):

    def make_dict(lst):
        offset = lst[1:] + [lst[0]]
        return {key: val for key, val in zip(lst, offset)}

    if make_dict(lst_1) == make_dict(lst_2):
        return True

   return False


if __name__ == "__main__":

    lst_1 = [1, 2, 3, 4, 5]
    lst_2 = [3, 4, 5, 1, 2]

    print(is_rotate(lst_1, lst_2))
