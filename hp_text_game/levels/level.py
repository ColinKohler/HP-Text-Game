import os, sys
import yaml

from .room import Room
from .cell import Cell

class Level(object):
  def __init__(self, ):
    self.rooms = dict()

  def generateLevel(self):
    self.rooms['great_hall'] = self.loadRoom('great_hall')

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

    return Room(room_doc['name'],
                int(room_doc['x_size']),
                int(room_doc['y_size']),
                cells=cells,
                walls=walls)

  def addEntityToRoom(self, entity, room, position):
    entity.addToRoom(position, self.rooms[room])
    self.rooms[room].addEntity(entity)

  def render(self, target):
    for room in self.rooms.values():
      map_y, map_x, map_h, map_w, map_window = room.render(target)

    return map_y, map_x, map_h, map_w, map_window
