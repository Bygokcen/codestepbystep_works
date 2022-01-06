def is_rotation(str1,str2):
    if len(str1)!=len(str2):
        return False
    temp = str1+str1
    print(temp)
    if temp.count(str2)>0:
        return True
    else:
        return False
    
print(is_rotation("COMPUTER", "UTERCOMP" ))