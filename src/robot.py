from src.cell import Cell
import pygame as pg

class Robot:
    def __init__(self, inicial_cell: Cell) -> None:
        self.inicial_cell = inicial_cell

        # self.rect = (inicial_position, (cell_size, cell_size))

    
    def update(self) -> None:
        pass

    def draw(self, surface) -> None:
        pg.draw.circle(surface,(255,0,0), self.inicial_cell.center,self.inicial_cell.cell_size/4)
        # pg.draw.rect(surface, (255,0,0), self.rect)
