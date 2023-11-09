import re

string = str(input('Регистрационный номер авто:'))
pattern1 = r"\w[АВЕКМНОРСТУХ]\w[АВЕКМНОРСТУХ]\d\d\d\w[АВЕКМНОРСТУХ]\d\d"
pattern2 = r"\w[АВЕКМНОРСТУХ]\w[АВЕКМНОРСТУХ]\d\d\d\w[АВЕКМНОРСТУХ]\w[АВЕКМНОРСТУХ]"
if re.fullmatch(pattern1, string):
    print("Частный автомобиль")
elif re.fullmatch(pattern2, string):
    print("Такси Марсель")
else: print("Введите правильно")

