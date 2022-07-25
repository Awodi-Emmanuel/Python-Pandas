# python-inheritance.py
class CompanyMember:
    '''Represents Company Member'''
    def __init__(self, name, designation, age):
        self.name = name
        self.designation = designation
        self.age = age
        
    def tell(self):
        '''Details of employee.'''
        print(f'Name: ', self.name, '\nDesignation : ', self.designation, '\nAge : ', self.age)        
        
        
        
class FactoryStaff(CompanyMember):
    '''Repressent a factory staff'''
    def __init__(self, name, designation, age, overtime_allow):
        CompanyMember.__init__(self, name, designation, age) 
        self.overtime_allow = overtime_allow
        CompanyMember.tell(self)
        print('Overtime Allowance: ', self.overtime_allow)
        
FactoryStaff('Ben', 'Elect', 39, 250)

        
class OfficeStaff(CompanyMember):
    def __init__(self, name, designation, age, travelling_allow):
        self.travelling_allow = travelling_allow
        super().__init__( name, designation, age)
        super().tell()
        print('Travelling Allowance $ : ', self.travelling_allow)
        
OfficeStaff('Emmy', 'Software Eng', 24, 4000)        

        
        
        
        

    