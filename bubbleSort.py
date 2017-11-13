def bubblesort(list):
    listlength = len(list) - 1
    for cycle in range(listlength, 0, -1):
        for i in range(cycle):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


def bubblesortsmart(list):
    listlength = len(list) - 1
    swaped = True

    for cycle in range(listlength, 0, -1):
        if swaped is not True:
            break
        swaped = False
        for i in range(cycle):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swaped = True

    return list

list = [5, 6, 9, 98, 5, 12, 46]
bubblesort(list)
bubblesortsmart(list)
print(list)
