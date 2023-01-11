from src.cell import Cell
from src.map import Map
from src.robot import Robot
from src.direction import Directions
from matplotlib import pyplot as plt

class ValueIterationAgent:
    def __init__(self, map: Map, robot: Robot) -> None:
        self.map = map
        self.robot = robot
        self.alpha = 0.2
        self.discount = 0.9
        self.iterations = 30
        self.values = self.inicialize_values()
        self.run_value_iterations()
        self.save_plot()

    def inicialize_values(self, is_random: bool = False) -> list[list]:
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
                        iteration_values[cell.row_index][cell.column_index] = self.map.goal_state_reward
                    else:
                        moves = self.map.get_valid_moves(cell)
                        iteration_values[cell.row_index][cell.column_index] = max([self.get_q_value(cell, move) for move in moves])
            self.values = iteration_values
    
    def get_move(self, cell):
        moves = self.map.get_valid_moves(cell)
        values = []
        for move in moves:
            new_cell = self.map.move(cell, move)
            values.append(self.values[new_cell.row_index][new_cell.column_index])
        max_index = values.index(max(values))
        return moves[max_index]

    def update(self) -> bool:
        direction = self.get_move(self.robot.current_cell)
        win, reward = self.robot.step(direction)
        return win

    def print_statistics(self) -> None:
        pass

    def save_plot(self) -> None:
        figure = plt.figure()
        ax = figure.add_subplot(111)
        cax = ax.matshow(self.values, interpolation='nearest', cmap='hot')
        figure.colorbar(cax)
        plt.savefig("figure2.png")



       
