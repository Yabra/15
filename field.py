# начальное размещение
#   1     2     3     4
# [1,1] [2,1] [3,1] [4,1]
#
#   5     6     7     8
# [1,2] [2,2] [3,2] [4,2]
#
#   9    10    11    12
# [1,3] [2,3] [3,3] [4,3]
#
#  13    14    15    x
# [1,4] [2,4] [3,4] [4,4]

import random
from tile import Tile


class Field:

    def __init__(self):
        self.tile_size = 100    # размер костяшки
        self.slit = 5           # размер зазора между костяшками
        
        # отступы от края экрана, откуда начинаем расставлять костяшки
        self.tiles_start_x = 20
        self.tiles_start_y = 20
        
        # начальная позиция дырки
        self.space_x = 4
        self.space_y = 4

        # массив костяшек...
        self.tiles = []

        # ...заполняем
        number = 1
        y = 1
        while y < 5:
            x = 1
            while x < 5:
                if number < 16:
                    tile = Tile(number, x, y)
                    self.tiles.append(tile)
                number = number + 1
                x = x + 1

            y = y + 1

        # свойства используемые для анимации
        self.animating = False  # анимируется
        self.speed = 15         # скорость смещения
        self.diff_x = 0         # смещение по оси X в пикселях
        self.diff_y = 0         # смещение по оси Y в пикселях

        self.shuffle()

    def shuffle(self):
        pass
     # todo переписать
        self.right(2)
        self.down(1)
        self.left(4)
        self.up(2)

        self.animation_end()

    # возвращает необходимую для отрисовки костяшек информацию
    # [
    #   {'image': image, 'coords': [x, y]},
    #   ...
    # ]
    def get_tiles_for_draw(self):
        out = []
        for tile in self.tiles:
            info_for_draw = {
                'image': tile.image,
                'coords': self.calc_coords(tile)
            }
            out.append(info_for_draw)

        return out

    def animation_start(self, direction):
        diff = self.tile_size + self.speed

        if direction == "done":
            self.diff_y = diff * (-1)
        elif direction == "up":
            self.diff_y = diff
        elif direction == "right":
            self.diff_x = diff * (-1)
        elif direction == "left":
            self.diff_x = diff
        else:
            print("Direction Error")

        self.animating = True

    def animation(self):
        if (
            abs(self.diff_x) <= self.speed
            and
            abs(self.diff_y) <= self.speed
        ):
            self.animation_end()

        if self.diff_x != 0:
            if self.diff_x > 0:
                self.diff_x = self.diff_x - self.speed
            elif self.diff_x < 0:
                self.diff_x = self.diff_x + self.speed
        elif self.diff_y != 0:
            if self.diff_y > 0:
                self.diff_y = self.diff_y - self.speed
            elif self.diff_y < 0:
                self.diff_y = self.diff_y + self.speed

    def animation_end(self):
        self.diff_x = 0
        self.diff_y = 0
        self.animating = False
        for tile in self.tiles:
            tile.animate = False

    # возвращает массив координат для отрисовки костяшки
    def calc_coords(self, tile):
        x_pos = tile.x
        x = (x_pos - 1) * self.tile_size + self.tiles_start_x + (x_pos - 1) * self.slit
        y_pos = tile.y
        y = (y_pos - 1) * self.tile_size + self.tiles_start_y + (y_pos - 1) * self.slit

        if tile.animate == True:
            x = x + self.diff_x
            y = y + self.diff_y

        return [x, y]

    # смещение костяшек вниз
    def down(self, y_pos):
        self.animation_start("done")
        count = self.space_y - y_pos
        for tile in self.tiles:
            if tile.x == self.space_x and y_pos <= tile.y and tile.y < self.space_y:
                tile.down()
        self.space_y = self.space_y - count

    # смещение костяшек вверх
    def up(self, y_pos):
        self.animation_start("up")
        count = y_pos - self.space_y
        for tile in self.tiles:
            if tile.x == self.space_x and y_pos >= tile.y and tile.y > self.space_y:
                tile.up()
        self.space_y = self.space_y + count

    # смещение костяшек вправо
    def right(self, x_pos):
        self.animation_start("right")
        count = self.space_x - x_pos
        for tile in self.tiles:
            if tile.y == self.space_y and x_pos <= tile.x and tile.x < self.space_x:
                tile.right()
        self.space_x = self.space_x - count

    # смещение костяшек влево
    def left(self, x_pos):
        self.animation_start("left")
        count = x_pos - self.space_x
        for tile in self.tiles:
            if tile.y == self.space_y and x_pos >= tile.x and tile.x > self.space_x:
                tile.left()
        self.space_x = self.space_x + count


    # метод получает координаты клика мышкой - coords (кортеж)
    # получает позицию костяшки в которую попал игрок (calc_tile_pos())
    # и если возможно сделать передвижение костяшек,
    # то запускает перемещение используя методы: down(), up(), right(), left()
    def try_turn(self, coords):
        x_pos, y_pos = self.calc_tile_pos(coords)
        if self.turn_accessibility(x_pos, y_pos) != True:
            return

        if x_pos == self.space_x:
            if y_pos < self.space_y:
                self.down(y_pos)
            elif y_pos > self.space_y:
                self.up(y_pos)
        if y_pos == self.space_y:
            if x_pos > self.space_x:
                self.left(x_pos)
            elif x_pos < self.space_x:
                self.right(x_pos)

        if self.check_win():
            self.win()

    def calc_tile_pos(self, coords):
        x = coords[0]
        x_pos = (x - self.tiles_start_x) // (self.tile_size + self.slit) + 1
        y = coords[1]
        y_pos = (y - self.tiles_start_y) // (self.tile_size + self.slit) + 1
        return x_pos, y_pos

    def turn_accessibility(self, x_pos, y_pos):
        if (
            self.animating == True
            or x_pos < 1 or x_pos > 4 or y_pos < 1 or y_pos > 4
            or (self.space_x == x_pos and self.space_y == y_pos)
            or (self.space_x != x_pos and self.space_y != y_pos)
        ):
            return False
        else:
            return True

    # проверяет не выиграл ли игрок
    # для этого перебираем все костяшки и сравниваем их текущую позицию
    # с победной позицией (win_x, win_y)
    def check_win(self):
        for tile in self.tiles:
            if not tile.in_win_position():
                return False

        return True

    def get_size(self):
        size_x = self.tile_size * 4 + self.slit * 3 + self.tiles_start_x * 2
        size_y = self.tile_size * 4 + self.slit * 3 + self.tiles_start_y * 2
        return (size_x, size_y)

    def win(self):
        print("You are win!")
