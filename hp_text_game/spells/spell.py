import os
import yaml

from ..status_effects.stun import Stun

class Spell:

    def __init__(self, spell_name):
        # Setup path to yaml spell descriptors
        spell_path = os.path.abspath(__file__)
        spell_dir = os.path.dirname(spell_path) + '/defined_spells/'
        spell_pwd = cell_dir + spell_name + '.yaml'

        # Read data from yaml file
        stream = open(cell_pwd, 'r')
        spell_doc = yaml.load(stream)

        # Load yaml data into python class
        self._name = spell_doc['name']
        self._type = spell_doc['type']
        self._mp_cost = spell_doc['mp_cost']
        self._hp_dmg  = spell_doc['hp_dmg']
        self._status_effects = list()
        for effect_doc in spell_doc['status_effects']:
            self.addEffect(effect_doc['name'], effect_doc['duration'])

    def __repr__(self):
        return self._name

    def addEffect(self, effect_name, duration):
        if effect_name == 'stun':
            stun_effect = Stun(duration)
            self._status_effects.append(stun_effect)
        else:
            return
