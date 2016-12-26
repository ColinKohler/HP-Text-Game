import time
import curses, curses.textpad

import ui_gen
from levels.room import Room
from entities.player import Player
from entities.npc import NPC

def worldLoop(window):
    # Add room, player, and npc to world
    room = Room.loadRoom('great_hall')

    player = Player(0, 'TerminusSTC', 100, 100, 'Slytherin', room, (12, 9))
    h_student = NPC(1, 'student', room, (12,12))

    # Setup curses
    curses.noecho()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)

    log_strs = list()
    while True:
        input_box = renderMainView(window, room, player, log_strs)
        cmd_input = input_box.edit()

        log_strs.append(cmd_input)
        split_input = cmd_input.split()
        spell, spell_args = split_input[0], split_input[1:]
        player.castSpell(spell, spell_args=spell_args)

        time.sleep(1.0)

def renderMainView(window, room, player, log_strs):
    max_height, max_width = window.getmaxyx()

    # Add map to window
    map_h, map_w = room._y_size + 4, room._x_size + 4
    map_y, map_x = 0, 0
    room_strs = room.getRows()
    str_colors = [curses.color_pair(2)] * len(room_strs)
    map_window = ui_gen.genTextWindow(map_h, map_w, map_y, map_x,
                                      room_strs, str_colors,
                                      y_pad=2, x_pad=2, box=True)
    map_window.refresh()

    # Add player card to window
    p_card_h, p_card_w = 10, 40
    p_card_y, p_card_x = map_y, map_x + map_w + 3
    p_card_strs = player.getPlayerCardStrings()
    str_colors = [curses.color_pair(3)] * 2 + \
                 [curses.color_pair(4)] + \
                 [curses.color_pair(5)]
    p_card_window = ui_gen.genTextWindow(p_card_h, p_card_w,
                                         p_card_y, p_card_x,
                                         p_card_strs, str_colors,
                                         y_pad=1, x_pad=1, box=True)
    p_card_window.refresh()

    # Add log to window
    cmd_h, cmd_w = 11, max_width
    cmd_y, cmd_x = max_height - cmd_h, 0
    str_colors = [curses.color_pair(2)] * len(log_strs)
    input_box, cmd_window = ui_gen.genCommandWindow(cmd_h, cmd_w,
                                                cmd_y, cmd_x,
                                                log_strs, str_colors,
                                                y_pad=1, x_pad=1, box=True)
    cmd_window.refresh()

    return input_box

if __name__ == '__main__':
    curses.wrapper(worldLoop)
