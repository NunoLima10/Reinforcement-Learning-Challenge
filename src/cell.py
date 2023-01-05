from collections import namedtuple
import pygame as pg


class Cell:
    cell_info = namedtuple("cell_inf","color char")
    cell_types = {
    "wall":cell_info( (0, 0, 0,) ,"#"),
    "space":cell_info( (255, 255, 255) ,"-")
    }

    def __init__(self, cell_size: int, cell_char: str, position: tuple) -> None:
        self.cell_size = cell_size
        self.position = position
        self.row_index = int(position[0] / cell_size)
        self.column_index = int(position[1] / cell_size)
        self.rect = (position, (cell_size, cell_size))
        self.cell_info = self.get_cell_info(cell_char)
        
    @property
    def center(self) -> tuple:
        return (self.position[0] + self.cell_size/2 , self.position[1] + self.cell_size/2)
    
    def get_cell_info(self, cell_char: str) -> dict:
        for key, cell_info in self.cell_types.items():
            if cell_info.char == cell_char:
                return self.cell_types[key]
        return None

    def draw(self, surface) -> None:
        pg.draw.rect(surface, self.cell_info.color, self.rect)

    def __repr__(self) -> str:
        return f"<Cell object position = {self.position} cell_info = {self.cell_info}"
        

        