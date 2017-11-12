def linearsearch(list, item):
    listlength = len(list)
    for i in range(listlength):
        if item == list[i]:
            print("Found at", i)
            return
        elif list[i] > item:
            return

    print("Not Found")

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

linearsearch(list, 7)
