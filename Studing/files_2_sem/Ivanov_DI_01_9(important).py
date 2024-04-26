from accessify import private, protected

class Person:

    def init(self, name, phone, salary = None):
        self.name = name
        self.phone = phone
        self._salary = salary
 
    @protected
    def set_salary(self, salary):
        self._salary = salary * self.k

    @protected
    def get_salary(self):
        print(self._salary)

class Manager(Person):

    def init(self, name, phone, rank, k = 1, salary=None):
        super().init(name, phone, salary)
        self.rank = rank 
        self.k = k
        
    
class Programmer(Person):

    def init(self, name, phone, rank, k = 1.2, salary=None):
        super().init(name, phone, salary)
        self.rank = rank
        self.k = k



m = Manager('Oleg', '525', 'Raver')
print(m.dict)
print(m.dict)

p = Programmer('Kolya', '52', 'Zoper')
print(p.dict)
print(p.dict)