from src.game import Game

def main() -> None:
    map_path = "src\maps\level1.map"
    cell_size = 50
    
    game = Game("RL- Challenge" , map_path, cell_size)
    game.start()
    game.close()   



if __name__=="__main__":
    main()