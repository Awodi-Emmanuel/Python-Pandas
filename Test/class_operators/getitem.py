class School:
    def __init__(self, *subjects):
        self.subjects = subjects
        
    def __getitem__(self, i):
        return self.subjects[i]
    
sub = School(Subject(), Subject())
print(len(sub[0]))