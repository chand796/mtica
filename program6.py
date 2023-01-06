##def outer():
##    print('outerfunction')
##    def inner():
##        print('innerfunction')
##    inner()
##outer()
#*****************************************
##message='outer function'
##def outer():
##    
##    def inner():
##        print(message)
##    inner()
##outer()
def outer():
    message='outer scope'
    print(message)
    def inner():
        nonlocal message
        message='inner scope'
        print('inner:',message)
    inner()
    print('outer:',message)
outer()
