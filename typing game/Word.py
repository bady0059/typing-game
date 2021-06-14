class Word:

    def __init__(self, word, x, y, speed):
        self._word = word
        self._x = x
        self._y = y
        self._speed = speed

        self._count = 0

    # move the word one step down
    def step(self):
        self._count += 1
        if self._count == self._speed:
            self._count = 0
            self._y += 1

    def get_word(self):
        return self._word

    def set_x(self, num):
        self._x = num

    def get_x(self):
        return self._x

    def set_y(self, num):
        self._y = num

    def get_y(self):
        return self._y

    def get_speed(self):
        return self._speed
