def quick_sort(list):
    less, equal, greater = [], [], []

    if len(list) > 1:
        pivot = list[0]
        for x in list:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)

        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return list

print(quick_sort([12, 4, 5, 6, 7, 3, 1, 15]))
