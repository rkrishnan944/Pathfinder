import pygame

pygame.init()
width = 600
window = pygame.display.set_mode((width,width)) 
pygame.display.set_caption("A* Path Visualizer")


# Color Coding for Cells
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
GREY = (128,128,128)
TURQUOISE = (64,224,208)

class Node:
    def __init__(self,row,col,width,total_rows) -> None:
        self.row = row 
        self.col = col 
        self.x = col*width  # x increases in right direction in pixel draw
        self.y = row*width  # y increases in downward direction in pixel draw
        self.width = width 
        self.color = WHITE 
        self.total_rows = total_rows

    def make_wall(self):
        self.color = BLACK
    def make_start(self):
        self.color = ORANGE
    def make_end(self):
        self.color = TURQUOISE
    def reset(self):
        self.color = WHITE   

    def draw_node(self,window):
        pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.width))
        pygame.draw.rect(window,BLACK,(self.x,self.y,self.width,self.width),1)

    def get_pos(self):
        return self.row,self.col
    

def make_grid_matrix(width,rows):

    grid = []
    gap = width // rows 
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i,j,gap,rows)
            grid[i].append(node)
    return grid 

def get_clicked_pixel_pos(mouse_x,mouse_y,width,rows):

    gap = width // rows 
    row = mouse_y // gap 
    col = mouse_x // gap 
    return row,col
            

def main():
    run = True 
    rows = 30 
    # Loop to run the game window forever until X is pressed on window 
    
   
    grid = make_grid_matrix(width,rows)
    start = None 
    end = None 

    while run :
        
        window.fill(WHITE)

        for row in grid:
            for node in row:
                node.draw_node(window)

    
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False  
            else:

                if pygame.mouse.get_pressed()[0]:

                    mouse_x,mouse_y = pygame.mouse.get_pos() # this returns pixel position , now we are converting to grid row and col , to know which cell to color 
                    pixel_row,pixel_col = get_clicked_pixel_pos(mouse_x,mouse_y,width,rows)
                    cell = grid[pixel_row][pixel_col]

                    if start == None:
                        start = cell 
                        cell.make_start()
                    elif end == None and cell!=start:
                        end = cell
                        cell.make_end()
                    elif cell!=start and cell!=end:
                        cell.make_wall()

                # Right click to Rest Buttons 
                elif pygame.mouse.get_pressed()[2]:
                    mouse_x,mouse_y = pygame.mouse.get_pos()
                    pixel_row, pixel_col = get_clicked_pixel_pos(mouse_x,mouse_y,width,rows)
                    cell = grid[pixel_row][pixel_col]
                    cell.reset()

                    if cell == start:
                        start = None
                    elif cell == end:
                        end = None
                            

        pygame.display.update()

        

main()
pygame.quit()



 