SALARY = 40000

class Person:
    def init(self, name, phone, age):
        self._name = name
        self._phone = phone
        self._age = age
        self._salary = SALARY

    def _set_salary(self, salary):
        self._salary = salary

    def _get_salary(self):
        return self._salary

    def change_name(self, new_name):
        self._name = new_name

    def change_salary(self, new_salary):
        self._set_salary(new_salary)

    def change_phone(self, new_phone):
        self._phone = new_phone

    def change_age(self, new_age):
        self._age = new_age

    def get_age(self):
        return self._age

class Manager(Person):
    def init(self, name, age, phone):
        super().init(name, age, phone)
        self._set_salary(int(SALARY * 1))


class Programmer(Person):
    def init(self, name, age, phone):
        super().init(name, age, phone)
        self._set_salary(int(SALARY * 1.2))


manager = Manager('John', "23", '123123123')
programmer = Programmer('John', "23", '123123123')


manager.change_name("John")
manager.change_salary(int(SALARY * 1))
manager.change_phone("123-456-7890")
programmer.change_name("Jane")
programmer.change_salary(int(SALARY * 1.2))
programmer.change_phone("987-654-3210")
manager.change_age(31)
programmer.change_age(26)


print(f"Manager: {manager._name}, Number phone: {manager._phone}, Age: {manager.get_age()}, Salary: {manager._get_salary()}")
print(f"Programmer:. {programmer._name}, Number phone: {programmer._phone}, Age: {programmer.get_age()}, Salary: {programmer._get_salary()}")