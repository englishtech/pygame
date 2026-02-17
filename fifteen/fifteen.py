# Импорт библиотек
import pygame
from random import shuffle
pygame.init()

# Основные параметры
time = 60
cell_size = 100
counter = 0
screen = pygame.display.set_mode([cell_size * 4, cell_size * 4])

# Создаем список пятнашек и перемешиваем его
fifteen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
shuffle(fifteen)

# Создаем список [номер пятнашки, x, y]
coords = []
cell = []
for i in range(1, 5):
    for j in range(1, 5):
        coords.append([cell_size * j - cell_size // 2,
                      cell_size * i - cell_size // 2])
for a in range(0, 16):
    cell.append([fifteen[a], coords[a]])

# Функция рисования черточек досочки


def draw_board():
    for i in range(1, 4):
        pygame.draw.line(screen, (0, 0, 0), (cell_size * i, 0),
                         (cell_size * i, cell_size * 4), width=3)
        pygame.draw.line(screen, (0, 0, 0), (0, cell_size * i),
                         (cell_size * 4, cell_size * i), width=3)


# Задаем шрифтик пятнашек
font = pygame.font.SysFont('serif', cell_size // 2)
font_counter = pygame.font.SysFont('serif', cell_size // 5)

# Пуск до выхода пользователя
running = True
while running:

    # Нажат крестик выхода?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter += 1
            # Проверяем в какую клеточку нажат курсорчик
            for i in range(0, 16):
                if event.pos[0] < cell[i][1][0] + cell_size // 2 and event.pos[0] > cell[i][1][0] - cell_size // 2 and event.pos[1] < cell[i][1][1] + cell_size // 2 and event.pos[1] > cell[i][1][1] - cell_size // 2:
                    pressed_cell = i
            # Проверяем - если нажат рядом с нулевой пятнашечкой, меняемся значениями
            if (abs(cell[pressed_cell][1][0] - cell[zero_cell][1][0]) == cell_size and cell[pressed_cell][1][1] == cell[zero_cell][1][1]) or (abs(cell[pressed_cell][1][1] - cell[zero_cell][1][1]) == cell_size and cell[pressed_cell][1][0] == cell[zero_cell][1][0]):
                cell[zero_cell][0] = cell[pressed_cell][0]
                cell[pressed_cell][0] = 0

    # Фончик
    screen.fill((255, 255, 255))

    # Времечко игры, вроде тут оно нах не нужно
    # pygame.time.delay(time)

    # Рисуем досочку
    draw_board()

    # Рисуем пятнашечки
    for i in range(0, 16):
        text_nums = font.render(str(cell[i][0]), True, (0, 180, 0))
        place = text_nums.get_rect(center=(cell[i][1][0], cell[i][1][1]))
        screen.blit(text_nums, place)
        if cell[i][0] == 0:
            zero_cell = i
            pygame.draw.rect(
                screen, (0, 0, 0), (cell[i][1][0] - cell_size // 2, cell[i][1][1] - cell_size // 2, cell_size, cell_size))

    # Выводим число ходиков
    counter_text = font_counter.render(
        'Ходы: ' + str(counter), True, (150, 150, 150))
    place = counter_text.get_rect(center=(cell_size // 2, 10))
    screen.blit(counter_text, place)

    # Всё на экран
    pygame.display.flip()

# Выход
pygame.quit()
