#Документ article.txt содержит следующий текст:
#Вечерело
#Жужжали мухи
#Светил фонарик
#Кипела вода в чайнике
#Венера зажглась на небе
#Деревья шумели
#Тучи разошлись
#Листва зеленела
#Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).


def lw(file):
    with open(file, encoding='utf-8') as text:
        w = text.read().split()
        ml = len(max(w, key=len))
        sw = [word for word in w if len(word) == ml]
        if len(sw) == 1:
            return sw[0]
        return sw
print(lw('/workspaces/Reiyden4ik/files/article.txt'))


#Составьте программу - простейший редактор текстовых файлов. 
# Алгоритм работы программы: Программа предлагает ввести имя будущего файла. 
# Записывает его, присваивая расширение .txt. Программа предлагает записать строку в файл. 
# При каждом нажатии кнопки ENTER происходит запись строки и переход на новую строчку. 
# Если строка пустая или спец. символ - программа сохраняет файл.

import re

nameFile = input("Введите название поста: \n")
forbidden_symbols = "\\|/*<>?:"
pattern = '[{0}]'.format(forbidden_symbols)
if not(re.search(pattern, nameFile)):
    file = open("/workspaces/Reiyden4ik/files/" + nameFile + ".txt", "w")
    while True:
        wr = input('Write: ')
        file.write(wr + '\n')
        if not wr:
            break
    file.close()
else:
    print('Введите корректное название файла.')