import copy

class Entity:
    def __init__(self, e_id, name, marker, hp, mp, faction, room=None, pos=None):
        self._id = e_id
        self._name = name
        self._marker = marker
        self._max_hp = hp
        self._current_hp = hp
        self._max_mp = mp
        self._current_mp = mp
        self._faction = faction
        self.status_effects = list()

        self._room = room
        self._in_room = False
        self._pos = None
        if room is not None and pos is not None:
            self.addToRoom(room, pos)

    def __repr__(self):
        print(self._name)

    def addToRoom(self, room, pos):
        if not self._in_room:
            self._room = room
            self._pos = list(pos)
            self._room.addEntity(self._id, self)
            return True
        else:
            return False

    def castSpell(self, spell, spell_args=list()):
        i = 0

    def hitBySpell(self, spell):
        self._hp -= spell._hp_dmg
        self._status_effects.extend(spell._status_effects)

    def moveCmd(self, cmd):
      new_pos = copy.copy(self._pos)
      if cmd == ord('w'):
        new_pos[1] -= 1
      elif cmd == ord('s'):
        new_pos[1] += 1
      elif cmd == ord('d'):
        new_pos[0] += 1
      elif cmd == ord('a'):
        new_pos[0] -= 1

      if not self._room.checkCollision(new_pos, self):
        self._pos = new_pos
