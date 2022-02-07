import curses, curses.textpad
from ui import curses_utils

class Room(object):
  def __init__(self, name, x_size, y_size, cells=None, walls=None):
    # Init variables
    self.name = name
    self.x_size = x_size
    self.y_size = y_size

    # Init grid variables
    self.cells = [[None]*x_size for _ in range(y_size)]
    self.entities = dict()
    self.walls = walls

    # Add cells if there were any
    if cells is not None:
      for cell in cells:
        x, y, cell = cell
        self.cells[y][x] = cell

  # Add and remove entities
  def addEntity(self, entity):
    self.entities[entity.name] = entity

  def removeEntity(self, entity):
    del self.entities[entity.name]

  def inCollision(self, pos, ignore_id=None):
    for wall in self.walls:
      if (pos[0] == wall[0]) and (pos[1] == wall[1]):
        return True

      for entity in self.entities.values():
        if ignore_id is not None and entity.id == ignore_id:
          continue

        if (pos[0] == entity.pos[0]) and (pos[1] == entity.pos[1]):
          return True

    return False

  def getTarget(self, target_pos):
    # TODO: Would be better to have a pos->entity map to check here.
    for entity in self.entities.values():
      if (entity.pos[0] == target_pos[0]) and (entity.pos[1] == target_pos[1]):
        return entity

    return None

  def render(self, target):
    map_h, map_w = self.y_size + 4, self.x_size + 4
    map_y, map_x = 0, 0

    room_strs = self.getRows(target)
    str_colors = [curses.color_pair(2)] * len(room_strs)
    map_window = curses_utils.genTextWindow(map_h, map_w, map_y, map_x,
                                            room_strs, str_colors,
                                            y_pad=2, x_pad=2, box=True)

    return map_y, map_x, map_h, map_w, map_window

  def getRows(self, target):
    room_string = list()
    for row in self.cells:
      row_string = list()
      for cell in row:
        if cell is None:
          row_string.append(' ')
        elif cell.type == 'wall':
          row_string.append('#')
        else:
          row_string.append('.')
      room_string.append(row_string)

    # Render entities
    for entity in self.entities.values():
      x, y = entity.pos
      room_string[y][x] = entity.marker

    # Render target
    if target:
      x, y = target
      room_string[y][x] = "*"

    # Set room strings list
    room_strs = list()
    for row_string in room_string:
      room_strs.append(''.join(row_string))

    return room_strs
