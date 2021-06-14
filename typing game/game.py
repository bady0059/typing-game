import socket
import time
import threading

from Word import Word
import keyboard
import pygame
import random

from GUI import GUI

file = open("words.txt", encoding="utf8")  # open file
num_lines = len(file.readlines())  # number of lines in file


# return random word from file
def get_text():
    file.seek(0)
    lines = file.readlines()
    return lines[random.randint(0, num_lines)]


# check for lost
def lost(words, gui):
    for word in words:
        if word.get_y() > 500:  # word escaped
            replace(words, word)
            gui.set_hears(gui.get_hearts() - 1)  # less one heart
            if gui.get_hearts() == 0:
                return False, words.clear()  # out of hearts
    return True, words


# replace typed word in new word
def replace(words, word):
    words.remove(word)
    words.append(Word(get_text()[:-1], random.randint(0, 700), 0, random.randint(2, 10)))
    return words


# check if word was typed and replace her
def change_words(gui, words):
    for word in words:
        if word.get_word() == gui.get_textInput().get_text():
            gui.set_score(gui.get_score() + len(word.get_word()))
            words = replace(words, word)
            gui.get_textInput().clear_text()
    return words


# connect to server
def connect(gui):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 4483))
    max_score = int(s.recv(128).decode())  # get the max score
    print(max_score)
    return s, max_score


def main():
    pygame.init()

    gui = GUI("typing game", 900, 500)
    screen = gui.get_screen()

    # connection
    s, max_score = connect(gui)

    # starts with 2 words
    words = [Word(get_text()[:-1], 50, 50, 10), Word(get_text()[:-1], 100, 100, 8)]

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        words = change_words(gui, words)  # update words
        gui.get_frame(events, words)  # get the frame
        running, words = lost(words, gui)
        pygame.display.update()

        if int(gui.get_score()) > max_score: # send score if it broken
            max_score = gui.get_score()
            s.sendall(str(max_score).encode())

    gui.lost(max_score)
    time.sleep(5)
    s.close()
    pygame.quit()


if __name__ == "__main__":
    main()
