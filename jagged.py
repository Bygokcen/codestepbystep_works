jagged = [[0] * 0 for i in range(5)]

count = 1
for i in range(0, 5):

    for k in range(-1, i):
        jagged[i].append(count)
        count += 1
print(jagged)
