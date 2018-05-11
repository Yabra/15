#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# импортируем необходимые библиотеки
import pygame
import configparser

# импортируем наш класс поля
from field import Field

# инициация PyGame, обязательная строчка
pygame.init()

config = configparser.ConfigParser()
config.read_file(open(r'15.conf'))
field_config = config['field']

# объявляем переменные, которые будем использовать в программе
field = Field(field_config)      # создаём поле
display_size = field.get_size()  # размеры окна
back_color = "#000000"           # цвет фона

screen = pygame.display.set_mode(display_size)  # создаем окно программы
pygame.display.set_caption("Пятнашки")          # название окна
background = pygame.Surface(display_size)       # создание видимой поверхности, будем использовать как фон
background.fill(pygame.Color(back_color))       # заливаем поверхность сплошным цветом

fps = config.getint('main', 'fps')  # задаём количество кадров в секунду
fpsclock = pygame.time.Clock()      # создаём объект который контролирует количество кадров в секунду

running = True

# основной цикл программы
while running:

    for event in pygame.event.get():        # обрабатываем события
        if event.type == pygame.QUIT:           # событие нажатия на крестик (закрытие окна)
            running = False                         # выходим из программы
        if event.type == pygame.MOUSEBUTTONUP:  # событие клик мышью
            field.try_turn(event.pos)               # делаем ход, если это возможно

    field.animation()

    # отрисовываем все элементы игры, начиная с фона,
    # каждую итерацию необходимо всё перерисовывать...
    # ...фон
    screen.blit(background, (0, 0))

    # ...костяшки
    for info in field.get_images_for_draw():
        screen.blit(info['image'], info['coords'])

    # обновление и вывод всех изменений на экран
    pygame.display.update()

    # контроль за количеством кадров в секунду
    fpsclock.tick(fps)
