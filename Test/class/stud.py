# The two types of class operations the operaton are:
# attribut reference  and Instantiation   

# from inspect import Attribute


# # Example1 class Attribute reference  
# class Student:
#     '''A simple example class'''
#     stu_class = 'V'
#     stu_roll_no = 13
#     stu_name = 'emmy'
    
#     def msg(self):
#         return 'New session will start soon.'
    
# print(Student.stu_class, Student.stu_roll_no, Student.stu_name, Student.__doc__)


# Example2 class intance /

class Stud:
    
    def __init__(self, sclass, sroll, sname):
        self.c = sclass
        self.r= sroll
        self.n = sname
        
    def messg(self):
        my_mess = 'new session will start soon'
        return my_mess
    
calls = Stud("B", 24, "jacob")
print(calls.c, calls.r, calls.n, Stud.__doc__)