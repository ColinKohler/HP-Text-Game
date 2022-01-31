class Room(object):
  def __init__(self, name, x_size, y_size, cells=None, walls=None):
    # Init variables
    self._name = name
    self._x_size = x_size
    self._y_size = y_size

    # Init grid variables
    self._cells = [[None]*x_size for _ in range(y_size)]
    self._entities = dict()
    self.walls = walls

    # Add cells if there were any
    if cells is not None:
      for cell in cells:
        x, y, cell = cell
        self._cells[y][x] = cell

  # Add and remove entities
  def addEntity(self, e_id, entity):
    self._entities[e_id] = entity

  def removeEntity(self, e_id):
    del self._entities[e_id]

  def checkCollision(self, pos, ignore_id=None):
    for wall in self.walls:
      if (pos[0] == wall[0]) and (pos[1] == wall[1]):
        return True

      for entity in self._entities.values():
        if ignore_id is not None and entity._id == ignore_id:
          continue

        if (pos[0] == entity._pos[0]) and (pos[1] == entity._pos[1]):
          return True

    return False

  def display(self):
    for row in self.getRows():
      print(row)

  def getRows(self):
    room_string = list()
    for row in self._cells:
      row_string = list()
      for cell in row:
        if cell is None:
          row_string.append(' ')
        elif cell._type == 'wall':
          row_string.append('#')
        else:
          row_string.append('.')
      room_string.append(row_string)

      for entity in self._entities.values():
        x, y = entity._pos
        room_string[y][x] = entity._marker

      room_strs = list()
      for row_string in room_string:
        room_strs.append(''.join(row_string))

      return room_strs
