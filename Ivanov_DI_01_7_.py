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
print(lw('C:/Users/maksim/Downloads/Ivanov_DI_01_7.py'))


#Составьте программу - простейший редактор текстовых файлов. 
# Алгоритм работы программы: Программа предлагает ввести имя будущего файла. 
# Записывает его, присваивая расширение .txt. Программа предлагает записать строку в файл. 
# При каждом нажатии кнопки ENTER происходит запись строки и переход на новую строчку. 
# Если строка пустая или спец. символ - программа сохраняет файл.

import re

nameFile = input("Введите название поста: \n")
if nameFile:
    file = open("/workspaces/Reiyden4ik/files/" + nameFile + ".txt", "w")
    while True:
        wr = input('Write: ')
        file.write(wr + '\n')
        if not wr:
            break
    file.close()
