from .entity import Entity
import curses, curses.textpad
from ui import curses_utils

class Player(Entity):
  def __init__(self, name, hp, mp, faction, logger):
    Entity.__init__(self, name, '@', faction)

    self.logger = logger

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

    #------------------#
    # Short-term state #
    #------------------#
    self.target = None

  def setTarget(self, target):
    self.target = target

    if self.target:
      self.logger.history.append('{} targets {}.'.format(self.name, self.target.name))

  def cast(self, spell):
    if not self.target:
      return

    self.logger.history.append('{} cast {} at {}.'.format(self.name, spell, self.target.name))

  # Render Junk
  def getPlayerCardStrings(self):
    return [
      self.name,
      self.faction,
      "Health: {}/{}".format(self.hp, self.hp_max),
      "Magic:  {}/{}".format(self.mp, self.mp_max)
    ]

  def render(self, y, x):
    # Add player card to window
    p_card_h, p_card_w = 10, 40
    p_card_y, p_card_x = y, x + 3
    p_card_strs = self.getPlayerCardStrings()
    str_colors = [curses.color_pair(3)] * 2 + \
                 [curses.color_pair(4)] + \
                 [curses.color_pair(5)]
    p_card_window = curses_utils.genTextWindow(p_card_h, p_card_w,
                                               p_card_y, p_card_x,
                                               p_card_strs, str_colors,
                                               y_pad=1, x_pad=1, box=True)
    return p_card_window
