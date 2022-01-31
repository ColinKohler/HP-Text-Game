import curses, curses.textpad

# Setup curses window and colors
def setupCurses():
  stdscr = curses.initscr()
  curses.cbreak()
  curses.noecho()
  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
  curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
  curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
  curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)

  return stdscr

# Render the main UI view
def renderMainView(window, level, player, log_strs, get_text_input=False):
  max_height, max_width = window.getmaxyx()

  map_y, map_x, map_h, map_w, map_window = level.render()
  map_window.refresh()

  # Add player card to window
  p_card_h, p_card_w = 10, 40
  p_card_y, p_card_x = map_y, map_x + map_w + 3
  p_card_strs = player.getPlayerCardStrings()
  str_colors = [curses.color_pair(3)] * 2 + \
               [curses.color_pair(4)] + \
               [curses.color_pair(5)]
  p_card_window = genTextWindow(p_card_h, p_card_w,
                                p_card_y, p_card_x,
                                p_card_strs, str_colors,
                                y_pad=1, x_pad=1, box=True)
  p_card_window.refresh()

  # Add log to window
  if get_text_input:
    cmd_h, cmd_w = 11, max_width
    cmd_y, cmd_x = max_height - cmd_h, 0
    str_colors = [curses.color_pair(2)] * len(log_strs)
    input_box, cmd_window = genCommandWindow(cmd_h, cmd_w,
                                             cmd_y, cmd_x,
                                             log_strs, str_colors,
                                             y_pad=1, x_pad=1, box=True)
    cmd_window.refresh()
  else:
    input_box = None

  return input_box

# Init window, add strings, and add box if desired
def genTextWindow(h, w, y, x, strings, colors, y_pad=0, x_pad=0, box=False):
  text_window = curses.newwin(h, w, y, x)
  for i, (string, color) in enumerate(zip(strings, colors)):
    text_window.addstr(y_pad+i, x_pad, string, color)
  if box:
    text_window.box()

  return text_window

def genCommandWindow(h, w, y, x, strings, colors, y_pad=0, x_pad=0, box=False):
  cmd_window = curses.newwin(h, w, y, x)
  if len(strings) <= (h - y_pad*2 - 1):
    for i, (string, color) in enumerate(zip(strings, colors)):
      cmd_window.addstr(y_pad+i, x_pad, string, color)
  else:
    # TODO: Better error handling here
    return False

  # Add textpad to log window
  cmd_window.addstr(h - y_pad - 1, x + x_pad, '>', curses.color_pair(1))
  input_window = curses.newwin(1, w - x_pad*2, y + h - y_pad*2, x + x_pad + 1)
  input_box = curses.textpad.Textbox(input_window, insert_mode=True)

  if box:
    cmd_window.box()

  return input_box, cmd_window
