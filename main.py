# Importing necessary library or module
import pygame    # Main Library to run this game
import sys
import random  # For generating random number

pygame.init()   # Initialize the pygame

# constants
window_height = 700  
window_weidth = 800
grid_weidth = 10  # Playing grid weidth
grid_height = 20  # Playing grid height
cellsize = 30  # Cellsize
x_offset = 50
y_offset = 50

# Colors
Black = (0,0,0)
White = (255,255,255)
Cyan = (0,255,255)
Blue = (0,0,255)
Orange = (255,165,0)
Yellow = (255,255,0)
Green = (0,255,0)
Purple = (128,0,128)
Red = (255,0,0)
Gray = (128,128,128)

# The tetrominos
Pieces = {
    "I" : {
        "shape" : [
            [[1,1,1,1]],
            [
                [1],
                [1],
                [1],
                [1]
            ]
        ],
        "color" : Cyan
    },
    "O" : {
        "shape" : [
            [
                [1,1],
                [1,1]
            ]
        ],
        "color" : Yellow
    },
    "T" : {
        "shape" : [
            [[0,1,0],
             [1,1,1]],
            [[1,0],
             [1,1],
             [1,0]],
            [[1,1,1],
             [0,1,0]],
            [[0,1],
             [1,1],
             [0,1]]
        ],
        "color" : Purple
    },
    "S" : {
        "shape" : [
            [[0,1,1],
             [1,1,0]],
            [[1,0],
             [1,1],
             [0,1]]
        ],
        "color" : Green
    },
    "Z" : {
        "shape" : [
            [[1,1,0],
             [0,1,1]],
            [[0,1],
             [1,1],
             [1,0]]
        ],
        "color" : Red
    },
    "J" : {
        "shape" : [
            [[1,0,0],
             [1,1,1]],
            [[1,1],
             [1,0],
             [1,0]],
            [[1,1,1],
             [0,0,1]],
            [[0,1],
             [0,1],
             [1,1]]
        ],
        "color" : Blue
    },
    "L" : {
        "shape" : [
            [[0,0,1],
             [1,1,1]],
            [[1,0],
             [1,0],
             [1,1]],
            [[1,1,1],
             [1,0,0]],
            [[1,1],
             [0,1],
             [0,1]]
        ],
        "color" : Orange
    }
}



# For the pieces (TetroMinos)
class TetroMino:
    # The constructor
    def __init__(self, piece_type):
        self.type = piece_type  # Store the tetrominos type
        self.shape = Pieces[piece_type]["shape"]  # Store shape
        self.color = Pieces[piece_type]["color"]  # Store color
        self.x = grid_weidth//2 - len(self.shape[0][0])//2  # Place the piece horizontally by adjusting
        self.y = 0
        self.rotation = 0   # Default 0


    # Getting the current rotating shape
    def get_current_shape(self):
        return self.shape[self.rotation]
    

    # Rotate the piece clockwise
    def rotate(self):
        self.rotation = (self.rotation+1) % len(self.shape)


    # Occupying the cells by the piece
    def get_cells(self):
        cells = []  # store position
        current = self.get_current_shape()
        for y,row in enumerate(current):
            for x,cell in enumerate(row):
                if cell:
                    cells.append((self.x+x, self.y+y)) # Add the cells position
        return cells
    



