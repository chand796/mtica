class Employee:
    empCount=0
    def __init__ (self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount +=1
    def displaycount(self):
        print("total employee of %d" % Employee.empCount)
    def displayemployee(self):
        print("name:", self.name, "salary", self.salary)
emp1=Employee("nikhil",9999)
emp1.displayemployee()
print("is salary an attribute",hasattr(emp1,'salary'))
print(getattr(emp1,'salary'))
setattr(emp1,'salary',7000)
print("modified salary",getattr(emp1,'salary'))
print(hasattr(emp1,'desg'))
setattr(emp1,'desg','manager')
print(hasattr(emp1,'desg'))
print("added attribute",getattr(emp1,'desg'))
delattr(emp1,'salary')
print("is salary an attribyte",hasattr(emp1,'salary'))
