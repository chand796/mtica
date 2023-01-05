class Employee:
    empCount=0
    def __init__ (self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount +=1
    def displaycount(self):
        print("total employee of {0}" .format(Employee.empCount))
    def displayemployee(self):
        print("name:", self.name, "salary", self.salary)
emp1=Employee("nikhil",9999)
emp1.displayemployee()
emp1.salary=17000
emp1.experience=3
emp1.displayemployee()
emp1.name="manoj"
emp1.displayemployee()
print(emp1.experience)
#del emp1.salary
emp1.displayemployee()
