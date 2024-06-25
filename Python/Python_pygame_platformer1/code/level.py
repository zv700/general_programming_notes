from settings import *

# for main.py to be able to run the Level class, import Level within main.py, then create an instance of Level class within Game class inside of main.py
class Level:
    # gather materials to be able to run the Level class
    def __init__(self, tmx_map):
        self.display_surface = pygame.display.get_surface() # display_surface allows this Level class to display the level on the program window's surface created by Game class within main.py, GET/obtain/select the empty black window created by Game class within main.py

def setup(self, tmx_map):
    tmx_map.get_layer_by_name('Terrain') 

    # method tells the Level class to run
    def run(self):
        self.display_surface.fill('pink') # changes the program window's background color

