import pygame

class Card():
    def __init__(self, suit_val, sprites, parent="placeholder", shown=False):
        self._suit=suit_val[len(suit_val)-1]
        self._val=int(suit_val[:len(suit_val)-1])
        self._parent=parent
        self._shown=shown
        self._sprites=sprites
        self._sprite=self._sprites[bool(self._shown)]
        self._pos=(18, 18)
    
    def set_pos(self, x, y):
        self._pos=(x, y)

    def set_shown(self, new_val):
        self._shown=new_val
    
    def set_parent(self, parent):
        self._parent=parent

    def get_parent(self):
        return self._parent
    
    def update_sprite(self):
        self._sprite=self._sprites[bool(self._shown)]

    def set_color(self):
        if self._suit == 'C' or self._suit == 'S':
            self._black=True
        else:
            self._black=False
    
    def __str__(self):
        return "card is at "+str(self._pos)+" and has a suit val of "+self._suit+str(self._val)

class Spot():
    def __init__(self, sprite):
        self._sprite=sprite
        self._pos=(0,0)
        self._cards=[]

    def set_pos(self, x, y):
        self._pos=(x, y)

class Ace_Spot(Spot):
    pass

class King_Spot(Spot):
    def pile(self):
        for i in range(len(self._cards)):
            self._cards[i].set_pos(self._pos[0], self._pos[1]+(18*i))