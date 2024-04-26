class Person:

    def init(self, name, phone, holiday=None, salary = None):
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