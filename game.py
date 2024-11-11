from field import Field
import pygame as pg
from apple import Apple
import random


class Game:
    def __init__(self):
        # Включаем модуль музыки
        pg.mixer.init()
        # Загружаем фоновую музыку и включаем ее
        pg.mixer.music.load("Snake song.mp3")
        pg.mixer.music.play(-1)  # Повторяется постоянно
        # Ширина и высота
        self.width = 1920
        self.height = 1080
        # Кадры в секунду
        self.fps = 60
        # Часы
        self.clock = pg.time.Clock()
        # Поле
        self.field = Field(32, 18, self.width, self.height)
        # Экран
        self.screen = pg.display.set_mode((self.width, self.height))
        # Запущена ли игра ?
        self.running = True

    def mainloop(self):
        # Основной цикл
        while self.running:
            # Тик часов
            self.clock.tick(self.fps)
            # обработать события
            events = pg.event.get()  # Получаем список событий
            for event in events:  # Для каждого события в событиях
                if event.type == pg.QUIT:  # Если тип одного из событий "Выход"
                    self.running = False  # Заканчивает цикл
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False

            # Обновляем поле
            self.field.update()
            # Рисуем поле
            self.field.draw(self.screen)
            pg.display.flip()
