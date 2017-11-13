def sumoflist(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sumoflist(list[1:])


list = [5, 6, 9, 98, 5, 12, 46]
sum = sumoflist(list)
print(sum)
