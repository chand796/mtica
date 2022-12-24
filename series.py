'''def printseries(n):
    temp=[]
    for i in range(n+1):
        temp.append(i)
    return temp
n=input("emter number")
ans=printseries()
print(*ans)
print(sum(ans))'''
'''import math
def checkprimenumber(num):
    if num<1:
        return 0
    if num==1 or num==2 or num==3:
        return num
    count=int(math.sqrt(num))+1
    count=num//2+1
    for i in range(2,count):
        if num%i==0:
            return 0
        return num
start=int(input())
stop=int(input())
lst=[]
for i in range(start,stop+1):
    if checkprimenumber(i):
        lst.append(i)
print(*lst)
print(len(lst))'''
def checkarmstrongnum(num):
    num=str(num)
    n=len(num)
    total=0
    for i in num:
        total+=int(i)**n
    if int(num)==total:
        return 1
    else:
        return 0
inpnum=int(input())
if checkarmstrongnum(inpnum):
    print("yes")
else:
    print("No")

    
     
