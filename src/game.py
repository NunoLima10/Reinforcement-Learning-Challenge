from src.map import Map
from src.robot import Robot
from src.direction import Directions

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
                    self.robot.step(Directions.NORTH)

                if event.key == pg.K_DOWN:
                    self.robot.step(Directions.SOUTH)

                if event.key == pg.K_LEFT:
                    self.robot.step(Directions.WEST)

                if event.key == pg.K_RIGHT:
                    self.robot.step(Directions.EAST)
                

    def update(self) -> None:
        # self.robot.step(Directions.EAST)
        pass
        

    def draw(self) -> None:
        self.screen.fill(self.default_background_color)
        self.map.draw(self.screen)
        self.robot.draw(self.screen)
        pg.display.update()

    def start(self) -> None:
        self.run()

    def __repr__(self) -> str:
        return f"<Game object title = '{self.title}' window_size = {self.window_size}>"
        
