class num:
    def __init__(self,n):
        #assert(length>=0 and width>=0),'invalid'
        self.n=n
       
    def even(self):
        if self.n%2==0:
           return "even"
        else:
            return "odd"
    def sumofdigits(self):
        if self.n<0:
            self.n=abs(self.n)
        tem=str(self.n)
        t=0
        for i in temp:
            t+=int(i)
        return t
    def armstrongnum(self):
        if self.n
        
    
n1=int(input("enter num"))
obj=num(n1)
print('given num is',obj.even())
print('sum of digits',obj.sumofdigits())
   
