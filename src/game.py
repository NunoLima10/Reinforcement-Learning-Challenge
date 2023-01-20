from src.map import Map
from src.robot import Robot
from src.randomly_agent import RandomlyAgent
from src.valueIteration_agent import ValueIterationAgent
from src.qlearning_agent import QLearningAgent

import pygame as pg

class Game:
    def __init__(self, title: str, map_path: str, cell_size: int , game_type: str ,fps: int = 30) -> None:
        self.title =  title
        self.map_path = map_path
        self.cell_size = cell_size
        self.game_type = game_type
        self.fps = fps
        self.map = Map(self.cell_size, map_path)
        self.robot = Robot(self.map)

        # default
        self.default_background_color = (64,64,64)
        self.randomly = RandomlyAgent(self.map, self.robot)
        self.value_iteration = ValueIterationAgent(self.map, self.robot)
        self.q_learning = QLearningAgent(self.map, self.robot)

        self.setup()

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
                if self.game_type == "play":
                    self.robot.check_events(event.key)
                
    def update(self) -> None:
        if self.game_type == "random":
            finished = self.randomly.update()
            if finished:
                exit()

        if self.game_type == "value":
            finished = self.value_iteration.update()
            if finished:
                exit()

        if self.game_type == "q-l":
            finished = self.q_learning.update()
            if finished:
                exit()
        
    def draw(self) -> None:
        self.screen.fill(self.default_background_color)
        self.map.draw(self.screen)
        self.robot.draw(self.screen)
        pg.display.update()

    def start(self) -> None:
        self.run()

    def __repr__(self) -> str:
        return f"<Game object title = '{self.title}' window_size = {self.window_size}>"
        
