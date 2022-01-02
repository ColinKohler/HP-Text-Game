import sys

class CmdParser(object):
  def __init__(self, player):
    self.player = player

    self.move_commands = list(map(ord, ['w', 's', 'a', 'd']))

  def parseCmd(self, cmd):
    if cmd in self.move_commands:
      self.player.moveCmd(cmd)
    elif cmd == 'c':
      split_input = cmd_input.split()
      spell, spell_args = split_input[1], split_input[2:]
      player.castSpell(spell, spell_args=spell_args)
    elif cmd == ord('q'):
      sys.exit()
