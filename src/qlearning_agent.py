from src.cell import Cell
from src.map import Map
from src.direction import Directions
from src.robot import Robot
from src.color_printer import ColorPrinter
from matplotlib import pyplot as plt

import random
import numpy as np
import time

class QLearningAgent:
    def __init__(self, map: Map, robot: Robot) -> None:
        self.map = map
        self.robot = robot
        self.alpha = 0.2
        self.discount = 0.9
        self.epsilon = 0.9
        self.noise = 0.95

        self.max_games = 30
        self.max_steps_number = 20_000
        self.steps_number = 0
        self.game_number = 1
        self.game_reward = 0 
        self.rewards = []
        self.space = range(self.max_games)
        self.directions = [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST] 

        self.q_values = self.inicialize_q_values()
        self.start_time = time.time()
        
    def inicialize_q_values(self) -> list[list]:
        return [
            [0  for _ in range(self.map.rows * self.map.columns)]
            for _ in range(len(self.directions))
        ]

    def max_cell_q_value(self, cell: Cell) -> float:
        cell_q_value = [self.q_values[index][cell.id] for index, _ in enumerate(self.directions)]
        return max(cell_q_value)

    def get_q_value(self, cell: Cell) -> float:
        value = 0
        for direction in self.map.get_valid_moves(cell):
            new_cell = self.map.move(cell, direction) 
            reward = self.map.get_reward(new_cell)
            value = (1 - self.alpha) * value + self.alpha * \
                (reward + self.discount * self.max_cell_q_value(new_cell))
        return value  

    def run_q_learning(self) -> None:
        values = self.inicialize_q_values()
        for row in  self.map.map:
            for cell in row:
                for index,_ in enumerate(self.directions):
                    if self.map.is_goal_state(cell):
                        values[index][cell.id] = self.map.goal_state_reward
                    else:
                        values[index][cell.id] = self.get_q_value(cell)
        self.q_values = values

    def test_probability(self, probability:  float) -> bool:
        return random.random() > probability

    def get_move(self, cell) -> Directions:
        legal_moves = self.map.get_valid_moves(cell)
        values = []
        for move in legal_moves:
            new_cell = self.map.move(cell, move)
            values.append(self.q_values[self.directions.index(move)][new_cell.id])

        max_value = max(values)
        max_values_index = [index for index,value in enumerate(values) if value == max_value]
        best_move =  legal_moves[random.choice(max_values_index)]
        random_move = random.choice(legal_moves)
        return random_move if self.test_probability(self.epsilon) else best_move

    def reset_episode(self) -> None:
        self.run_q_learning()
        self.rewards.append(self.game_reward / self.steps_number)
        print(f"iteration {self.game_number} episode_reward / steps_number: {ColorPrinter.colored(self.game_reward / self.steps_number)}")
        self.game_number += 1
        self.steps_number = 0
        self.game_reward = 0
        self.robot.current_cell = self.map.robot_inicial_cell
    
    def update(self) -> bool:
        direction = self.get_move(self.robot.current_cell)
        win, reward = self.robot.step(direction)
        self.steps_number += 1
        self.game_reward += reward
      
        last_iteration = self.game_number > self.max_games
        if last_iteration:
            self.calculate_statistics()
            self.print_statistics()
            self.save_plots()
        
        if win or self.steps_number > self.max_steps_number:
            self.reset_episode()
        return last_iteration

    def save_plots(self) -> None:
        plt.figure(1)
        plt.title("QLearningAgent")
        plt.xlabel("iteration")
        plt.ylabel("iteration_reward / steps_number")       
        plt.plot(self.space, self.rewards)
        plt.plot(self.space,[self.average for _ in self.space]) 
        plt.tight_layout()  
        plt.savefig("QLearningAgent.png")
        
    def calculate_statistics(self) -> None:
        self.time = time.time() - self.start_time
        self.average = np.average(self.rewards)
        self.standard_deviation = np.std(self.rewards)

    def print_statistics(self) -> None:
        ColorPrinter.show(f"{'='*10}QLearningAgent:{'='*10}","warning")
        print(f"max steps number: {ColorPrinter.colored(self.max_steps_number)}")
        print(f"max games: {ColorPrinter.colored(self.max_games)}")
        print(f"average reward / steps_number: {ColorPrinter.colored(round(self.average, 2))}")
        print(f"standard_deviation reward / steps_number: {ColorPrinter.colored(round(self.standard_deviation,2))}")
        print(f"time took {ColorPrinter.colored(round(self.time,2))} sec")
