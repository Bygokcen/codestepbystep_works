def min_to_front(x):
    y=min(x)
    c=0
    for i in range(0,len(x)):
        c=i
        if x[i]==y:
            break
    x.pop(c)
    x.insert(0,y)
    return x
list=[3, 8, 92, 4, 2, 17, 9]
min_to_front(list)