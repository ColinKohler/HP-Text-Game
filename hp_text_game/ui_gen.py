import curses, curses.textpad

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
