class Person:
    '''person entity'''
    
    def __init__(self, first_name, last_name, surname, age):
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        self.age = age
        
    def __repr__(self):
        return f'Person(first_name={self.first_name}, last_name={self.last_name}, surname={self.surname}, age={self.age}'
    
    def __lt__(self, other):
        check_realquick = self.age > other
        return check_realquick
data = [
    {"first_name":"John", "last_name":"Jobs", "surname":"Israel", "age":24},
    {"first_name":"Mike", "last_name":"Isaac", "surname":"Thiago", "age":25},
    {"first_name":"Mary", "last_name":"Emmanuel", "surname":"Jackson", "age":30}
    
    ]
result = [Person(**row)for row in data]
print(result)
