arr = [[1, 2, 3, 4], [5, 4, 3, 1], [2, 4, 8, 5], [3, 5, 8, 1]]
#Вывод при помощи цикла for и метода join
print('Arrray is ')
for i in arr:
  print(' '.join(list(map(str, i))))
#Пример 1. Подсчет суммы всех элементов
s = 0
for i in range(len(arr)):
  for j in range(len(arr[i])):
    s += arr[i][j]
print('Ex. 1, sum is ', s)
#Пример 2. Подсчет суммы всех элементов
s = 0
for row in arr:
  for element in row:
    s +=element
print('Ex. 2, sum is ', s)
#4 задачи на дом
