import copy

class Entity:
  def __init__(self, name, marker, faction):
    self.name = name
    self.marker = marker
    self.faction = faction

    self.pos = None
    self.status_effects = list()

  def setPosition(self, position):
    self.pos = position
