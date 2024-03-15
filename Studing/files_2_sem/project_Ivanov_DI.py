#pip3 install pygame
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

    _X_max = 11
    _Y_max = 21 

    _screen_x = 300 
    _screen_y = 600 

    _screen = pygame.display.set_mode((_screen_x, _screen_y))
    pygame.display.set_caption("Tetris. project Ivanov")
    fps = 90 

class Cell:
    _dx = Window._screen_x/(Window._X_max - 1)
    _dy = Window._screen_y/(Window._Y_max - 1)

    grid = [] 

    for i in range(0, Window._X_max):
        grid.append([])
        for j in range(0, Window._Y_max):
            grid[i].append([1])

    for i in range(0, Window._X_max):
        for j in range(0, Window._Y_max): 
            grid[i][j].append(pygame.Rect(i*_dx, j*_dy, _dx, _dy))
            grid[i][j].append(pygame.Color("red"))

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


class Entity:

    det = [[],[],[],[],[],[],[]]
    for i in range(0, len(Det.details)):
        for j in range(0, 4):
            det[i].append(pygame.Rect(Det.details[i][j][0]*Cell._dx + Cell._dx*(Window._X_max//2), Det.details[i][j][1]*Cell._dy, Cell._dx, Cell._dy))

    detail = pygame.Rect(0, 0, Cell._dx, Cell._dy)
    det_choice = copy.deepcopy(random.choice(det))

class Game:
    count = 0
    game = True
    rotate = False
    while game:
        delta_x = 0
        delta_y = 1
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
        if key[pygame.K_DOWN]:
            count = 31 * Window.fps

        Window._screen.fill(pygame.Color("Indigo"))

        for i in range(0, Window._X_max):
            for j in range(0, Window._Y_max):
                pygame.draw.rect(Window._screen, Cell.grid[i][j][2], Cell.grid[i][j][1], Cell.grid[i][j][0])

        for i in range(4):
            if ((Entity.det_choice[i].x + delta_x * Cell._dx < 0) or (Entity.det_choice[i].x + delta_x * Cell._dx >= Window._screen_x)):
                delta_x = 0
            if ((Entity.det_choice[i].y + Cell._dy >= Window._screen_y) or (Cell.grid[int(Entity.det_choice[i].x//Cell._dx)][int(Entity.det_choice[i].y//Cell._dy) + 1][0] == 0)):
                delta_y = 0
                for i in range(4):
                    x = int(Entity.det_choice[i].x // Cell._dx)
                    y = int(Entity.det_choice[i].y // Cell._dy)
                    Cell.grid[x][y][0] = 0
                    Cell.grid[x][y][2] = pygame.Color("red")
                Entity.detail.x = 0
                Entity.detail.y = 0
                Entity.det_choice = copy.deepcopy(random.choice(Entity.det))

        for i in range(4):
            Entity.det_choice[i].x += delta_x*Cell._dx

        count += Window.fps
        if count > 30 * Window.fps:
            for i in range(4):
                Entity.det_choice[i].y += delta_y*Cell._dy
            count = 0

        for i in range(4):
            Entity.detail.x = Entity.det_choice[i].x
            Entity.detail.y = Entity.det_choice[i].y
            pygame.draw.rect(Window._screen, pygame.Color("red"), Entity.detail)


        C = Entity.det_choice[2]
        if rotate == True:
            for i in range(4):
                x = Entity.det_choice[i].y - C.y
                y = Entity.det_choice[i].x - C.x

                Entity.det_choice[i].x = C.x - x
                Entity.det_choice[i].y = C.y + y
            rotate = False



        for j in range(Window._Y_max - 1, -1, -1): 
            count_cells = 0
            for i in range(0, Window._X_max):
                if Cell.grid[i][j][0] == 0:
                    count_cells += 1
                elif Cell.grid[i][j][0] == 1:
                    break
            if count_cells == (Window._X_max - 1):
                for l in range(0, Window._X_max):
                    Cell.grid[l][0][0] = 1 
                for k in range(j, -1, -1):
                    for l in range(0, Window._X_max):
                        Cell.grid[l][k][0] = Cell.grid[l][k-1][0]

        pygame.display.flip()
        pygame.time.Clock().tick(Window.fps)