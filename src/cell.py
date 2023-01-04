
import pygame as pg

tiles = {
    "#":(0,0,0),
    "-":(255,255,255)
}

class Cell:
    def __init__(self, cell_size: int, cell_type: str, position: tuple) -> None:
        self.cell_size = cell_size
        self.row_index = int(position[0] / cell_size)
        self.column_index = int(position[1] / cell_size)
        self.position = position
        self.rect = (position, (cell_size, cell_size))
        self.cell_type = cell_type
        self.color = tiles[cell_type]

    @property
    def center(self) -> tuple:
        return (self.position[0] + self.cell_size/2 , self.position[1] + self.cell_size/2)

    def draw(self, surface) -> None:
        pg.draw.rect(surface, self.color, self.rect)
        

        