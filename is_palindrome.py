def is_palindrome(x):
    x=x.lower()
    rev=-1
    for i in range(0,int(len(x)/2)):
        if x[i]!=x[rev]:
            return False
            break
        else:
            rev-=1
    return True

        
name="123 $$ 321"
print(is_palindrome(name))