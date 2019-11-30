import time
import curses, curses.textpad

import ui
from levels.room import Room
from entities.player import Player
from entities.npc import NPC
from cmd_parser import CmdParser

def worldLoop(window):
    # Add room, player, and npc to world
    room = Room.loadRoom('great_hall')

    player = Player(0, 'TerminusSTC', 100, 100, 'Slytherin', room, (12, 9))
    h_student = NPC(1, 'student', room, (12,12))

    screen = ui.setupCurses()
    cmd_parser = CmdParser(player)
    log_strs = list()
    while True:
        input_box = ui.renderMainView(window, room, player, log_strs, get_text_input=True)
        cmd = screen.getch()
        cmd_parser.parseCmd(cmd)

        #cmd_input = input_box.edit()

        #split_input = cmd_input.split()
        #spell, spell_args = split_input[0], split_input[1:]
        #player.castSpell(spell, spell_args=spell_args)

        #log_strs.append(chr(cmd))

if __name__ == '__main__':
    curses.wrapper(worldLoop)
