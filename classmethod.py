class Employee:
    raise_amount=3
    def __init__(self):
        print("Initialisation started for employee")
    @classmethod
    def change_amount(cls):
        cls.raise_amount = 100
        return cls.raise_amount
emp1 = Employee()
emp1.raise_amount = 5
Employee.raise_amount = 4

print( emp1.change_amount() )
#print(Employee.__dict__)
print(Employee.raise_amount)
print(emp1.raise_amount) 
print(Employee.change_amount())
print(emp1.__dict__)

