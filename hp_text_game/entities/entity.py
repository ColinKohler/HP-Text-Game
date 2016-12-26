

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
        self._pos = pos
        self._in_room = False

        # Add the entity to the room object if a pos was given
        if room is not None and pos is not None:
            self._room.addEntity(e_id, pos[0], pos[1], self)
            self._in_room = True

    def __repr__(self):
        print self._name

    def addToRoom(self, room, pos):
        if not self._in_room:
            self._room = room
            self._pos = pos
            self._room.addEntity(self._id, pos[0], pos[1], self)
            return True
        else:
            return False

    def castSpell(self, spell, spell_args=list()):
        i = 0

    def hitBySpell(self, spell):
        self._hp -= spell._hp_dmg
        self._status_effects.extend(spell._status_effects)
