def selectionsort(list):
    n = len(list)

    for i in range(n - 1):
        min = list[i]
        minposition = i
        for j in range(i + 1, n):
            if list[j] < min:
                min = list[j]
                minposition = j

        list[minposition], list[i] = list[i], list[minposition]


list = [5, 6, 9, 98, 5, 12, 46]
# list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
selectionsort(list)
print(list)
