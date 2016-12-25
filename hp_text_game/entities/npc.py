import os
import yaml

class NPC:

    def __init__(self, e_id, npc_type, room=None, pos=None):
        self._id = e_id
        self._room = room
        self._pos = pos
        self._in_room = False

        self.loadNPCType(npc_type)

        # Add the player to the room object if a pos was given
        if room is not None and pos is not None:
            self._room.addEntity(e_id, pos[0], pos[1], self)
            self._in_room = True

    def loadNPCType(self, npc_type):
        # Setup path to yaml cell descriptors
        npc_path = os.path.abspath(__file__)
        npc_dir = os.path.dirname(npc_path) + '/npc_types/'
        npc_pwd = npc_dir + npc_type + '.yaml'

        # Read data from yaml file
        stream = open(npc_pwd, 'r')
        npc_doc = yaml.load(stream)

        # Load yaml data into python class
        self._name = npc_doc['name']
        self._marker = npc_doc['marker']
        self._hp = npc_doc['hp']
        self._mp = npc_doc['mp']
        self.status_effects = list()
        self._faction = npc_doc['faction']
        self._attitude = npc_doc['attitude']

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

    def hitBySpell(self, spell):
        self._hp -= spell._hp_dmg
        self._status_effects.extend(spell._status_effects)
