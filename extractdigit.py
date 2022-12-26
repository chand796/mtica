def extractdigit(s):
    n=''
    for i in s:
        if i in '1234567890':
            n+=i
    return n
str1=input()
a=extractdigit(str1)
print("extractdigits in:'",str1,"'is",a)
