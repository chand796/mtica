def COUNTSPECIALCHAR(s):
    n=0
    for i in s:
        if i in '!@#$%^&~*()qwertyuiasdfghjklxcvbnmQWERTYUIOPASDFGHJKLXCVBNM234567890op':
            n+=1
    return n
str1=input()
a=COUNTSPECIALCHAR(str1)
print("COUNTSPECIALCHAR in:'",str1,"'is",a)
