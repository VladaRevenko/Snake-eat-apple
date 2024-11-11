import pygame as pg


class Apple:
    def __init__(self, width, height, x, y):
        self.x = x
        self.y = y
        self.image = pg.image.load("ЯБЛОКО.png")
        self.image = pg.transform.scale(self.image, (width, height))

    def draw(self, screen: pg.Surface, cells: dict[tuple[int, int], pg.Rect]):
        cell = cells[self.x, self.y]
        screen.blit(self.image,(cell.x, cell.y))

