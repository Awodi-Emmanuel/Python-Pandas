# python-global-variable.py
def global_fun():
    global a
    print('a is -> ', a)
    a = 50
    print('After new value within the function a is -> ',a)
a = 100
    
global_fun()
print('Value of a is -> ',a)
