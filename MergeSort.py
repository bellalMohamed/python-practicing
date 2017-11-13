def mergesort(array):
    if len(array) <= 1:
        return array
    midpoint = int(len(array) / 2)
    left, right = mergesort(array[:midpoint]), mergesort(array[midpoint:])

    return merge(left, right)


def merge(left, right):
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result.extend(right[right_pointer:])
    result.extend(left[left_pointer:])
    return result

sortedArray = mergesort([5, 6, 8, 9, 4, 2, 13, 12, 3, 2, 5])
print(sortedArray)
