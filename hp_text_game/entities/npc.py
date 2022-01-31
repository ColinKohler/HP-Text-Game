import os
import yaml

from .entity import Entity

class NPC(Entity):
  def __init__(self, npc_type):
    name, marker, hp, faction, attitude = self.loadNPCType(npc_type)
    super().__init__(name, marker, faction)

    self.hp = hp
    self.hp_max = hp

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
           npc_doc['hp'], \
           npc_doc['faction'], npc_doc['attitude']
