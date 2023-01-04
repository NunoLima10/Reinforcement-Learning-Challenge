from src.cell import Cell
from src.map import Map
from src.direction import Directions
import pygame as pg

class Robot:
    def __init__(self, game_map: Map) -> None:
        self.map = game_map
        self.inicial_cell = self.map.robot_inicial_cell
        self.current_cell = self.map.robot_inicial_cell

        #default
        self.color = (255,0,0)

    def step(self, direction: Directions) -> None:
        new_cell = self.map.move(self.current_cell, direction)

        if new_cell is not None:
            self.current_cell =  new_cell

    def update(self) -> None:
        pass

    def draw(self, surface) -> None:
        pg.draw.circle(surface,self.color, self.current_cell.center,self.map.cell_size / 4)
      
