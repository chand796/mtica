def EXTRACTSPECIALCHAR(s):
    n=''
    for i in s:
        if i in 'QWERTYUIOPKJHGFDSMNBVCXZqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&~*()':
            n+=i
    return n
str1=input()
a=EXTRACTSPECIALCHAR(str1)
print("EXTRACTSPECIALCHAR in:'",str1,"'is",a)
