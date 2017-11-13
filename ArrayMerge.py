def mergetwosortedarrays(left, right):
    left_pointer = right_pointer = 0
    result = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result

lista = [2, 5, 6, 9]
listb = [3, 4, 7, 8]
mergedArray = mergetwosortedarrays(lista, listb)
print(mergedArray)
