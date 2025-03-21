import pygame
import spritesheet_files.spritesheet_slicer as slicer
import deck_builder as db

pygame.init()

screen=pygame.display.set_mode((1000, 1000))

card_names=db.card_name_build()
card_sprites=db.sprite_dict_build()
card_sprites_list=db.sprite_list_build(card_sprites)
deck=db.build_deck(card_names, card_sprites)

playing=True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing=False
    
    for i in range(len(deck)):
        screen.blit(deck[i]._sprites, (15*i, 0))

    pygame.display.update()
    pygame.time.Clock().tick(60)