class A:
    def first_method(self):
        print("method of class a")
class B(A):
    def first_method(self):
        print("method of class b")
        super().first_method()#calls the first method of the superclass "a"
ob=B()
ob.first_method()
