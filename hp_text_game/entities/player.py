class Player:

    def __init__(self, e_id, name, hp, mp, room=None, pos=None):
        self._id   = e_id
        self._name = name
        self._marker = '@'
        self._hp = hp
        self._mp = mp
        self.status_effects = list()
        self._room = room
        self._pos = pos
        self._in_room = False

        # Add the player to the room object if a pos was given
        if room is not None and pos is not None:
            self._room.addEntity(e_id, pos[0], pos[1], self)
            self._in_room = True

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
