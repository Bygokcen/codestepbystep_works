def collapse_pairs(list):
    if len(list) % 2 == 0:
        for i in range(0, len(list), 2):
            x = list[i] + list[i + 1]
            if x % 2 != 0:
                list[i + 1] = x
                list[i]=0
            else:
                list[i] = x
                list[i+1]=0
    else:
        for i in range(0, len(list) - 1, 2):
            x = list[i] + list[i + 1]
            if x % 2 != 0:
                list[i + 1] = (x)
                list[i]=0
            else:
                list[i] = (x)
                list[i+1]=0
    return list


x = [7, 2, 8, 9, 4, 22, 7, 1, 9, 10]

print(collapse_pairs([7, 2, 8, 9, 4, 22, 7, 1, 9, 10]))
print(collapse_pairs([1, 4, 2, 4, 7, 1, 1, 9, 2, 3, 4, 1]))
print(collapse_pairs([0, 0, -1, -1, -1, 5, 5, 5, 0, 0]))
print(collapse_pairs([42, 42, 42, 42]))
print(collapse_pairs([2, 5, 6]))
print(collapse_pairs([1, 3, 3]))
print(collapse_pairs([2, 4, 6, 8, 10, 12, -2, -4]))
print(collapse_pairs([1]))