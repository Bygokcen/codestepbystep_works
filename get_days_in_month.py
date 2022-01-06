def get_days_in_month(x):
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    return month[x+1]


def is_all_vowels(x):
    a=x.lower()
    b = ["a", "e", "i", "o", "u"]
    for i in range(0,len(a)):
        if a[i].isalpha():
            if a[i] in b:
                continue
            else:
                return False
                break
        else:
            continue
    return True
print(is_all_vowels("banana"))
