'''
Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. 
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа. С помощью метода is_triangle() возвращаются следующие значения
(в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.
'''
class TriangleChecker:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_triangle(self):
        if not (isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)) and isinstance(self.z, (int, float))):
            raise ValueError("Нужно вводить только числа!")
        if self.x <= 0 or self.y <= 0 or self.z <= 0:
            return False
        if self.x + self.y <= self.z or self.x + self.z <= self.y or self.y + self.z <= self.x:
            return False
        return True

    def get_values(self):
        return self.x, self.y, self.z

trian = TriangleChecker(1, 2, 3)
try:
    trian.x = int(input())
    trian.y = int(input())
    trian.z = int(input())
except ValueError as e:
    print(e)
    exit()

if trian.is_triangle():
    print('Ура, можно построить треугольник!')
else:
    print('Жаль, но из этого треугольник не сделать.')