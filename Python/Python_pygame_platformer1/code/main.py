from settings import * # * = all code within file
from level import Level
from pytmx.util_pygame import load_pygame   #pytmx = map loader for pygame, handles "Tiled" object types while loading metadata for them -> edit maps and objects in Tiled instead of in source code, can import tmx files 
from os.path import join    # relative path for specific operating system, for directory addresses, some operating systems use forward slash or backslash which can cause issues if using program on different computers, join avoids this issue


###########################################
## Create the game program window #########
###########################################

# create Game class which controls basic logic of whole game
class Game:
    # method sets up the program's window, but DOES NOT run the program yet, begin "gathering materials" to be able to "build the house" but waiting for the signal to be able to start building
    def __init__(self):     # initialize the game itself, get everything you need to be able to run the game
        pygame.init()       # start running pygame, pygame is imported via settings.py
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))   # tells the game itself to display the program window surface (the actual program window with X in the top right, etc.) using window dimensions from settings.py
        pygame.display.set_caption('Slime World')   # set the title of the displayed program window

        # dictionary, each map assigned to KEY integer, VALUE is the tmx file associated with each map
        self.tmx_maps = {0: load_pygame(join('..', 'data', 'levels', 'map1.tmx'))}
        self.current_stage = Level(self.tmx_maps[0])
        
        self.current_stage = Level() # in example game, the stage can be either a level or the overworld, change to self.level if you only have levels/no overworld

    # method calls the game to run "turn the key to start the car's engine"
    def run(self):
        # Check to see if user is closing the game window via X in top right
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:    # pygame.QUIT = clicking the X button at the top right of the window to close the game window
                    pygame.quit()
                    sys.exit()
                    # if the event listener recieves the signal to QUIT, it first closes out pygame module then closes the system module, closing the window

            self.current_stage.run() # corresponds to self.current_stage = Level() above

            pygame.display.update()

# call the game class, actually tell the game to run
if __name__ == '__main__':
    game = Game()
    game.run()
            # wrap the game running code within 'if' statement to future proof against additional code interfering with ability to run the game
            # "if the name of the program is still: main, then run the game"
            # at this point, running main.py will display a blank black window with title and X in top right
            # see level.py


