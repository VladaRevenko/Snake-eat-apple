import random

import pygame as pg
from snake import Snake
from apple import Apple


class Field:
    def __init__(self, horizontal: int, vertical: int, width: int, height: int) -> None:
        self.cells = {}
        self.vertical = vertical
        self.horizontal = horizontal
        self.cell_width = width // horizontal
        self.cell_height = height // vertical
        self.field_pixel = pg.image.load("Пиксельная трава.png")
        self.field_pixel = pg.transform.scale(self.field_pixel, (width, height))
        self.sound_apple = pg.mixer.Sound("звук яблоко.mp3")
        # Звук поражения
        self.sound_over = pg.mixer.Sound("Звук поражения.mp3")
        # Добавим все ряды в словарь
        for y in range(0, self.vertical):
            # Добавим ряд в словарь
            for x in range(0, self.horizontal):
                cell = pg.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height)
                self.cells[x, y] = cell
        # Змея
        self.snake = Snake(5, 5, self.cell_width, self.cell_height)
        # Яблоко
        self.apple = Apple(self.cell_width, self.cell_height, random.randint(0, self.horizontal - 1),
                           random.randint(0, self.vertical - 1))

    def update(self):
        # Змейка съела яблоко ?
        if self.snake.y == self.apple.y and self.snake.x == self.apple.x:
            self.apple = Apple(self.cell_width, self.cell_height,
                               random.randint(0, self.horizontal - 1),
                               random.randint(0, self.vertical - 1))
            self.snake.eat_apple = True
            # Включить звук яблоко
            self.sound_apple.play()
        # Движение
        self.snake.move()
        if self.snake.game_over:
            self.sound_over.play()
            pg.time.wait(4000)
            quit()

    def draw(self, screen: pg.Surface):
        screen.blit(self.field_pixel, (0, 0))
        # for key in self.cells:
        #     cell = self.cells[key]
        #     pg.draw.rect(screen, 'green', cell, 1)
        self.apple.draw(screen, self.cells)
        self.snake.draw(screen, self.cells)
