# Импорт библиотек
import pygame
import random
pygame.init()

# Основные параметры
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode([screen_width, screen_height])
obj_num = 150  # Количество объектов
obj_type = 'камень'
obj_size = 30  # Размер объекта
speed = 0

# Создаем список объектов и заполняем его: 0 - x, 1 - y, 2 - тип объекта
obj_list = []
i = 0
for i in range(obj_num):
    x, y = random.randrange(screen_width), random.randrange(screen_height)
     
    # По равному количеству каждого объекта
    if obj_num // 3 - 1 < i < (obj_num // 3) * 2 - 1:
        obj_type = 'ножницы'
    elif i >= (obj_num // 3) * 2:
        obj_type = 'бумага'
    obj_list.append([x, y, obj_type])

# Загрузка изображений КНБ
rock_img, scissor_img, paper_img = pygame.image.load("img/rock.png").convert(
), pygame.image.load("img/scissor.png").convert(), pygame.image.load("img/paper.png").convert()
rock_img = pygame.transform.scale(rock_img, (obj_size, obj_size))
rock_img.set_colorkey((0, 0, 0))
scissor_img = pygame.transform.scale(scissor_img, (obj_size, obj_size))
scissor_img.set_colorkey((0, 0, 0))
paper_img = pygame.transform.scale(paper_img, (obj_size, obj_size))
paper_img.set_colorkey((0, 0, 0))

# Пуск до выхода пользователя
running = True
while running:

    # Нажат крестик выхода?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Фон
    screen.fill((100, 100, 100))

    # Время игры, подумаем
    pygame.time.delay(speed)

    i = 0
    j = 0
    dist = 0

    for i in range(obj_num):
        for j in range(i + 1, obj_num):
            # Измеряем расстояние между каждой парой объектов
            dist = int((abs(obj_list[j][1] - obj_list[i][1]) **
                        2 + abs(obj_list[j][0] - obj_list[i][0]) ** 2) ** 0.5)

            # Если столкнулись
            if dist < obj_size // 2:
                if obj_list[i][2] == 'камень':
                    if obj_list[j][2] == 'ножницы':
                        obj_list[j][2] = 'камень'
                    if obj_list[j][2] == 'бумага':
                        obj_list[i][2] = 'бумага'

                elif obj_list[i][2] == 'ножницы':
                    if obj_list[j][2] == 'камень':
                        obj_list[i][2] = 'камень'
                    if obj_list[j][2] == 'бумага':
                        obj_list[j][2] = 'ножницы'

                elif obj_list[i][2] == 'бумага':
                    if obj_list[j][2] == 'ножницы':
                        obj_list[i][2] = 'ножницы'
                    if obj_list[j][2] == 'камень':
                        obj_list[j][2] = 'бумага'
    # Рисовка объектов
    for obj in obj_list:
        if obj[2] == 'камень':
            screen.blit(
                rock_img, (obj[0] - obj_size // 2, obj[1] - obj_size // 2))
        elif obj[2] == 'ножницы':
            screen.blit(
                scissor_img, (obj[0] - obj_size // 2, obj[1] - obj_size // 2))
        elif obj[2] == 'бумага':
            screen.blit(
                paper_img, (obj[0] - obj_size // 2, obj[1] - obj_size // 2))

        # Меняем координаты, видимо правое значение не входит
        obj[0] += random.randrange(-5, 6)
        obj[1] += random.randrange(-5, 6)

        # Заехал за границы?
        if obj[0] < 0:
            obj[0] = 0
        if obj[1] < 0:
            obj[1] = 0
        if obj[0] > screen_width:
            obj[0] = screen_width
        if obj[1] > screen_height:
            obj[1] = screen_height

    # Всё на экран
    pygame.display.flip()

# Выход
pygame.quit()
