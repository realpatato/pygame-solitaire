import pygame
import spritesheet_files.spritesheet_slicer as slicer
import deck_manager as dm

pygame.init()

screen=pygame.display.set_mode((1000, 1000))

deck=dm.build_deck()
#deck.shuffle()

for k in range(7):
    for i in range(k, 7):  
        deck._cards[deck._card_pos].set_pos(81*i+18, (18*k)+153)
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
    
    deck.reset_pos()

    pygame.display.update()
    pygame.time.Clock().tick(60)