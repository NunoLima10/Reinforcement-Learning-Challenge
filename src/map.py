from src.cell import Cell
from src.direction import Directions

import pygame as pg

class Map:
    def __init__(self, cell_size: int, file_path: str) -> None:
        self.cell_size = cell_size
        self.file_path = file_path
        self.robot_inicial_cell: Cell = None
        self.map = self.load_map()

        self.rows = len(self.map[0])
        self.columns = len(self.map)

        self.width = self.rows * cell_size
        self.height =  self.columns * cell_size

        self.show_grid = True
        self.lines = self.generate_grid_lines()

    def valide_map(self, map: list[list]) -> bool:
        pass
    
    def generate_grid_lines(self) -> None:
        
        lines = []
        for i in range(1,self.rows):
            x_start =  i * self.cell_size
            y_start = 0
            y_end = self.height
            start_point = (x_start, y_start)
            end_point = (x_start, y_end)
            lines.append((start_point, end_point))

        for i in range(1,self.columns):
            x_start = 0
            y_start = i *  self.cell_size
            x_end = x_start + self.width

            start_point = (x_start, y_start)
            end_point = (x_end, y_start)
            lines.append((start_point, end_point))

        return lines
        
    def load_map(self) -> list:
        with open(self.file_path,"r") as file:
            content = file.readlines()
        map = []
        for column_index, line in enumerate(content):
            row = []
            for row_index, cell_type in enumerate(line):
                if cell_type == '\n':
                    continue

                position = (row_index * self.cell_size, column_index * self.cell_size)
                if cell_type == "R":
                    cell_type = "-"
                    self.robot_inicial_cell = Cell(self.cell_size, cell_type, position)
               
                cell = Cell(self.cell_size, cell_type, position)
                row.append(cell)
            map.append(row)
        return map
    
    def get_valid_moves(self, position: tuple) -> list[Directions]:
        pass

    
    def draw(self, surface: pg.Surface) -> None:
        for row in  self.map:
            for cell in row:
                cell.draw(surface)
                      
        if self.show_grid:
            for line in self.lines:
                pg.draw.line(surface,(0,0,0),line[0],line[1])

                
                   
            
