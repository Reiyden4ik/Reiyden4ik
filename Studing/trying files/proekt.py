import pygame
import random
import copy

pygame.init()

class Window:

    def __init__(self, I_max, J_max, screen_x, screen_y):
        self._X_max = I_max
        self._Y_max = J_max
        self._screen_x = screen_x
        self._screen_y = screen_y

    _X_max = 11 # количество клеток по x
    _Y_max = 21 # количество клеток по y

    _screen_x = 300 # параметр экрана
    _screen_y = 600 # параметр экрана

    _screen = pygame.display.set_mode((_screen_x, _screen_y)) # сам экран
    pygame.display.set_caption("Тетрис. Made by Ivanov") # имя экрана
    fps = 90 # частота обновления экрана

class Cell:
    # ширина и высота каждой ячейки нашей сетки. -1, т. к. количество точек на единицу меньше количества ячеек
    _dx = Window._screen_x/(Window._X_max - 1)
    _dy = Window._screen_y/(Window._Y_max - 1)

    grid = [] # список параметров сеток в окне

    # пройтись по всем элементам сетки и добавить список
    for i in range(0, Window._X_max):
        grid.append([])
        for j in range(0, Window._Y_max):
            grid[i].append([1])

    # заполняем списки с сущностями прямоугольника
    for i in range(0, Window._X_max):
        for j in range(0, Window._Y_max): 
            grid[i][j].append(pygame.Rect(i*_dx, j*_dy, _dx, _dy)) # список для каждой ячеки в сетке, 1, сущность прямоугольника в координатах
            grid[i][j].append(pygame.Color("White")) # цвет полосок

# фигуры кубиков. Не менять так как будет не по центру падать
class Det():
    details = [
        [[-2, 0], [-1, 0], [0, 0], [1, 0]],
        [[-1, 1], [-1, 0], [0, 0], [1, 0]],
        [[1, 1], [-1, 0], [0, 0], [1, 0]],
        [[-1, 1], [0, 1], [0, 0], [-1, 0]],
        [[1, 0], [1, 1], [0, 0], [-1, 0]],
        [[0, 1], [-1, 0], [0, 0], [1, 0]],
        [[-1, 1], [0, 1], [0, 0], [1, 0]],
    ]

# список с сущностями деталей
class Entity:

    det = [[],[],[],[],[],[],[]]
    for i in range(0, len(Det.details)):
        for j in range(0, 4):
            # координаты умножаем на шаг и ставим сверху по центру
            det[i].append(pygame.Rect(Det.details[i][j][0]*Cell._dx + Cell._dx*(Window._X_max//2), Det.details[i][j][1]*Cell._dy, Cell._dx, Cell._dy))

    detail = pygame.Rect(0, 0, Cell._dx, Cell._dy)
    det_choice = copy.deepcopy(random.choice(det)) # копия деталей из списка

class Game:
    count = 0
    game = True
    rotate = False
    while game:
        delta_x = 0
        delta_y = 1
        # движение влево-вправо и выход для клавиш
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -1
                elif event.key == pygame.K_RIGHT:
                    delta_x = 1
                elif event.key == pygame.K_UP:
                    rotate = True

        key = pygame.key.get_pressed()
        # ускорение вниз
        if key[pygame.K_DOWN]:
            count = 31 * Window.fps

        Window._screen.fill(pygame.Color("Gray")) #цвет фона

        for i in range(0, Window._X_max):
            for j in range(0, Window._Y_max):
                pygame.draw.rect(Window._screen, Cell.grid[i][j][2], Cell.grid[i][j][1], Cell.grid[i][j][0]) # рисуем каждый квадрат сетки

        #границы
        for i in range(4):
            if ((Entity.det_choice[i].x + delta_x * Cell._dx < 0) or (Entity.det_choice[i].x + delta_x * Cell._dx >= Window._screen_x)): # лево-право
                delta_x = 0
            if ((Entity.det_choice[i].y + Cell._dy >= Window._screen_y) or (Cell.grid[int(Entity.det_choice[i].x//Cell._dx)][int(Entity.det_choice[i].y//Cell._dy) + 1][0] == 0)): # нижняя грань
                delta_y = 0
                for i in range(4):
                    # индексы для закрашивания клеток
                    x = int(Entity.det_choice[i].x // Cell._dx)
                    y = int(Entity.det_choice[i].y // Cell._dy)
                    Cell.grid[x][y][0] = 0 #закрашиваем квадратик
                    Cell.grid[x][y][2] = pygame.Color("White") # цвет клетки внизу
                Entity.detail.x = 0
                Entity.detail.y = 0
                Entity.det_choice = copy.deepcopy(random.choice(Entity.det)) # копия деталей из списка

        #передвижение по x
        for i in range(4):
            Entity.det_choice[i].x += delta_x*Cell._dx

        count += Window.fps
        #передвижение по y
        if count > 30 * Window.fps: # чтобы быстро не улетало
            for i in range(4):
                Entity.det_choice[i].y += delta_y*Cell._dy
            count = 0

        # границы деталей
        for i in range(4):
            Entity.detail.x = Entity.det_choice[i].x
            Entity.detail.y = Entity.det_choice[i].y
            pygame.draw.rect(Window._screen, pygame.Color("White"), Entity.detail) # цвет клетки

        # поворот
        C = Entity.det_choice[2] #центр СК
        if rotate == True:
            for i in range(4):
                x = Entity.det_choice[i].y - C.y
                y = Entity.det_choice[i].x - C.x

                Entity.det_choice[i].x = C.x - x
                Entity.det_choice[i].y = C.y + y
            rotate = False


        # для сноса нижней ячейки
        for j in range(Window._Y_max - 1, -1, -1): #цикл по рядам снизу вверх
            count_cells = 0
            for i in range(0, Window._X_max): #цикл по столбцам справа налево
                if Cell.grid[i][j][0] == 0:
                    count_cells += 1
                elif Cell.grid[i][j][0] == 1:
                    break
            if count_cells == (Window._X_max - 1):
                for l in range(0, Window._X_max):
                    Cell.grid[l][0][0] = 1 #все ячейки первого ряда
                for k in range(j, -1, -1):
                    for l in range(0, Window._X_max):
                        Cell.grid[l][k][0] = Cell.grid[l][k-1][0] # смещение вниз

        pygame.display.flip()
        pygame.time.Clock().tick(Window.fps)