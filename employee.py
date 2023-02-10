class Employee:
    raise_amt=1.04
    def __init__(self,first_name=None,last_name=None,pay=0):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    def apply_raise(   self):
        self.pay = self.pay * self.raise_amt
    
class Developer(Employee):
    def __init__(self,first_name=None,last_name=None,pay=0,prog_lang=None):
        super().__init__(first_name,last_name,pay)
        self.prog_lang =prog_lang

class Manager(Employee):
    def __init__(self,first_name=None,last_name=None,pay=0,employees=None):
        super().__init__(first_name,last_name,pay)
        if employees is None:
            self.employees  = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_employees(self):
        print(" Developers Working under Manager {}".format(self.first_name))
        for emp in self.employees:
            print('---> ' ,emp.fullname())

dev1  = Developer('Ashish','C',50000,'Java')
dev2  = Developer('Harsh','Upreti',1000,'Python')
mgr_1 = Manager('Shubham','Sonawane',9000,[dev1,dev2])
mgr_1.print_employees()
