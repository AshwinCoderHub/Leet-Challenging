def merge_lists(list1, list2):
    """
    Merge two sorted lists into a new sorted list.

    Parameters:
    - list1 (list): The first sorted list.
    - list2 (list): The second sorted list.

    Returns:
    - list: A new list containing all elements from both input lists in non-decreasing order.
    """
    result = []  # Initialize an empty list to store the merged result
    i = j = 0  # Initialize pointers for list1 and list2


    while i < len(list1) and j < len(list2):
        # Compare elements and append the smaller one to the result
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # Add any rest elements from list1 and list2
    result.extend(list1[i:])
    result.extend(list2[j:])

    return result


# Example usage:
list1 = [1, 2, 4]
list2 = [1, 3, 4]
result = merge_lists(list1, list2)
print(result)

list1 = []
list2 = []
b = merge_lists(list1, list2)
print(b)

list1 = []
list2 = [0]
c = merge_lists(list1, list2)
print(c)
