
from src.direction import Directions
from src.cell import Cell
from src.map import Map
import random


class ValueIterationAgent:
    def __init__(self, map: Map) -> None:
        self.map= map
        self.alpha = 0.2
        self.discount = 0.9
        self.iterations = 30
        self.directions = [Directions.NORTH, Directions.SOUTH, Directions.WEST, Directions.EAST]
        self.values = self.inicialize_values()
        self.run_value_iterations()

    def inicialize_values(self, is_random: bool = False) -> list[list]:
        # values = []
        # for column_index in range(self.map.columns):
        #     row_values = []
        #     for row_index in range(self.map.rows):
        #         cell_values = [0 for _ in range(len(self.directions))]
        #         row_values.append(cell_values)
        #     values.append(row_values)
        # return values
        return [
            [0  for _ in range(self.map.columns)]
            for _ in range(self.map.rows)
        ]
    
    def get_q_value(self, cell: Cell, direction: Directions) -> None:
        value = 0
        for direction in self.map.get_valid_moves(cell):
            new_cell = self.map.move(cell, direction) 
            reward = self.map.get_reward(new_cell)
            value = (1 - self.alpha) * value + self.alpha * \
                (reward + self.discount * self.values[new_cell.row_index][new_cell.column_index])
        return value  
    
    def run_value_iterations(self) -> None:
        for episode in range(self.iterations):
            iteration_values = self.inicialize_values()
            for row in  self.map.map:
                for cell in row:
                    if self.map.is_goal_state(cell):
                        iteration_values[cell.row_index][cell.column_index] = 100
                    else:
                        moves = self.map.get_valid_moves(cell)
                        iteration_values[cell.row_index][cell.column_index] = max([self.get_q_value(cell, move) for move in moves])
            self.values = iteration_values
            print("="*50)
            for line in self.values:
                print([round(value,2) for value in line])

    def get_move(self, cell):
        moves = self.map.get_valid_moves(cell)
        values = []
        for move in moves:
            new_cell = self.map.move(cell, move)
            values.append(self.values[new_cell.row_index][new_cell.column_index])
        max_index = values.index(max(values))
        return moves[max_index]


       
