import copy

class Entity:
  def __init__(self, name, marker, faction):
    self.name = name
    self.marker = marker
    self.faction = faction

    self.pos = None
    self.status_effects = list()

  def addToRoom(self, position, room):
    self.pos = position
    self.room = room

  # Movement controllers
  def moveLeft(self):
    self.moveTo([self.pos[0], self.pos[1]-1])

  def moveLeftUpDiag(self):
    self.moveTo([self.pos[0]+1, self.pos[1]-1])

  def moveUp(self):
    self.moveTo([self.pos[0]+1, self.pos[1]])

  def moveRightUpDiag(self):
    self.moveTo([self.pos[0]+1, self.pos[1]+1])

  def moveRight(self):
    self.moveTo([self.pos[0], self.pos[1]+1])

  def moveRightDownDiag(self):
    self.moveTo([self.pos[0]-1, self.pos[1]+1])

  def moveDown(self):
    self.moveTo([self.pos[0]-1, self.pos[1]])

  def moveLeftDownDiag(self):
    self.moveTo([self.pos[0]-1, self.pos[1]-1])

  def moveTo(self, pos):
    if not self.room.inCollision(pos):
      self.pos = pos
      return True
    else:
      return False
