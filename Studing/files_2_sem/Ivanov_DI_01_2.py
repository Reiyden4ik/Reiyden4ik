"""
Создайте класс "Соус" (для определения вкуса соуса: сырный, чесночный и т.д.), принимающий 1 аргумент при инициализации (отвечающий за вкус). 
В этом классе реализуйте метод show_my_souce(), выводящий на печать Соус и {ДОБАВКА} в случае наличия добавки, а иначе отобразится следующая фраза: Майонез.
"""

class Sause:
    dobavka = str(input())
    def __init__(self, sause):
        self.sause = 'Chesnok'
    def show_my_souse(self, sause):
        if dobavka == '':
            print("Майонез")
        else:
            print(s + '' + dobavka)

"""
Создайте класс Employee (сотрудник), который имеет следующие приватные свойства:
name – имя сотрудника; age – возраст; salary – оклад; bonus – премия. Класс Employee должен иметь следующие методы:
get_name() – возвращает имя сотрудника; get_age() – возвращает возраст; get_salary() – возвращает зарплату сотрудника; 
set_bonus(bonus) – устанавливает свойство bonus; get_bonus() – возвращает бонус для сотрудника; 
get_total_salary() – возвращает общую зарплату сотрудника (оклад + бонус).
"""

class Employee:
    def __init__(self, name, age, salary, bonus):
        self.name = name
        self.age = age
        self.salary = salary 
        self.bonus = bonus
    
    def get_name(self):
        name = str(input())
    def get_age(self):
        age = int(input())
    def get_salary(self):
        salary = int(input())
    def set_bonus(self, salary):
        self.bonus = salary*0,1
    def get_bonus(self):
        bonus = self.bonus
    def get_total_salary(self):
        print(salary+bonus)
