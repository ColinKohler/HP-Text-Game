import yaml
import os

class Cell:

    # Init
    def __init__(self, cell_type):
        # Setup path to yaml cell descriptors
        cell_path = os.path.abspath(__file__)
        cell_dir = os.path.dirname(cell_path) + '/cell_types/'
        cell_pwd = cell_dir + cell_type + '.yaml'

        # Read data from yaml file
        stream = open(cell_pwd, 'r')
        cell_doc = yaml.load(stream)

        # Load yaml data into python class
        self._name = cell_doc['name']
        self._type = cell_doc['type']
        self._modifiers = cell_doc['modifiers']

    def __repr__(self):
        return self._name
