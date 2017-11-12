def binarysearch(list, item):
    first = 0
    last = len(list) - 1
    midpoint = 0

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            print('Found')
            return
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    print('Not Found')


def binarysearchrec(list, item):
    if len(list) == 0:
        print('Not Found')
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == item:
            print('Found')
            return True
        else:
            if item < list[midpoint]:
                return binarysearchrec(list[:midpoint], item)
            else:
                return binarysearchrec(list[midpoint + 1:], item)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

binarysearchrec(list, 10)
