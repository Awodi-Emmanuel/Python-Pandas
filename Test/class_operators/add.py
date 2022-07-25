class School:
    def __init__(self, *subjects):
        self.subjects = list(subjects)
        
class Subject:
    def __add__(self, other):
        return School(self, other)
F1, F2 = Subject(), School()
print(F1 + F2)
