import pygame
import deck_manager as dm
import mouse_handler as mh

pygame.init()

screen=pygame.display.set_mode((592, 810))
pygame.display.set_caption("Solitaire")

deck=dm.build_deck()
ace_spots=dm.spots_build(4)
king_spots=dm.spots_build(7, "king")
deck.shuffle()

for k in range(7):
    if k > 2:
        ace_spots[k-3].set_pos((81*k)+18, 18)
    for i in range(k, 7):  
        if k == 0:
            king_spots[i].set_pos((81*i)+18, (18*k)+131)
        if i == k:
            deck._cards[deck._card_pos].set_shown(True)
        deck._cards[deck._card_pos].set_parent(king_spots[i])
        king_spots[i]._cards.append(deck._cards[deck._card_pos])
        deck.advance_pos()

deck._cards=deck._cards[deck._card_pos:]

for spot in king_spots:
    spot.pile()

playing=True

cur_selection=None
mouse_down=False

while playing:
    mouse_pos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for king_spot in king_spots:
                cur_selection=mh.select_card(king_spot._cards, mouse_pos)
                mouse_down=True
                if cur_selection != None:
                    break
        
        if event.type == pygame.MOUSEBUTTONUP:
            print()
            if cur_selection != None:
                for king_spot in king_spots:
                    on_king_spot=mh.check_pos_king_spot(king_spot._cards, mouse_pos)
                    if on_king_spot:
                        print("Hello")
                        old_king_spot=cur_selection.get_parent()
                        print(old_king_spot._cards)
                        print(king_spot._cards)
                        king_spot._cards.append(cur_selection)
                        old_king_spot._cards.remove(cur_selection)
                        for spot in king_spots:
                            spot.pile()
                        break
            cur_selection=None
            mouse_down=False

        if event.type == pygame.QUIT:
            pygame.quit()
            playing=False
    
    screen.fill((82, 152, 72))

    for king_spot in king_spots:
        screen.blit(king_spot._sprite, king_spot._pos)
        for card in king_spot._cards:
            card.update_sprite()
            screen.blit(card._sprite, card._pos)
    
    for card in deck._cards:
        card.update_sprite()
        screen.blit(card._sprite, card._pos)
    
    for ace_spot in ace_spots:
        screen.blit(ace_spot._sprite, ace_spot._pos)
    
    if mouse_down:
        if cur_selection != None:
            cur_selection.set_pos(mouse_pos[0]-35, mouse_pos[1]-47.5)
            screen.blit(cur_selection._sprite, cur_selection._pos)
    
    deck.reset_pos()

    pygame.display.update()
    pygame.time.Clock().tick(60)