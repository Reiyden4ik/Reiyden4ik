#1. Создать объект pandas Series из листа, объекта NumPy, и словаря
import pandas as pd
import numpy as np
slist = list('abcde')
sarr = np.arange(5)
sdict = dict(zip(slist, sarr))
ser1 = pd.Series(slist)
ser2 = pd.Series(sarr)
ser3 = pd.Series(sdict)
print(ser1)
print(ser2)
print(ser3)

#2. Получить не пересекающиеся элементы в двух объектах Series
import numpy as np
import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([4, 5, 6, 7, 8])
s_unity = pd.Series(np.union1d(s1, s2))
ssl = pd.Series(np.intersect1d(s1, s2))
a = s_unity[~s_unity.isin(ssl)]
a2 = np.setxor1d(s1, s2, assume_unique=False)
print(a)

#3. Узнать частоту уникальных элементов объекта Series (гистограмма)
import numpy as np
import pandas as pd
data = str(input("Введите строку:"))
series = int(input("Укажите размер:"))
k = pd.Series(np.take(list(data), np.random.randint(len(data), size=series)))
ans = k.value_counts()
print(ans)

#4. Объединить два объекта Series вертикально и горизонтально
import pandas as pd
r1 = pd.Series(range(5))
r2 = pd.Series(list('abcde'))
av = r1._append(r2)
ah = pd.concat([r1, r2], axis=1)
print(av)
print(ah)

#5. Найти разность между объектом Series и смещением объекта Series на n
import pandas as pd
n = int(input("Введите число:"))
s = pd.Series([1, 5, 7, 8, 12, 15, 17])
v = s.diff(periods=n)
print(v)