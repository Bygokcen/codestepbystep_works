def word_wrap3(adres):
    with open(adres) as f:

        icerik = f.readlines()
        icerik = [elem.replace('\n', '') for elem in icerik]
        count = 0

        for i in range(0, len(icerik)):
            if len(icerik[i]) <= 60:
                print(icerik[i], end="")

            else:
                texts = icerik[i].split(" ")
                for text in texts:
                    if count+len(text)<=60:
                        print(text,end=" ")
                        count+=len(text)+1
                    else:
                        print()
                        print(text,end=" ")
                        count=len(text)+1

                count = 0
            print()


word_wrap3("any.txt")
