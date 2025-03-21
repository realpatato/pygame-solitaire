import pygame

class Card():
    def __init__(self, suit_val, sprites, shown=False):
        self._suit=suit_val[len(suit_val)-1]
        self._val=int(suit_val[:len(suit_val)-1])
        self._shown=shown
        self._sprites=sprites
        self._sprite=self._sprites[bool(self._shown)]
        self._pos=(18, 18)
    
    def set_pos(self, x, y):
        self._pos=(x, y)

    def set_shown(self, new_val):
        self._shown=new_val
    
    def update_sprite(self):
        self._sprite=self._sprites[bool(self._shown)]

    def set_color(self):
        if self._suit == 'C' or self._suit == 'S':
            self._black=True
        else:
            self._black=False

class Ace_Spot():
    def __init__(self, sprite):
        self._sprite=sprite
        self._pos=(0,0)

    def set_pos(self, x, y):
        self._pos=(x, y)