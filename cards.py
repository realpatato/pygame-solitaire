import pygame

class Card():
    def __init__(self, suit, val, sprites, shown=True):
        self._suit=suit
        self._val=val
        self._sprites=sprites
        self._shown=shown
    
    def set_color(self):
        if self._suit == 'C' or self._suit == 'S':
            self._black=True
        else:
            self._black=False