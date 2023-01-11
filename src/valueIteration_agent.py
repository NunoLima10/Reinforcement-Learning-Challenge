from src.cell import Cell
from src.map import Map
from src.robot import Robot
from src.direction import Directions
from matplotlib import pyplot as plt

import  random
import numpy as np
import time
class ValueIterationAgent:
    def __init__(self, map: Map, robot: Robot) -> None:
        self.map = map
        self.robot = robot
        self.alpha = 0.2
        self.discount = 0.9

        self.max_iteration = 30
        self.max_steps_number = 20_000
        self.steps_number = 0
        self.iteration_number = 0
        self.episode_reward = 0 
        self.rewards = []
        self.space = range(self.max_iteration)

        self.values = self.inicialize_values()
        self.run_value_iterations()
        self.start_time = time.time()
        

    def inicialize_values(self) -> list[list]:
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
        max_value = max(values)
        max_values_index = [index for index,value in enumerate(values) if value == max_value]
        return moves[random.choice(max_values_index)]

    def reset_episode(self) -> None:
        self.run_value_iterations()
    
        self.rewards.append(self.episode_reward / self.steps_number)
        print(f" iteration {self.iteration_number} episode_reward / steps_number: {self.episode_reward / self.steps_number}")
        self.iteration_number += 1
        self.steps_number = 0
        self.episode_reward = 0
        self.robot.current_cell = self.map.robot_inicial_cell

    def update(self) -> bool:
        direction = self.get_move(self.robot.current_cell)
        win, reward = self.robot.step(direction)
        self.steps_number += 1
        self.episode_reward += reward

        if win or self.steps_number > self.max_steps_number:
            self.reset_episode()
        
        last_iteration = self.iteration_number >= self.max_iteration
        if last_iteration:
            self.calculate_statistics()
            # self.save_plot()
            self.save_plot2()
        return last_iteration

    def print_statistics(self) -> None:
        pass

    def save_plot(self) -> None:
        figure = plt.figure()
        ax = figure.add_subplot(111)
        cax = ax.matshow(self.values, interpolation='nearest', cmap='hot')
        figure.colorbar(cax)
        plt.savefig("figure2.png")
    
    def save_plot2(self) -> None:
        plt.xlabel("iteration")
        plt.ylabel("iteration_reward / steps_number")       
        plt.plot(self.space, self.rewards)
        plt.plot(self.space,[self.average for _ in self.space])   
        plt.savefig("figure3.png")

    def calculate_statistics(self) -> None:
        self.time = time.time() - self.start_time
        self.average = np.average(self.rewards)
        self.standard_deviation = np.std(self.rewards)



       
