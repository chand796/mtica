def removeduplicates(s):
    str1=''
    for i in s:
        if i not in str1:
            str1+=i
    return str1
str2=input()
a=removevowels(str2)
print("without duplicates",removevowels(str2))
