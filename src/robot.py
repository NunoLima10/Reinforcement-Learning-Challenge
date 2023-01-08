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
        distance = self.map.distance_to_goal_state(new_cell)
        is_goal_state = distance == 0 
        reward = 0 if is_goal_state else 1 /distance * 10
        return  (is_goal_state,  reward)
            
       
    def steps(self, direction_list: list[Directions]) -> None:
        pass
    
    def random_step(self) -> tuple[bool, float]:
        valid_moves  = self.map.get_valid_moves(self.current_cell)
        if valid_moves:
            return self.step(random.choice(valid_moves))
        return (False, 0)  
    
    def update(self) -> None:
        pass

    def draw(self, surface) -> None:
        pg.draw.circle(surface,self.color, self.current_cell.center,self.map.cell_size / 4)

    def __repr__(self) -> str:
        return f"<Robot object color = {self.color}>"
      
