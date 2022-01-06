import string

adres = "weather.txt"  # input("Input file? ")
with open(adres) as f:
    icerik = f.readlines()
    listm = []
    for i in range(0, len(icerik)):
        fix = str(icerik[i]).split()
        for j in range(0, len(fix)):
            s = fix[j]
            x=s.translate(str.maketrans('', '', string.punctuation))
            if x.islower() or x.isupper() or x in string.punctuation :
                continue
            else:
                listm.append(float(s))

    for i in range(1, len(listm)):
        x = listm[i] - listm[i - 1]
        print(listm[i - 1], "to", str(listm[i]) + ", change =",round(x,2))
