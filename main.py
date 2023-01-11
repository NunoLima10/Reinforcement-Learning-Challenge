#Nuno Lima 10/01/2023
from src.game import Game

def main() -> None:
    map_path = "src\maps\level1.map"
    cell_size = 75
    game_types = ["play", "random","value"] 
    game = Game("RL-Challenge" , map_path, cell_size, type ="value", fps=120 )
    game.start()
     
if __name__=="__main__":
    main()