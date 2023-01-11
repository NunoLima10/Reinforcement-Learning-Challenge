from src.map import Map
from src.direction import Directions

import pygame as pg
import random

class Robot:
    def __init__(self, game_map: Map) -> None:
        self.map = game_map
        self.inicial_cell = self.map.robot_inicial_cell
        self.current_cell = self.map.robot_inicial_cell

        #default
        self.color = (255,0,0)

    def step(self, direction: Directions) -> tuple[bool, float]:
        new_cell = self.map.move(self.current_cell, direction)
        if new_cell is None:
            return(False, 0)

        self.current_cell =  new_cell
        return(self.map.is_goal_state(new_cell),  self.map.get_reward(new_cell))
            
    def random_step(self) -> tuple[bool, float]:
        valid_moves  = self.map.get_valid_moves(self.current_cell)
        move = random.choice(valid_moves)
        return self.step(move) if valid_moves else (False, 0)
    
    def update(self) -> None:
        pass

    def check_events(self, key) -> None:
        if key == pg.K_UP:
            _, reward = self.step(Directions.NORTH)
        elif key == pg.K_DOWN:
             _, reward = self.step(Directions.SOUTH)
        elif key == pg.K_LEFT:
            _, reward = self.step(Directions.WEST)
        elif key == pg.K_RIGHT:
            _, reward = self.step(Directions.EAST)

        print(f"reward: {reward}")

    def draw(self, surface) -> None:
        pg.draw.circle(surface,self.color, self.current_cell.center,self.map.cell_size / 4)

    def __repr__(self) -> str:
        return f"<Robot object color = {self.color}>"
      
