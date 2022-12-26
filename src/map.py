import pygame as pg


class Map:
    def __init__(self, cell_size: int, file_path: str) -> None:
        self.cell_size = cell_size
        self.file_path = file_path
        self.map = self.load_map()

        self.rows = len(self.map[0])
        self.columns = len(self.map)

        self.width = self.rows * cell_size
        self.height =  self.columns * cell_size

        self.show_grid = True
        self.lines = self.generate_grid_lines()
        
        self.tiles = {
            "#":(0,0,0),
            "-":(255,255,255)
        }
    
    def valide_map(self, map:list[list]) -> bool:
        pass
    
    def generate_grid_lines(self) -> None:
        
        lines = []
        for i in range(1,self.rows):
            x_start =  i * self.cell_size
            y_start = 0
            y_end = self.height
            start_point = (x_start, y_start)
            end_point = (x_start, y_end)
            lines.append((start_point, end_point))

        for i in range(1,self.columns):
            x_start = 0
            y_start = i *  self.cell_size
            x_end = x_start + self.width

            start_point = (x_start, y_start)
            end_point = (x_end, y_start)
            lines.append((start_point, end_point))

        return lines
        

    def load_map(self) -> list:
        with open(self.file_path,"r") as file:
            content = file.readlines()
        map = []
        for line in content:
            row = [cell for cell in line if cell != "\n"]
            map.append(row)
        return map

    
    def draw(self, surface: pg.Surface) -> None:
        
        for column_index, line in enumerate(self.map):
            for row_index, cell in enumerate(line):
                position = (row_index * self.cell_size, column_index * self.cell_size)
                rect = (position,(self.cell_size,self.cell_size))
                color = self.tiles[cell]              
                pg.draw.rect(surface,color,rect)

        
        if self.show_grid:
            for line in self.lines:
                pg.draw.line(surface,(0,0,0),line[0],line[1])

                
                   
            
