def div(a,b):
    assert (isinstance(a,int) or isinstance(a,float)) ,"argargument should be either int or float"
    assert(isinstance(a,int) or isinstance(a,float)),"argument should be either int or float"   
    
    assert(b!=0),"division by zero is not defined"
    return a/b
try:
    print(div(3,0))
except Exception as ob:
    print(ob)
try:
    print(div(20,3))
except Exception as ob:
    print(ob)
try:
    print(div(100,20))
except Exception as ob:
    print(ob)
try:
    print(div("hello",4))
except Exception as ob:
    print(ob)    
    
        
