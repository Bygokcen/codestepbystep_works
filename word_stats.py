import string


def word_stats(adres):
    with open(adres) as f:
        icerik = f.readlines()
        text = []
        alpha = []
        average = 0
        for i in range(0, len(icerik)):
            cumle = icerik[i].split()

            for k in range(len(cumle)):
                x = cumle[k]
                text.append(x.lower())
        for i in range(len(text)):
            average += len(text[i])
            for j in range(len(text[i])):
                if text[i][j] not in alpha and text[i][j].isalpha():
                    alpha.append(text[i][j])
        print("Total words    =",len(text))
        print("Average length =",average/len(text))
        print("Unique letters =",len(alpha))



word_stats("tobe.txt")
