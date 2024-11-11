import pygame as pg


class Snake:
    def __init__(self, x, y, width, height):
        self.x = x  # Координаты головы
        self.y = y
        # Картинка головы
        self.head_image = pg.image.load("Голова змеи (с языком).png")
        self.tail_image = pg.image.load("Часть змеи.png")
        self.head_image = pg.transform.scale(self.head_image, (width, height + height // 2))
        # Словарь картинок головы
        self.head = {
            "up": self.head_image,
            "down": pg.transform.rotate(self.head_image, 180),
            "right": pg.transform.rotate(self.head_image, 270),
            "left": pg.transform.rotate(self.head_image, 90)
        }
        self.tail_image = pg.transform.scale(self.tail_image, (width, height))
        # Хвост
        self.tail = [(self.x, self.y - 1), (self.x, self.y - 2)]
        # Съели яблоко ?
        self.eat_apple = False
        # Счетчик кадров
        self.frames = 0
        self.direction = "down"  # Направление
        # Конец игры ?
        self.game_over = False

    def draw(self, screen, cells: dict[tuple[int, int]: pg.Rect]):
        # pg.draw.rect(screen, 'red', cells[self.x, self.y])
        cell = cells[self.x, self.y]
        if self.direction == 'up':
            x, y = cell.x, cell.y - cell.height // 2
        elif self.direction == 'down':
            x, y = cell.x, cell.y
        elif self.direction == 'left':
            x, y = cell.x - cell.width // 2, cell.y
        else:
            x, y = cell.x, cell.y
        screen.blit(self.head[self.direction], (x, y))
        for part in self.tail:
            # pg.draw.rect(screen, 'white', cells[part])
            cell = cells[part]
            screen.blit(self.tail_image, (cell.x, cell.y))

    def move(self):
        # Получить все нажатые клавиши
        keys = pg.key.get_pressed()
        if keys[pg.K_DOWN] and self.direction != 'up':
            self.direction = 'down'
        elif keys[pg.K_UP] and self.direction != 'down':
            self.direction = 'up'
        elif keys[pg.K_LEFT] and self.direction != 'right':
            self.direction = 'left'
        elif keys[pg.K_RIGHT] and self.direction != 'left':
            self.direction = 'right'
        self.frames += 1
        if self.frames == 3:
            self.frames = 0

            head = (self.x, self.y)
            if self.direction == 'right':
                self.x += 1
            elif self.direction == 'left':
                self.x -= 1
            elif self.direction == 'up':
                self.y -= 1
            else:
                self.y += 1

            # Проверяем GAME OVER
            if self.x == 32 or self.y == 18 or self.x == -1 or self.y == -1:
                self.game_over = True
                return  # Выход из функции
            for i in self.tail:
                if (self.x, self.y) == i:
                    self.game_over = True
                    return

            # Цикл по индексам хвоста
            last_position = head
            for i in range(0, len(self.tail)):
                # Запоминаем позицию хвоста
                pos = self.tail[i]
                self.tail[i] = last_position
                last_position = pos
            if self.eat_apple:
                self.tail.append(last_position)
                self.eat_apple = False
    # def borders(self, vertical, horizontal, cell_height, cell_width):
    #     if vertical > cell_height:
    #         return
    #     if horizontal > cell_width:
    #         return
