"""
Flatten array of arbitrarily nested arrays of integers into flat array of integers

Ex [[1,2,[3]],4] -> [1,2,3,4]
"""


def flatten_array(input: list, output: list = None) -> list:
    if output is None:
        output = []

    for item in input:
        if isinstance(item, int):
            output.append(item)
            continue

        flatten_array(item, output)

    return output


# Tests

assert flatten_array([[1, 2, [3]], 4]) == [1, 2, 3, 4]
assert flatten_array([[[]]]) == []
assert flatten_array([]) == []
assert flatten_array([67, [0, 7, 9], [444, 0, 3], 4, 6, [8], 9]) == [67, 0, 7, 9, 444, 0, 3, 4, 6, 8, 9]
assert flatten_array([-1, [99], [-99, [0, 7], -5]]) == [-1, 99, -99, 0, 7, -5]
assert flatten_array([5, [], 6, 7]) == [5, 6, 7]
