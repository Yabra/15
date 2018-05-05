import os.path
import pygame


class Tile:
    def __init__(self, number, start_x, start_y):
        self.number = number  # имя костяшки 1-15
        
        # загружаем изображение костяшки исходя из её имени
        file_name = str(number) + '.png'
        file_path = os.path.join('data', file_name)
        self.image = pygame.image.load(file_path)

        # устанавливаем стартовую позицию костяшки
        self.x = start_x
        self.y = start_y
        
        # устанавливаем победную позицию костяшки, она равна стартовой
        self.win_x = start_x
        self.win_y = start_y

        self.animate = False

    # перемещение костяшки вниз
    # перемещение костяшки в любом направлении всегда происходит только на одну позицию, т.к. дырка в поле одна
    def down(self):
        self.y = self.y + 1
        self.animate = True

    # перемещение костяшки вверх
    def up(self):
        self.y = self.y - 1
        self.animate = True

    # перемещение костяшки вправо
    def right(self):
        self.x = self.x + 1
        self.animate = True

    # перемещение костяшки влево
    def left(self):
        self.x = self.x - 1
        self.animate = True

    # возвращает True если позиция костяшки совпадает с победной
    # в противном случае возвращает False
    def in_win_position(self):
        if self.x == self.win_x and self.y == self.win_y:
            return True
        else:
            return False
