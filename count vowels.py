def extracdigit(s):
    n=
    for i in s:
        if i in '1234567890':
            n+=1
    return n
str1=input()
a=extracdigit(str1)
print("no.of.vowels in:'",str1,"'is",a)
