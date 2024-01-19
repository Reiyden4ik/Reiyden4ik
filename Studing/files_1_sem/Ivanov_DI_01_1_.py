#Домашнее задание номер 1 
#1 задание
import math

R = float(input("Чтобы найти площадь круга и длину окружности, введите  радиус:"))

L = 2*math.pi*R
S = math.pi*R*R

L = round(L, 2)
S = round(S, 2)

print("Длина окружности равна:", L)
print("Площадь круга равна:", S)


#2 задание

x = 10
y = 55

print(x, y)

x, y = y, x

print(x, y)

#3 Задание

import math
g = 9.81
L = int(input("Чтобы найти период математичческого маятника, введите его длину:"))

T = 2*math.pi*sqrt(L/g)
T = round(T, 2)

print("Период маятника равен:", T) 

