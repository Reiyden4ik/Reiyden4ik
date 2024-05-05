SALARY = int(input())

import collections

class Person:
    __slots__ = ['_attributes']

    def __init__(self, name, phone, age):
        self._attributes = collections.namedtuple('Attributes', ['name', 'phone', 'age', 'salary'])(name, phone, age, SALARY)

    def change(self, attr, new_val):
        attrs = self._attributes._asdict()
        attrs[attr] = new_val
        self._attributes = collections.namedtuple('Attributes', attrs.keys())(*attrs.values())
        return getattr(self._attributes, attr)

class Manager(Person):
    __slots__ = []

    def __init__(self, name, age, phone):
        super().__init__(name, age, phone)
        self.change('salary', int(SALARY * 1))

class Programmer(Person):
    __slots__ = []

    def __init__(self, name, age, phone):
        super().__init__(name, age, phone)
        self.change('salary', int(SALARY * 1.2))

manager = Manager('John', 23, '123123123')
programmer = Programmer('John', 23, '123123123')

manager.change('name', "Jack")
manager.change('salary', int(SALARY * 1))
manager.change('phone', "123-456-789")
programmer.change('name', "Zane")
programmer.change('salary', int(SALARY * 1.2))
programmer.change('phone', "987-654-321")
manager.change('age', 32)
programmer.change('age', 28)

print(f"Manager: {manager._attributes.name}, Number phone: {manager._attributes.phone}, Age: {manager._attributes.age}, Salary: {manager._attributes.salary}")
print(f"Programmer: {programmer._attributes.name}, Number phone: {programmer._attributes.phone}, Age: {programmer._attributes.age}, Salary: {programmer._attributes.salary}")