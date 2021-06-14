import pygame
from TextInput import TextInput


class GUI:

    def __init__(self, title, width=900, height=500):
        self._width = width
        self._height = height
        self._screen = pygame.display.set_mode([width, height])
        self._textinput = TextInput()
        self._hearts = 3
        self._score = 0

        pygame.display.set_caption(title)

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score

    def get_hearts(self):
        return self._hearts

    def set_hears(self, num):
        self._hearts = num

    # display all the hears
    def display_hearts(self):
        img = pygame.image.load('heart.png')
        x = 750
        y = 20
        for heart in range(self._hearts):
            self._screen.blit(img, (x, y))
            x += 40

    # get the text input
    def get_textInput(self):
        return self._textinput

    # get the screen
    def get_screen(self):
        return self._screen

    # make a frame
    def get_frame(self, events, words):
        self._screen.fill((0, 0, 0))  # background
        for word in words:  # display all the words and step them
            self.text('freesansbold.ttf', 32, word.get_x(), word.get_y(), word.get_word(), (100, 200, 0))
            word.step()
        self._textinput.update(events)
        self._screen.blit(self._textinput.get_surface(), (375, 450))
        self.display_hearts()
        self.text('freesansbold.ttf', 32, 760, 80, str(self._score), (100, 70, 200)) # score

    # display text on the screen
    def text(self, fontFace, size, x, y, text, colour):
        font = pygame.font.Font(fontFace, size)
        text = font.render(text, 1, colour)
        self._screen.blit(text, (x, y))

    # lost
    def lost(self, max_score):
        self._screen = pygame.display.set_mode([self._width, self._height])
        self._screen.fill((0, 0, 0))
        self.text('freesansbold.ttf', 32, 100, 100, ("You lost your score is " + str(self._score)), (0, 200, 8))
        self.text('freesansbold.ttf', 32, 100, 150, ("Best score: "+str(max_score)), (100, 50, 20))  # max score
        pygame.display.update()
