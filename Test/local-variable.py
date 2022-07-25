# python-local-variable.py
def fun_local(a):
    print('a is -> ', a)
    a = 50
    print('After new value within the function a is -> ',a)
a = 100
    
fun_local(40)
print('Value of a is ->', a)