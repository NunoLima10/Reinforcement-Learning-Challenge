from src.map import Map
from src.robot import Robot
from src.valueIteration_agent import ValueIterationAgent
from src.direction import Directions
from randomly_agent import Randomly

import pygame as pg
import time
class Game:
    def __init__(self, title: str, map_path: str, cell_size: int , fps: int = 120) -> None:
        self.title =  title
        self.map_path = map_path
        self.cell_size = cell_size
        self.fps = fps
        self.map = Map(self.cell_size, map_path)
        self.robot = Robot(self.map)

        # default
        self.default_background_color = (64,64,64)
        self.setup()

        # self.value_iteration_agente = ValueIterationAgent(self.map)
        self.randomly = Randomly(self.map, self.robot, 20_000, 30)
        # for line in self.value_iteration_agente.values:
        #     print( line)

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
        is_last_episode = self.randomly.update()
        if is_last_episode:
            exit()
       
        # win, reward = self.robot.step(self.value_iteration_agente.get_move(self.robot.current_cell))
        # self.rewards.append(reward)
        # if win:
        #     print("win heehehehehehe")
        #     pg.quit()
        #     # fig = plt.figure()
        #     # ax = fig.add_subplot(111)

        #     # cax = ax.matshow(self.value_iteration_agente.values, interpolation='nearest', cmap='hot')
        #     # fig.colorbar(cax)

        #     # plt.savefig("figure2.png")
        #     self.rewards.pop()
        #     space = range(len(self.rewards))
        #     average = np.average(self.rewards)
        #     standard_deviation = np.std(self.rewards)
        #     plt.plot(space,self.rewards)
        #     plt.plot(space,[average for _ in space])
        #     plt.savefig("figure3.png")
        
        pass
            
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
        
