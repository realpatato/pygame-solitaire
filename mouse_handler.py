import pygame

def select_card(cards, mouse_pos):
    select_card=None
    for i in range(len(cards)):
        if (mouse_pos[0] >= cards[i]._pos[0]) and (mouse_pos[0] <= cards[i]._pos[0]+70):
            if (mouse_pos[1] >= cards[i]._pos[1]) and (mouse_pos[1] <= cards[i]._pos[1]+95):
                if cards[i]._shown:
                    select_card=cards[i]
    return select_card

def check_pos_king_spot(cards, mouse_pos):
    try:
        if (mouse_pos[0] >= cards[-1]._pos[0]) and (mouse_pos[0] <= cards[-1]._pos[0]+70):
            if (mouse_pos[1] >= cards[-1]._pos[1]+10) and (mouse_pos[1] <= cards[-1]._pos[1]+105):
                return True
        else:
            return False
    except IndexError:
        pass
        if cards == []:
            print("King spot empty")