from src.cell import Cell
from src.direction import Directions

import pygame as pg
import math
class Map:
    def __init__(self, cell_size: int, file_path: str) -> None:
        self.cell_size = cell_size
        self.file_path = file_path
        self.robot_inicial_cell: Cell = None
        self.robot_char = "R"
        self.goal_state_reward = 100
        
        self.map = self.load_map()
        
        self.rows = len(self.map[0])
        self.columns = len(self.map)

        self.width = self.rows * cell_size
        self.height =  self.columns * cell_size

        self.show_grid = True
        self.grid_color = (0,0,0)
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
            x_end = self.width
            start_point = (x_start, y_start)
            end_point = (x_end, y_start)
            lines.append((start_point, end_point))
        return lines
        
    def load_map(self) -> list:
        with open(self.file_path,"r") as file:
            content = file.readlines()
        map = []
        id = 0
        for column_index, line in enumerate(content):
            row = []
            for row_index, cell_char in enumerate(line):
                if cell_char == '\n':
                    continue
                position = (row_index * self.cell_size, column_index * self.cell_size)

                if cell_char == self.robot_char:
                    self.robot_inicial_cell = Cell(id,self.cell_size, cell_char, position)
                    cell_char = Cell.cell_types["space"].char
                
                if cell_char == Cell.cell_types["goal_state"].char:
                    self.goal_state = Cell(id,self.cell_size, cell_char, position)
               
                cell = Cell(id,self.cell_size, cell_char, position)
                row.append(cell)
                id += 1
            map.append(row)
        return map
    
    def is_valid_position(self, x, y) -> bool:
        return x >= 0 and y >= 0 and x < self.rows and y <  self.columns 
    
    def move(self, cell: Cell, direction: Directions) -> Cell:
        new_position_x = cell.row_index + direction.x
        new_position_y = cell.column_index + direction.y

        if not self.is_valid_position(new_position_x, new_position_y):
            return None

        new_cell = self.map[new_position_y][new_position_x]

        if new_cell.cell_info == Cell.cell_types["wall"]:
            return None

        return new_cell

    def get_valid_moves(self, cell: Cell) -> list[Directions]:
        directions = [Directions.NORTH, Directions.SOUTH, Directions.WEST, Directions.EAST]
        return [direction for direction in directions if self.move(cell, direction) is not None]

    def normalize(self, position) -> tuple:
        return ((position[0] /self.width),position[1] /self.height)

    def get_reward(self, cell: Cell) -> float:
        distance = math.dist(self.normalize(cell.position), self.normalize(self.goal_state.position))
        return  0 if distance else self.goal_state_reward

    def is_goal_state(self, cell: Cell) -> bool:
        return cell.position == self.goal_state.position

    def draw(self, surface: pg.Surface) -> None:
        for row in  self.map:
            for cell in row:
                cell.draw(surface)
                      
        if self.show_grid:
            for line in self.lines:
                pg.draw.line(surface, self.grid_color, line[0], line[1])

    def __repr__(self) -> str:
        return f"<Map object cell_size = {self.cell_size} file_path = {self.file_path}>"   
            
