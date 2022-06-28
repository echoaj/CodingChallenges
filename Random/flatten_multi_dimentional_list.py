

# Flatten a multidimentional list
# Given an array where each entry can be another array, and so forth,
# flatten the array. [4, [3, 6, [9, 1, 9, [5, 1]]]


def flatten_multi_dimentional_list(list_of_lists):
    """
    Flatten a multidimentional list
    Given an array where each entry can be another array, and so forth,
    flatten the array. [4, [3, 6, [9, 1, 9, [5, 1]]]]
    """
    flattened_list = []
    for item in list_of_lists:
        if isinstance(item, list):
            flattened_list.extend(flatten_multi_dimentional_list(item))
        else:
            flattened_list.append(item)
    return flattened_list


print(flatten_multi_dimentional_list([4, [3, 6, [9, 1, 9, [5, 1]]]]))
print(flatten_multi_dimentional_list([4, [3, 6, [9, 1, 9, [5, 1]]], [1, 2, 3]]))