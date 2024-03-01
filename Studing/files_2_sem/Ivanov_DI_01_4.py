'''
Простой класс, представляющий рациональную дробь (num – числитель, den – знаменатель).
Класс содержит конструктор и методы умножения и деления (дроби на дробь и дроби на целое число).
Метод создания случайной дроби из заданного диапазона целых чисел объявлен как статический.
Следует отметить, что в языке имеется готовый тип Fraction в модуле fractions.
И данный пример нужно рассматривать только как образец для создания собственных классов.
'''

class Ratiofraction:
    def __init__(self, rum, den):
        if self.__check_den__(den):
            self.rum = rum
            self.den = den
    @classmethod
    def __check_den__(cls, den):
        if den > 0:
            return True
        raise ValueError("den must be natural!")
rt = Ratiofraction(int(input()), int(input()))
print(rt.rum, "/", rt.den)