import textwrap
def word_wrap3(adres):
    with open(adres) as f:
        icerik=f.readlines()
        icerik=[elem.replace('\n','') for elem in icerik]
        s=''
        for i in range(0,len(icerik)):
            for j in range(0,len(icerik[i]),60):

                s+=icerik[i][j:j+60]
                s+='\n'
        print(s)
word_wrap3("any.txt")