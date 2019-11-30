import os
import yaml

from .entity import Entity

class NPC(Entity):

    def __init__(self, e_id, npc_type, room=None, pos=None):
        name, marker, hp, mp, faction, attitude = self.loadNPCType(npc_type)
        Entity.__init__(self, e_id, name, marker, hp, mp, faction, room=room, pos=pos)

    def loadNPCType(self, npc_type):
        # Setup path to yaml cell descriptors
        npc_path = os.path.abspath(__file__)
        npc_dir = os.path.dirname(npc_path) + '/npc_types/'
        npc_pwd = npc_dir + npc_type + '.yaml'

        # Read data from yaml file
        stream = open(npc_pwd, 'r')
        npc_doc = yaml.load(stream)

        # Return yaml data
        return npc_doc['name'], npc_doc['marker'], \
               npc_doc['hp'], npc_doc['mp'], \
               npc_doc['faction'], npc_doc['attitude']
