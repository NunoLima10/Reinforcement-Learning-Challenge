from src.map import Map
from src.robot import Robot
from src.color_printer import ColorPrinter
from matplotlib import pyplot as plt

import time
import numpy as np

class RandomlyAgent:
    def __init__(self,map: Map, robot: Robot) -> None:
        self.map = map
        self.robot = robot
        self.max_steps_number = 20_000
        self.max_episode_number = 30
        self.steps_number = 0
        self.episode_number = 1
        self.episode_reward = 0 
        self.rewards = []
        self.space = range(self.max_episode_number)
        self.average = 0
        self.standard_deviation = 0 
        self.start_time = time.time()

    def reset_episode(self) -> None:
        self.rewards.append(self.episode_reward/self.steps_number)
        self.episode_number += 1
        self.steps_number = 0
        self.episode_reward = 0
        self.robot.current_cell = self.map.robot_inicial_cell
        
    def update(self) -> bool:
        is_last_episode = False
        win, reward = self.robot.random_step()
    
        self.episode_reward += reward
        self.steps_number += 1
        
        if win or self.steps_number > self.max_steps_number:
            print(f"episode {self.episode_number} total reward {ColorPrinter.colored(self.episode_reward/self.steps_number)}")
            self.reset_episode()

        if self.episode_number > self.max_episode_number:
                self.calculate_statistics()
                self.save_plots()
                self.print_statistics()
                is_last_episode = True

        return is_last_episode
                
    def calculate_statistics(self) -> None:
        self.time = time.time() - self.start_time
        self.average = np.average(self.rewards)
        self.standard_deviation = np.std(self.rewards)

    def save_plots(self) -> None:
        plt.figure(1)
        plt.title(f"RandomlyAgent")
        plt.xlabel("episodes")
        plt.ylabel("episode_reward / steps_number")       
        plt.plot(self.space, self.rewards)
        plt.plot(self.space,[self.average for _ in self.space])   
        plt.savefig("RandomlyAgent.png")
    
    def print_statistics(self) -> None:
        ColorPrinter.show(f"{'='*10}RandomlyAgent{'='*10}","warning")
        print(f"max steps number: {ColorPrinter.colored(self.max_steps_number)}")
        print(f"max episode number: {ColorPrinter.colored(self.max_episode_number)}")
        print(f"average reward / steps_number: {ColorPrinter.colored(round(self.average, 2))}")
        print(f"standard_deviation reward / steps_number: {ColorPrinter.colored(round(self.standard_deviation,2))}")
        print(f"time took {ColorPrinter.colored(round(self.time,2))} sec")
