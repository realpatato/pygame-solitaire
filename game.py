import pygame
import spritesheet_files.spritesheet_slicer as slicer
import deck_manager as dm

pygame.init()

screen=pygame.display.set_mode((1000, 1000))

deck=dm.build_deck()
ace_spots=dm.ace_spots_build()
deck.shuffle()

for k in range(7):
    if k > 2:
        ace_spots[k-3].set_pos((81*k)+18, 18)
    for i in range(k, 7):  
        deck._cards[deck._card_pos].set_pos((81*i)+18, (18*k)+131)
        if k == 0:
            ace_spots[i].set_pos((81*k)+18, 131)
        if i == k:
            deck._cards[deck._card_pos].set_shown(True)
        deck.advance_pos()

playing=True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing=False
    
    screen.fill((82,152,72))
    
    for card in deck._cards:
        card.update_sprite()
        screen.blit(card._sprite, card._pos)
    
    for ace_spot in ace_spots:
        screen.blit(ace_spot._sprite, ace_spot._pos)
    
    deck.reset_pos()

    pygame.display.update()
    pygame.time.Clock().tick(60)