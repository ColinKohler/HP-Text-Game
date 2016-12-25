import time
import curses, curses.textpad

from levels.room import Room
from entities.player import Player

def worldLoop(window):
    room = Room.loadRoom('great_hall')
    player = Player(0, 'Terminus', 100, 100)
    player.addToRoom(room, (12, 9))

    curses.noecho()
    while True:
        max_height, max_width = window.getmaxyx()
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        # Add map to window
        map_h, map_w = room._y_size + 3, room._x_size + 3
        map_y, map_x = 0, 0
        map_window = curses.newwin(map_h, map_w, map_y, map_x)
        room_strs = room.getRows()
        for i, room_str in enumerate(room_strs):
            map_window.addstr(1+i, 3, room_str, curses.color_pair(1))
        map_window.refresh()

        # Add player card to window
        p_card_h, p_card_w = 10, 40
        p_card_y, p_card_x = map_y, map_x + map_w + 3
        p_card_window = curses.newwin(p_card_h, p_card_w, p_card_y, p_card_x)
        p_card_window.box()
        p_card_window.refresh()

        # Add log to window
        log_h, log_w = 11, max_width
        log_y, log_x = max_height - log_h, 0
        log_window = curses.newwin(log_h, log_w, log_y, log_x)
        log_window.box()
        log_window.addstr(1,1,'test')

        # Add textpad to log window
        h, w, y, x = 1, max_width, max_height-1, 1
        log_window.addstr(log_h-1, x-1, '>', curses.color_pair(1))
        log_window.refresh()

        input_window = curses.newwin(h, w, y, x)
        input_box = curses.textpad.Textbox(input_window, insert_mode=True)
        text_input = input_box.edit()

        time.sleep(1.0)

if __name__ == '__main__':
    curses.wrapper(worldLoop)
