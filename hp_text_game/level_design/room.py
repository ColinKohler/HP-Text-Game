class Room:

    # Init
    def __init__(self, x_size, y_size):
        self._x_size = x_size
        self._y_size = y_size

        self._cells = [[None]*y_size for _ in xrange(x_size)]

    @classmethod
    def loadRoom(self, room_name):
        i = 0

    # Get and set cells
    def setCell(self, x, y, cell):
        self._cells[x][y] = cell

    def getCell(self, x, y):
        return self._cells[x][y]

    # IO
    def displayCells(self):
        print self._cells
