import curses, curses.textpad
from ui import curses_utils

class UI(object):
  def __init__(self, window, player, level):
    self.window = window
    self.player = player
    self.current_level = level
    self.max_height, self.max_width = self.window.getmaxyx()

    # Setup curses window and colors
    self.screen = curses.initscr()

    curses.cbreak()
    curses.noecho()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)

    self.in_target_mode = False
    self.target = None

  def getCommand(self):
    return self.screen.getch()

  # Render the main UI view
  def render(self, log_strs):
    map_y, map_x, map_h, map_w, map_window = self.current_level.render(self.target)
    map_window.refresh()

    # Add player card to window
    p_card_window = self.player.render(map_y, map_x + map_w)
    p_card_window.refresh()

    # Add input box to window
    cmd_window = self.renderCmdWindow(log_strs)
    cmd_window.refresh()

  def renderCmdWindow(self, log_strs):
    cmd_h, cmd_w = 11, self.max_width
    cmd_y, cmd_x = self.max_height - cmd_h, 0
    str_colors = [curses.color_pair(2)] * len(log_strs)
    input_box, cmd_window = curses_utils.genCommandWindow(cmd_h, cmd_w,
                                                          cmd_y, cmd_x,
                                                          log_strs, str_colors,
                                                          y_pad=1, x_pad=1, box=True)

    return cmd_window

  def setTargetMode(self):
    self.in_target_mode = True
    self.target = self.player.pos

  def setTarget(self, pos):
    self.target = pos

  def moveTargetLeft(self):
    self.setTarget([self.target[0], self.target[1]-1])

  def moveTargetLeftUpDiag(self):
    self.setTarget([self.target[0]+1, self.target[1]-1])

  def moveTargetUp(self):
    self.setTarget([self.target[0]+1, self.target[1]])

  def moveTargetRightUpDiag(self):
    self.setTarget([self.target[0]+1, self.target[1]+1])

  def moveTargetRight(self):
    self.setTarget([self.target[0], self.target[1]+1])

  def moveTargetRightDownDiag(self):
    self.setTarget([self.target[0]-1, self.target[1]+1])

  def moveTargetDown(self):
    self.setTarget([self.target[0]-1, self.target[1]])

  def moveTargetLeftDownDiag(self):
    self.setTarget([self.target[0]-1, self.target[1]-1])
