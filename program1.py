##class Vehicle:
##    def __init__(self,name,max_speed,mileage):
##        self.name=name
##        self.max_speed=max_speed
##        self.mileage=mileage
##    def capacity(self,capacity):
##        return "the seating capacity of a{self.name}\is {capacity} passengers"
##class Bus(Vehicle):
##    def capacity(self,capacity=50):
##        return super().capacity(capacity=50)
##school_bus=Bus("school volvo",180,12)    
##
##print(school_bus.capacity())
a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print("a:",a)
print("b:",b)
