import sys

class CmdParser(object):
  def __init__(self, ui, player):
    self.ui = ui
    self.player = player

    self.in_target_mode = False

    self.mvmtCmds = [
      ord('h'),
      ord('y'),
      ord('k'),
      ord('u'),
      ord('l'),
      ord('n'),
      ord('j'),
      ord('b')
    ]

  def parseCmd(self, cmd):
    if self.in_target_mode:
      self.parseTargetCmd(cmd)
      return

    if cmd in self.mvmtCmds:
      self.parseMvmtCmd(cmd)
    elif cmd == ord('t'):
      self.in_target_mode = True
      self.ui.setTargetMode()
    elif cmd == ord('c'):
      pass
    elif cmd == ord('q'):
      sys.exit()

  def parseTargetCmd(self, cmd):
    if cmd == ord('h'):
      self.ui.moveTargetLeft()
    elif cmd == ord('y'):
      self.ui.moveTargetLeftUpDiag()
    elif cmd == ord('k'):
      self.ui.moveTargetUp()
    elif cmd == ord('u'):
      self.ui.moveTargetRightUpDiag()
    elif cmd == ord('l'):
      self.ui.moveTargetRight()
    elif cmd == ord('n'):
      self.ui.moveTargetRightDownDiag()
    elif cmd == ord('j'):
      self.ui.moveTargetDown()
    elif cmd == ord('b'):
      self.ui.moveTargetLeftDownDiag()
    elif cmd == ord('e'):
      self.player.setTarget(self.ui.target)
      self.in_target_mode = False
      self.ui.in_target_mode = False
      self.ui.target = None
    elif cmd == ord('q'):
      self.in_target_mode = False
      self.ui.in_target_mode = False

  def parseMvmtCmd(self, cmd):
    if cmd == ord('h'):
      self.player.moveLeft()
    elif cmd == ord('y'):
      self.player.moveLeftUpDiag()
    elif cmd == ord('k'):
      self.player.moveUp()
    elif cmd == ord('u'):
      self.player.moveRightUpDiag()
    elif cmd == ord('l'):
      self.player.moveRight()
    elif cmd == ord('n'):
      self.player.moveRightDownDiag()
    elif cmd == ord('j'):
      self.player.moveDown()
    elif cmd == ord('b'):
      self.player.moveLeftDownDiag()
