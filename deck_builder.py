import pygame
import cards as cards
import spritesheet_files.spritesheet_slicer as slicer

def card_name_build():
    suits=['C', 'D', 'H', 'S']
    card_names=[]
    for suit in suits:
        for i in range(13):
            card_names.append(str(i+1)+suit)
    return card_names

def sprite_dict_build():
    spritesheet=pygame.image.load("spritesheet_files/playingCards.png")

def sprite_list_build(sprite_dict, card_names=card_name_build()):
    sprite_list=[]
    for name in card_names:
        sprite_list.append(sprite_dict[name])
    return sprite_list