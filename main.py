#Nuno Lima 10/01/2023
from src.game import Game

def main() -> None:
    map_path = "src\maps\level1.map"
    cell_size = 50
    game_types = ["play", "random","value","q-l"] 
    game = Game("RL-Challenge" , map_path, cell_size, type ="q-l", fps=10)
    game.start()
     
if __name__=="__main__":
    main()