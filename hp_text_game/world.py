import time
import curses, curses.textpad

from ui.ui import UI
from levels.level import Level
from entities.player import Player
from entities.npc import NPC
from cmd_parser import CmdParser

def worldLoop(window):
    # Add room, player, and npc to world
    level = Level()
    level.generateLevel()

    player = Player('TerminusSTC', 100, 100, 'Slytherin')
    level.addEntityToRoom(player, 'great_hall', [12, 9])

    h_student = NPC('student')
    level.addEntityToRoom(h_student, 'great_hall', [12, 12])

    ui = UI(window, player, level)
    cmd_parser = CmdParser(ui, player, level)
    log_strs = list()
    while True:
      ui.render(log_strs)
      cmd = ui.getCommand()
      cmd_parser.parseCmd(cmd)
      #log_strs.append(cmd)

if __name__ == '__main__':
  curses.wrapper(worldLoop)
