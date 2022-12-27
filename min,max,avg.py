lst=[]
while(True):
    inpnum=int(input("enter a value(0 toend):"))
    if inpnum==0:
        break
    else:
        lst.append(inpnum)
lst.sort()
print("min",lst[0])
print("max",lst[-1])
print("avg",round(sum(lst)/len(lst),1))
        
    
