class Stun:

    def __init__(self, duration):
        self._duration = duration

    def __repr__(self):
        print('stun')

    def tick(self):
        self._duration -= 1

        return self._duration > 0
