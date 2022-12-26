def removevowels(s):
    temp=''
    for i in s:
        if i not in 'AEIOUaeiou':
            temp+=i
    return temp
str1=input()
a=removevowels(str1)
print("string",str1,"without vowel is",a)
