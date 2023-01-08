from src.map import Map
from src.robot import Robot
from src.direction import Directions

from matplotlib import pyplot as ptl

import pygame as pg

class Game:
    def __init__(self, title: str, map_path: str, cell_size: int , fps: int = 30) -> None:
        self.title =  title
        self.map_path = map_path
        self.cell_size = cell_size
        self.fps = fps
        self.map = Map(self.cell_size, map_path)
        self.robot = Robot(self.map)

        # default
        self.default_background_color = (64,64,64)
        self.setup()

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
                # print(reward)
                

    def update(self) -> None:
        self.randomly()
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
                pg.quit()
                ptl.plot(range(len(self.rewards)),self.rewards)
                ptl.show()
        
        


        

    def draw(self) -> None:
        self.screen.fill(self.default_background_color)
        self.map.draw(self.screen)
        self.robot.draw(self.screen)
        pg.display.update()

    def start(self) -> None:
        self.run()

    def __repr__(self) -> str:
        return f"<Game object title = '{self.title}' window_size = {self.window_size}>"
        
