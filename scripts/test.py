import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from hp_text_game.level_design.room import Room
from hp_text_game.level_design.cell import Cell

if __name__ == '__main__':
    room = Room.loadRoom('great_hall')
    room.display()
