def COUNTextractspecialchar(s):
    n=0
    for i in s:
        if i in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            n+=1
    return n
str1=input()
a=COUNTextractspecialchar(str1)
print("countextractspecialchar in:'",str1,"'is",a)
