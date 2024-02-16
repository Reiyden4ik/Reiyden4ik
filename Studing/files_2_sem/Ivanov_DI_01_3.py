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
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    def is_triangle(self, x, y, z):
        if type(x) in (int, float) and type(y) in (int, float) and type(z) in (int, float):
            self.__x = x
            self.__y = y
            self.__z = z
        else:
            raise ValueError("Нужно вводить только числа!")
        if x+y>z and x+z>y and z+y>x:
            print('Ура, можно построить треугольник!')
        elif x<0 or y<0 or z<0: 
            print('С отрицательными числами ничего не выйдет!')
        else:
            print('Жаль, но из этого треугольник не сделать.')

    def get_value(self):
        return self.__x, self.__y, self.__z
trian = TriangleChecker(0, 0, 0)
trian.is_triangle(20, 20, 30)
