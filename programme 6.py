class Student:
    college='MTICA'
    course='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displaystudent(self):
        print('Name: '+self.name+'\nrollno: '+str(self.rollno))
        print('college: '+self.college+'\ncourse: '+self.course)

for i in range(2):
    n=input()
    r=int(input())
    obj=Student(n,r)
    obj.displaystudent()