# Main Gaming Object
class TetrisGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((window_weidth,window_height)) # Create Window
        pygame.display.set_caption("Tetris")  # Give title
        self.fps = pygame.time.Clock()   # Control fps
        self.grid = [[0 for _ in range(grid_weidth)] for _ in range(grid_height)]  # Creating the grid
        self.running = True # Game loop
        self.current_piece = self.spawn_pieces()  # Get current piece
        self.fall_time = 0
        self.fall_speed = 1000  # miliseconds
        self.score = 0  # Keep track of scores
        self.line_cleared = 0 # Keep tracks how many lines have cleared
        self.level = 1 # Level


    # For random pieces generation
    def spawn_pieces(self):
        piece_type = random.choice(list(Pieces.keys())) # Select random piece type
        return TetroMino(piece_type)


    # Drawing the grid
    def draw_grid(self):
        # Drawing the vertical lines
        for x in range(grid_weidth+1):
            pygame.draw.line(self.screen, Gray, (x_offset+x*cellsize, y_offset), (x_offset+x*cellsize, y_offset+grid_height*cellsize))
        
        # Drawing the horizontal lines
        for y in range(grid_height+1):
            pygame.draw.line(self.screen, Gray, (x_offset,y_offset+y*cellsize), (x_offset+cellsize*grid_weidth, y_offset+y*cellsize))


    # Drawing the filled cell of the grid with color
    def draw_cells(self):
        for y in range(grid_height):
            for x in range(grid_weidth):
                if self.grid[y][x] != 0:
                    # Making rectangle by their positions
                    rectangle = pygame.Rect(
                        x_offset+x*cellsize+1,
                        y_offset+y*cellsize+1,
                        cellsize-2,cellsize-2
                    )
                    pygame.draw.rect(self.screen, self.grid[y][x], rectangle) # Draw


    # To draw the falling piece
    def current_cells(self):
        if self.current_piece:
            # Loop through all the grid position
            for x,y in self.current_piece.get_cells():
                if 0<=x and x<grid_weidth and y>=0 and y<grid_height: # Checking if position is not out of borders
                    # Making rectangle by their positions
                    rectangle = pygame.Rect(
                        x_offset+x*cellsize+1,
                        y_offset+y*cellsize+1,
                        cellsize-2,
                        cellsize-2
                    )
                    pygame.draw.rect(self.screen, self.current_piece.color, rectangle) # Draw the rectangle


    # For checking the collision with boundaries or other pieces
    def check_collision(self):
        if not self.current_piece: # check if there is actually a piece or not
            return False
        
        # Loop through checking the collision
        for x,y in self.current_piece.get_cells():
            # Checking collision with boundaries
            if x<0 or x>=grid_weidth or y>=grid_height:
                return True
            
            # Checking collision with other pieces
            if y>=0 and self.grid[y][x]!=0:
                return True
        
        return False


    # For moving the pieces
    def move_pieces(self, dx, dy):
        if self.current_piece:
            old_x, old_y = self.current_piece.x, self.current_piece.y # saving the old position in case it needs
            self.current_piece.x += dx   # Update x position
            self.current_piece.y += dy   # Update y position

            if self.check_collision():
                # Revert the move if collision happen
                self.current_piece.x = old_x
                self.current_piece.y = old_y
                return False
            return True


    # Placing piece in the grid
    def place_piece(self):
        if self.current_piece:
            for x,y in self.current_piece.get_cells():
                if x>=0 and x<grid_weidth and y>=0 and y<grid_height:
                    self.grid[y][x] = self.current_piece.color  # Color the grid with piece color
        
        self.clear_line() # Clear the line


    # Rotate the pieces
    def rotate_piece(self):
        if self.current_piece:
            old_rotation = self.current_piece.rotation
            self.current_piece.rotate()  # Rotate the piece

            # Revert rotation if collision happen
            if self.check_collision():
                self.current_piece.rotation = old_rotation


    # Handling game events
    def handle_event(self):
        # Checking if something is pressed
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.running = False  # Break the game loop
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:  # Escape key
                    self.running = False
                elif events.key == pygame.K_LEFT:  # Arrow left
                    self.move_pieces(-1,0)
                elif events.key == pygame.K_RIGHT: # Arrow Right
                    self.move_pieces(1,0)
                elif events.key == pygame.K_DOWN:  # Arrow Down
                    self.move_pieces(0,1)
                elif events.key == pygame.K_UP:    # Arrow Up
                    self.rotate_piece()  # Rotate the falling tetromino
    

    # For clearing the filled line
    def clear_line(self):
        # store the indices of the lines that are completely filled
        lines_to_clear = []

        # Checking bottom to top
        for y in range(grid_height-1, -1, -1):
            if all(cell!=0 for cell in self.grid[y]):
                lines_to_clear.append(y) # Adding the index of filling rows
        
        # Clearing the entire row
        for y in lines_to_clear:
            del self.grid[y]  # Delete the row
        # Inserting an whole row
        for y in lines_to_clear:
            self.grid.insert(0,[0 for _ in range(grid_weidth)]) # Insert a new row in the top

        # Update the scores and other statistics
        if lines_to_clear:
            self.line_cleared += len(lines_to_clear) # Update the number of line cleared
            self.update_score(len(lines_to_clear))   # Update score
            self.update_level()                      # Update level


    # Update the game state
    def update(self):
        self.fall_time += self.fps.get_time() # A counter for how long it's been since the piece last fell down by one block.

        if self.fall_speed<=self.fall_time: # Defining how fast the piece should fall
            self.fall_time = 0  # Reset time after the piece moved down
            
            # Attempt to move the piece down
            # If the attempt become failure it means the piece is landed
            if not self.move_pieces(0,1):
                # Piece cannot move down
                self.place_piece()  # Place the piece permanently on the grid
                self.current_piece = self.spawn_pieces() # Create a new falling piece

                # Checks if the newly spawned piece immediately collides or overlaps with already placed blocks.
                if self.check_collision():
                    self.game_over()


    # Game over indicator
    def game_over(self):
        print("\n\n")
        print(f"Game over!! Final score : {self.score}") # Print the final score in terminal
        self.running = False  # Break the game loop


    # Update scores 
    def update_score(self,line_cleared):
        # Tetris scoring system
        # If at the same time 2 rows can be filled then 200 point will be added
        # If at the same time 3 rows can be filled then 500 point will be added and so on
        line_scores = {1:100, 2:200, 3:500, 4:800}
        base_score = line_scores.get(line_cleared,0) # Calculating the primary scores
        self.score += base_score * self.level  # Calculate the final score


    # Update level
    def update_level(self):
        new_level = (self.line_cleared//10) + 1 # Calculating the new level

        if new_level != self.level:
            self.level = new_level # Update the level
            self.fall_speed = max(50, 1000-(self.level-1)*50) # Increasing falls speed 
    

    # For showing scores, level and the line it has cleared
    def draw_ui(self):
        font = pygame.font.Font(None,36) # Rendering font object

        # Show score
        score_text = font.render(f"Score : {self.score}", True, White)  # Make the text indicating scores
        self.screen.blit(score_text,(x_offset+grid_weidth*cellsize+20,50)) # Write this directly to main surface

        # Show level
        level_text = font.render(f"Level : {self.level}", True, White)
        self.screen.blit(level_text,(x_offset+cellsize*grid_weidth+20,100))

        # Show the number of lines cleared
        line_text = font.render(f"Lines: {self.line_cleared}", True, White)
        self.screen.blit(line_text,(x_offset+cellsize*grid_weidth+20,150))


    # Make visible to the screen the drawing
    def draw(self):
        self.screen.fill(Black) # Screen fills with Black
        self.draw_grid()        # Draw the grid
        self.draw_cells()       # Draw the cells inside the grid
        self.current_cells()
        self.draw_ui()          # Draw the scoring interface
        pygame.display.flip() # Updates the display with the drawing


    # Make the game running
    def run(self):
        # Main game loop
        while self.running:
            self.handle_event()  # Handling keyboard input
            self.update()        # Update everything on the screen
            self.draw()          # Draw 
            self.fps.tick(60) # 60 fps
        
        pygame.quit() # Exit the game
        sys.exit()    # Terminate the program



if __name__=="__main__":
    game = TetrisGame() # Object to run the game
    game.run()
