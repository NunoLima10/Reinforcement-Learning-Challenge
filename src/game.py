from src.map import Map
from src.robot import Robot
from src.valueIteration_agent import ValueIterationAgent
from src.direction import Directions

from matplotlib import pyplot as plt

import pygame as pg
import numpy as np
import time
class Game:
    def __init__(self, title: str, map_path: str, cell_size: int , fps: int = 5) -> None:
        self.title =  title
        self.map_path = map_path
        self.cell_size = cell_size
        self.fps = fps
        self.map = Map(self.cell_size, map_path)
        self.robot = Robot(self.map)

        # default
        self.default_background_color = (64,64,64)
        self.setup()

        self.value_iteration_agente = ValueIterationAgent(self.map)
        # for line in self.value_iteration_agente.values:
        #     print( line)

        self.is_training = True
        self.max_steps_number = 20_000
        self.steps_number = 0
        self.max_episode_number = 30
        self.episode_number = 0
        self.episode_reward = 0 
        self.rewards =[]
    
    @property
    def window_size(self):
        return(self.map.width, self.map.height)

    def setup(self) -> None:
        pg.init()
        pg.display.set_caption(self.title)
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode(self.window_size)


    def run(self) -> None:
        while True:
            self.clock.tick(self.fps)
            self.check_events()
            self.update()
            self.draw()

    def close(self) -> None:
        pg.quit()
        exit()

    def check_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.close()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                     _, reward = self.robot.step(Directions.NORTH)

                if event.key == pg.K_DOWN:
                     _, reward = self.robot.step(Directions.SOUTH)

                if event.key == pg.K_LEFT:
                     _, reward = self.robot.step(Directions.WEST)

                if event.key == pg.K_RIGHT:
                    _, reward = self.robot.step(Directions.EAST)
                print(reward)
                

    def update(self) -> None:
        # self.randomly()
        win, reward = self.robot.step(self.value_iteration_agente.get_move(self.robot.current_cell))
        self.rewards.append(reward)
        if win:
            print("win heehehehehehe")
            pg.quit()
            # fig = plt.figure()
            # ax = fig.add_subplot(111)

            # cax = ax.matshow(self.value_iteration_agente.values, interpolation='nearest', cmap='hot')
            # fig.colorbar(cax)

            # plt.savefig("figure2.png")
            self.rewards.pop()
            space = range(len(self.rewards))
            average = np.average(self.rewards)
            standard_deviation = np.std(self.rewards)
            plt.plot(space,self.rewards)
            plt.plot(space,[average for _ in space])
            plt.savefig("figure3.png")
        # if self.move_index < len(self.moves):
        #     self.robot.step(self.moves[self.move_index])
        #     self.move_index += 1
        pass
            
    def randomly(self) -> None:
        win, reward = self.robot.random_step()
        self.steps_number += 1
        self.episode_reward += reward

        #reset
        if win or self.steps_number > self.max_steps_number:
            print(f"episode {self.episode_number} total reward {self.episode_reward/self.steps_number}")
            self.rewards.append(self.episode_reward/self.steps_number)
            self.episode_number += 1
            self.steps_number = 0
            self.episode_reward = 0
            self.robot.current_cell = self.map.robot_inicial_cell
            #end
            if self.episode_number > self.max_episode_number:
                time_end = time.time()
                pg.quit()
                plt.xlabel("episodes")
                plt.ylabel("episode_reward/steps_number")
                space = range(len(self.rewards))
                average = np.average(self.rewards)
                standard_deviation = np.std(self.rewards)
                plt.plot(space,self.rewards)
                plt.plot(space,[average for _ in space])
               
                plt.savefig("figure1.png")
               

                print("==========RandomSteps==========")
                print(f"max steps number: {self.max_steps_number}")
                print(f"max episode number: {self.max_episode_number}")
                print(f"rewards: {[ round(rewards,2) for rewards in self.rewards]}")
                print(f"average reward / steps_number: {round(average, 2)}")
                print(f"standard_deviation reward / steps_number: {round(standard_deviation,2)}")
                print(f"time took {round(time_end - self.time_start,2)} sec")
                exit()
    
    def draw(self) -> None:
        self.screen.fill(self.default_background_color)
        self.map.draw(self.screen)
        self.robot.draw(self.screen)
        pg.display.update()

    def start(self) -> None:
        self.time_start = time.time()
        self.run()

    def __repr__(self) -> str:
        return f"<Game object title = '{self.title}' window_size = {self.window_size}>"
        
