def first_digit(x):
    y=abs(x)
    r=1
    while True:
        if y // r > 0:
            r *= 10
            continue
        else:
            r //= 10

            break

    return y//r
first_digit(-947)
print(11%10)
