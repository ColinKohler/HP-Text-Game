from entity import Entity

class Player(Entity):

    def __init__(self, e_id, name, hp, mp, faction, room=None, pos=None):
        Entity.__init__(self, e_id, name, '@', hp, mp, faction, room=room, pos=pos)

    def getPlayerCardStrings(self):
        return [self._name, self._faction,
                "Health: {}/{}".format(self._current_hp, self._max_hp),
                "Magic:  {}/{}".format(self._current_mp, self._max_mp)]
