def collapse(list):
    listm = []
    if len(list) % 2 == 0:
        for i in range(0, len(list), 2):
            listm.append(list[i] + list[i + 1])
        return listm
    else:

        for i in range(0, len(list)-1, 2):

            listm.append(list[i] + list[i + 1])
        listm.append(list[len(list) - 1])
        return listm


x = [1, 2, 3]
print(collapse(x))
