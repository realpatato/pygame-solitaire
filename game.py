import pygame
import spritesheet_files.spritesheet_slicer as slicer
import deck_manager as dm

pygame.init()

screen=pygame.display.set_mode((1000, 1000))

card_names=dm.card_name_build()
card_sprites=dm.sprite_dict_build()
card_sprites_list=dm.sprite_list_build(card_sprites)
deck=dm.build_deck(card_names, card_sprites)
deck.shuffle()

for k in range(7):
    for i in range(k, 7):  
        deck._cards[deck._card_pos].set_pos(81*i, (18*k)+153)
        deck.advance_pos()

playing=True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing=False
    
    screen.fill((0,0,0))
    
    for card in deck._cards:
        screen.blit(card._sprites, card._pos)
    
    deck.reset_pos()

    pygame.display.update()
    pygame.time.Clock().tick(60)