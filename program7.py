class Wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("grrr..")
        

class Dog(Wolf):
    def bark(self):
        print("woof")
pet1=Dog("tommy","brown")
pet1.bark()
pet2=Wolf("jimmy","gray")
pet2.bark()
Dog("abc","xyz").bark()

