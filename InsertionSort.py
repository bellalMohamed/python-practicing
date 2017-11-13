def insertion_sort(list):
    for index in range(1, len(list)):
        currentValue = list[index]
        position = index

        while position > 0 and list[position - 1] > currentValue:
            list[position] = list[position - 1]
            position -= 1
            list[position] = currentValue

    return list

print(insertion_sort([12, 4, 5, 6, 7, 3, 1, 15]))
