def findFactor(n):""#FOR FINDING FACTORS""
    temp=list()
    for i in range(1,n+1):
        if n%i==0:
            temp.append(i)
    return temp
if temp%2==0:
    return temp
    
print("enter nums")
a= int(input())
print(*findFactor(a))


#FOR GCD
##def findgcd(n):
##    temp=[]
##    for i in range(1,n+1):
##        if n%i==0:
##            temp.append(i)
##    return temp
##def findgcd2(n1,n2):
##    lst1=findgcd(n1)
##    lst2=findgcd(n2)
##    s1=set(lst1)
##    s2=set(lst2)
##    ans=list(s1.intersection(s2))
##    ans.sort()
##    return ans[-1]
##print("enter two numbers")
##a=int(input())
##b=int(input())
##print(findgcd2(a,b))
##    
