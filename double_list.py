def double_list(list):
    x = len(list)
    for i in range(0, len(list) * 2, 2):
        list.insert(i, list[i])


double_list(['1', '0', '6'])

