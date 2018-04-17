#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# импортируем необходимые библиотеки
import pygame
import random
# import time
from pygame import time

# импортируем наши классы поля, и костяшек
from field import Field
from tile import Tile

pygame.init()                                   # инициация PyGame, обязательная строчка

# объявляем переменные, которые будем использовать в программе
field = Field()                 # создаём поле
display_size = field.get_size()  # группируем ширину и высоту в одну переменную
back_color = "#000000"          # цвет фона

screen = pygame.display.set_mode(display_size)  # создаем окно программы
pygame.display.set_caption("Пятнашки")          # название окна
background = pygame.Surface(display_size)       # создание видимой поверхности, будем использовать как фон
background.fill(pygame.Color(back_color))       # заливаем поверхность сплошным цветом

#field.shuffle_start()          # перемешиваем костяшки

fps = 1                        # задаём количество кадров в секунду
fpsclock = pygame.time.Clock()  # создаём объект который контролирует количество кадров в секунду

# cc = 0
running = True
while running:                          # основной цикл программы
    for event in pygame.event.get():        # обрабатываем события
        if event.type == pygame.QUIT:           # событие нажатия на крестик (закрытие окна)
            running = False                         # выходим из программы
        if event.type == pygame.MOUSEBUTTONUP:  # событие клик мышью
            field.try_turn(event.pos)               # делаем ход, если это возможно
        if event.type == pygame.K_F1:
            print("true")
            field.shuffle()

#    if not field.animating and field.shuffling:
#        field.shuffle()

#    field.animate()

    # отрисовываем все элементы игры, начиная с фона, каждую итерацию необходимо всё перерисовывать
    screen.blit(background, (0, 0))                 # фон
    
    for info in field.get_tiles_for_draw():
        screen.blit(info['image'], info['coords'])  # костяшки

    # отладка
    # if not field.animating:
    # if cc == 0:
    #     field.tiles[14].right()
    # elif cc == 1:
    #     field.right(3)
    # elif cc == 2:
    #     field.up(2)
    # elif cc == 3:
    #     field.left(1)
    # elif cc == 4:
    #     running = False

    # cc += 1

    pygame.display.update()         # обновление и вывод всех изменений на экран
    fpsclock.tick(fps)              # контроль за количеством кадров в секунду
