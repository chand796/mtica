'''def checkanagram(s1):
    s2=s1[::-1]
    if s1==s2:
        return'yes'
    else:
        return'no'
inp=int(input())
print(checkanagram()'''
def extract_vowel(s):
    temp=''
    for i in s:
        if i in 'AEIOUaeiou':
            temp+=i
    return temp
str1=input()
a=extract_vowel(str1)
print(a)
