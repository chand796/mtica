class Dog:
    price=400
    def __init__(self,name,color):
        self.name=name
        
        self.color=color
    def bark(self):
        print("woof")
        print(self.name,"has",self.price,"and in",self.color)
if __name__=="__main__":
    pet1=Dog("tommy","brown",300)
    pet2=Dog("sheru","white")
    pet1.bark()
    pet2.bark()
    print(pet1.price)
    print(pet2.price)
    print(Dog.price)
    Dog('abc','blue').bark()
