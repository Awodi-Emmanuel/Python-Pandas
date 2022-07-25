from .add import Subject
class School:
    def __init__(self, *subjects):
        self.subjects = list(subjects)
    
    def __len__(self):
        return len(self.subjects)
Sub = School(Subject(), Subject())
print(len(Sub))
