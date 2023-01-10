from src.game import Game

def main() -> None:
    map_path = "src\maps\level1.map"
    cell_size = 75
    
    game = Game("RL - Challenge" , map_path, cell_size)
    game.start()
     



if __name__=="__main__":
    main()