def extractspecialchar(s):
    n=''
    for i in s:
        if i in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            n+=i
    return n
str1=input()
a=extractspecialchar(str1)
print("extractspecialchar in:'",str1,"'is",a)
