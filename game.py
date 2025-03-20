import pygame
import spritesheet_files.spritesheet_slicer as slicer

pygame.init()

screen=pygame.display.set_mode((1000, 1000))

spritesheet=pygame.image.load("spritesheet_files/playingCards.png")
card_names=[["12S", "13S", "11S", "1S", "10S", "9S", "8S", "7S", "6S", "5S"],
            ["4S", "3S", "2S", "JOKER", "12H", "13H", "11H", "1H", "10H", "9H"],
            ["8H", "7H", "6H", "5H", "4H", "3H", "2C", "12D", "13D", "11D"],
            ["1D", "10D", "9D", "8D", "7D", "6D", "5D", "4D", "3D", "2D"],
            ["12C", "13C", "11C", "1C", "10C", "9C", "8C", "7C", "6C", "5C"],
            ["4C", "3C", "2H"]]
sprite_w=140
sprite_h=190

sprites=slicer.parse(spritesheet, sprite_w, sprite_h, card_names)

playing=True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing=False
    
    for index, key in enumerate(sprites):
        screen.blit(sprites[key], (15*index, 0))

    pygame.display.update()
    pygame.time.Clock().tick(60)