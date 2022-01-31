import os, sys
import yaml
import curses, curses.textpad

from .room import Room
from .cell import Cell
import ui

class Level(object):
  def __init__(self, ):
    self.rooms = list()

  def generateLevel(self):
    great_hall = self.loadRoom('great_hall')

    self.rooms.append(great_hall)

  def loadRoom(self, room_name):
    # Setup path to yaml room descriptors
    room_path = os.path.abspath(__file__)
    room_dir = os.path.dirname(room_path) + '/defined_rooms/'
    room_pwd = room_dir + room_name + '.yaml'

    # Read data from yaml file
    stream = open(room_pwd, 'r')
    room_doc = yaml.load(stream)

    # Load yaml data into python class
    cells = list()
    walls = list()
    cell_docs = room_doc['cells']
    for cell_doc in cell_docs:
      for i in range(cell_doc['x_min'], cell_doc['x_max']+1):
        for j in range(cell_doc['y_min'], cell_doc['y_max']+1):
          cells.append((i, j, Cell(cell_doc['type'])))

          if 'wall' in cell_doc['type']:
            walls.append((i, j))

    return Room(room_doc['name'], room_doc['x_size'], room_doc['y_size'], cells=cells, walls=walls)

  def render(self):
    for room in self.rooms:
      map_h, map_w = room._y_size + 4, room._x_size + 4
      map_y, map_x = 0, 0
      room_strs = room.getRows()
      str_colors = [curses.color_pair(2)] * len(room_strs)
      map_window = ui.genTextWindow(map_h, map_w, map_y, map_x,
                                    room_strs, str_colors,
                                    y_pad=2, x_pad=2, box=True)

      return map_y, map_x, map_h, map_w, map_window
