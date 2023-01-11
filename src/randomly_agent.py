from src.map import Map
from src.robot import Robot
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
        self.episode_number = 0
        self.episode_reward = 0 
        self.rewards = []
        self.space = range(self.max_episode_number)
        self.average = 0
        self.standard_deviation = 0 
        self.start_time = time.time()
        

    def update(self) -> bool:
        is_last_episode = False
        win, reward = self.robot.random_step()
    
        self.episode_reward += reward
        self.steps_number += 1
        
        if win or self.steps_number > self.max_steps_number:
            print(f"episode {self.episode_number} total reward {self.episode_reward/self.steps_number}")
            self.reset_episode()

        if self.episode_number > self.max_episode_number:
                self.calculate_statistics()
                self.save_plot()
                self.print_statistics()
                is_last_episode = True

        return is_last_episode
                
    def reset_episode(self) -> None:
        self.rewards.append(self.episode_reward/self.steps_number)
        self.episode_number += 1
        self.steps_number = 0
        self.episode_reward = 0
        self.robot.current_cell = self.map.robot_inicial_cell

    def calculate_statistics(self) -> None:
        self.rewards.pop()
        self.time = time.time() - self.start_time
        self.average = np.average(self.rewards)
        self.standard_deviation = np.std(self.rewards)

    def save_plot(self) -> None:
        plt.xlabel("episodes")
        plt.ylabel("episode_reward / steps_number")       
        plt.plot(self.space, self.rewards)
        plt.plot(self.space,[self.average for _ in self.space])   
        plt.savefig("figure1.png")
    
    def print_statistics(self) -> None:
        print("==========RandomSteps==========")
        print(f"max steps number: {self.max_steps_number}")
        print(f"max episode number: {self.max_episode_number}")
        print(f"rewards: {[ round(rewards,2) for rewards in self.rewards]}")
        print(f"average reward / steps_number: {round(self.average, 2)}")
        print(f"standard_deviation reward / steps_number: {round(self.standard_deviation,2)}")
        print(f"time took {round(self.time,2)} sec")
