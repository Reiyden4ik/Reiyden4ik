import matplotlib.pyplot as plt

# Создаем новый график
fig = plt.figure()

# Добавляем подграфик
ax = fig.add_subplot(111)

# Нарисовать круг
circle = plt.Circle((0, 0), 1, fill = False)
ax.add_artist(circle)

# Установить пределы графика
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Показать график
plt.show()