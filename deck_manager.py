import pygame
import random
import cards as cards
import spritesheet_files.spritesheet_slicer as slicer

class Deck():
    def __init__(self, cards):
        self._cards=cards
        self._card_pos=0

    def shuffle(self, count=1000):
        for i in range(count):
            card_pos_a=random.randint(0, 51)
            card_pos_b=random.randint(0, 51)
            temp=self._cards[card_pos_a]
            self._cards[card_pos_a]=self._cards[card_pos_b]
            self._cards[card_pos_b]=temp
    
    def advance_pos(self):
        self._card_pos+=1
    
    def reset_pos(self):
        self._card_pos=0

def card_name_build():
    '''
        creates a list of all of the card names in order
    '''
    #creates a list of the possible suits
    suits=['C', 'D', 'H', 'S']
    #creates an empty list which will store the names of the cards
    card_names=[]
    #loops over each item in suits
    for suit in suits:
        #and pairs each item with a number 1-13
        for i in range(13):
            #adds suit_val/card name to list of card names
            card_names.append(str(i+1)+suit)
    #returns the newly created list
    return card_names

def sprite_dict_build():
    '''
        creates the dictionary of sprites using the slicer functions
    '''
    #loads in the spritesheet
    spritesheet=pygame.image.load("spritesheet_files/playingCards.png")
    #creates a list of the card names in the order they appear in the spritesheet
    card_names=[["12S", "13S", "11S", "1S", "10S", "9S", "8S", "7S", "6S", "5S"],
            ["4S", "3S", "2S", "JOKER", "12H", "13H", "11H", "1H", "10H", "9H"],
            ["8H", "7H", "6H", "5H", "4H", "3H", "2C", "12D", "13D", "11D"],
            ["1D", "10D", "9D", "8D", "7D", "6D", "5D", "4D", "3D", "2D"],
            ["12C", "13C", "11C", "1C", "10C", "9C", "8C", "7C", "6C", "5C"],
            ["4C", "3C", "2H"]]
    #calling the slicer parse function
    card_sprites=slicer.parse(spritesheet, 140, 190, card_names)
    #returns the dictionary of sprites
    return card_sprites

def sprite_list_build(sprite_dict, card_names=card_name_build()):
    '''
        creates a organized list of the sprites, using a dictionary and a list of names
    '''
    #empty list to store the list of sprites
    sprite_list=[]
    #iterates over each name in list of names
    for name in card_names:
        #adds sprite to list
        sprite_list.append(sprite_dict[name])
    #returns the newly created list of sprites
    return sprite_list

def build_deck(sprite_name_list, sprite_dict):
    '''
        "Builds" the deck, probably temp and should probably use a deck class
    '''
    #empty list to contain the cards in the deck
    deck=[]
    #iterates over each str in the name list
    for sprite_str in sprite_name_list:
        #adds a card object to deck with suit_val and sprite
        deck.append(cards.Card(sprite_str, sprite_dict[sprite_str]))
    deck=Deck(deck)
    return deck