def factorial(num):
    assert(num>=0),"factorial of negative num is not possible"
    assert(isinstance(num,int)),"factorial of non integers not possible  "
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
try:
    print(factorial(-5))
except Exception as ob:
    print(ob)
try:
    print(factorial(5.3))
except Exception as ob:
    print(ob)
try:
    print(factorial(5))
except Exception as ob:
    print(ob)
try:
    print(factorial("today"))
except Exception as ob:
    print(ob)    
