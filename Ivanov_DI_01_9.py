#pip3 install matplotlib
from matplotlib import pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([25, 32, 34, 20, 25])
plt.plot(x, y)
plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
plt.xlim(-10, 10)
plt.title('Первый график') #Название
plt.show()