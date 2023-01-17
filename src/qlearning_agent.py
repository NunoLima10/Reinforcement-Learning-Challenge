from src.cell import Cell
from src.map import Map
from src.direction import Directions
from src.robot import Robot

import random
import time

class QLearningAgent:
    def __init__(self, map: Map, robot: Robot) -> None:
        self.map = map
        self.robot = robot
        self.alpha = 0.2
        self.discount = 0.9
        self.epsilon = 0.1

        self.max_games = 30
        self.max_steps_number = 20_000
        self.steps_number = 0
        self.game_number = 1
        self.game_reward = 0 
        self.rewards = []
        self.space = range(self.max_games)

        self.q_values = self.inicialize_q_values()
        self.start_time = time.time()
        
    def inicialize_q_values(self) -> list[list]:
        return [
            [random.random()  for _ in range(self.map.columns)]
            for _ in range(self.map.rows)
        ]

    def get_q_value(self, cell: Cell, direction: Directions) -> None:
        value = 0
        for direction in self.map.get_valid_moves(cell):
            new_cell = self.map.move(cell, direction) 
            reward = self.map.get_reward(new_cell)
            value = (1 - self.alpha) * value + self.alpha * \
                (reward + self.discount * self.q_values[new_cell.row_index][new_cell.column_index])
        return value  

    def get_move(self, cell):
        pass

    def test_probability(probability: float) -> bool:
        return random.random() > probability
    
    def reset_episode(self) -> None:
        pass
    
    def save_plots(self) -> None:
        pass
    
    def calculate_statistics(self) -> None:
        pass

    def print_statistics(self) -> None:
        pass

    def update(self) -> None:
        pass
