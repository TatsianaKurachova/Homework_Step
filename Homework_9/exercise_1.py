class Student:
    def __init__(self, name='Ivan', age=18, group_number='10A'):
        self.name = name
        self.age = age
        self.groupNumber = group_number
 
    def get_name(self):
        return f'Name - {self.name}'
 
    def get_age(self):
        return f'Age - {self.age}'
 
    def get_group_number(self):
        return f'Group number - {self.groupNumber}.'
 
    def set_name(self):
        print("Name:", self.name) 

    def set_group_number(self):
        print("Group number:", self.groupNumber)  
    
    def set_age(self):
        print("Age:", self.age)      
        
Sophia = Student('Sophia', 23, '10G')
print(f'{Sophia.get_name()}, {Sophia.get_age()}, {Sophia.get_group_number()}')
Anna = Student('Anna', 18, '09B')
print(f'{Anna.get_name()}, {Anna.get_age()}, {Anna.get_group_number()}')
Maksim = Student('Maksim', 21, '10F')
print(f'{Maksim.get_name()}, {Maksim.get_age()}, {Maksim.get_group_number()}')
Andry = Student('Andry', 19 ,'11A')
print(f'{Andry.get_name()}, {Andry.get_age()}, {Andry.get_group_number()}')
Ivan = Student()
print(f'{Ivan.get_name()}, {Ivan.get_age()}, {Ivan.get_group_number()}')
Michail = Student('Michail', 20, '09B')
print(f'{Michail.get_name()}, {Michail.get_age()}, {Michail.get_group_number()}')