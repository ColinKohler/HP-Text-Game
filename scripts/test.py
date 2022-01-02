import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from hp_text_game.levels.room import Room
from hp_text_game.levels.cell import Cell

if __name__ == '__main__':
    room = Room.loadRoom('great_hall')
    room.display()
