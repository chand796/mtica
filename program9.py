class A:
    def first_method(self):
        print("i am in first method")
class B:
    def second_method(self):
        print("i am second method")
class C(A,B):
    def third_method(self):
        print("i am in third method")
if __name__ =="__main__":
    ob=C()
    ob.first_method()
    ob.second_method()
    #ob.third_method()
    
