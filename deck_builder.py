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
    card_names=[["12S", "13S", "11S", "1S", "10S", "9S", "8S", "7S", "6S", "5S"],
            ["4S", "3S", "2S", "JOKER", "12H", "13H", "11H", "1H", "10H", "9H"],
            ["8H", "7H", "6H", "5H", "4H", "3H", "2C", "12D", "13D", "11D"],
            ["1D", "10D", "9D", "8D", "7D", "6D", "5D", "4D", "3D", "2D"],
            ["12C", "13C", "11C", "1C", "10C", "9C", "8C", "7C", "6C", "5C"],
            ["4C", "3C", "2H"]]
    card_sprites=slicer.parse(spritesheet, 140, 190, card_names)
    return card_sprites

def sprite_list_build(sprite_dict, card_names=card_name_build()):
    sprite_list=[]
    for name in card_names:
        sprite_list.append(sprite_dict[name])
    return sprite_list

def build_deck(sprite_list, sprite_dict):
    deck=[]
    for sprite_str in sprite_list:
        deck.append(cards.Card(sprite_str, sprite_dict[sprite_str]))
    return deck