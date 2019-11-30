import sys

class CmdParser(object):
  def __init__(self, player):
    self.player = player

    self.move_commands = list(map(ord, ['w', 's', 'a', 'd']))

  def parseCmd(self, cmd):
    if cmd in self.move_commands:
      self.player.moveCmd(cmd)
    elif cmd == ord('q'):
      sys.exit()
