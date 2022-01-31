from .entity import Entity

class Player(Entity):

    def __init__(self, name, hp, mp, faction):
      Entity.__init__(self, name, '@', faction)

      #-----------------#
      # Long-term state #
      #-----------------#
      self.hp = hp
      self.hp_max = hp
      self.mp = mp
      self.mp_max = mp

      self.level = 1;
      self.gold = 0;

      self.stats = dict()
      self.equipment = dict()
      self.spells = list()

    def getPlayerCardStrings(self):
      return [
        self.name,
        self.faction,
        "Health: {}/{}".format(self.hp, self.hp_max),
        "Magic:  {}/{}".format(self.mp, self.mp_max)
      ]
