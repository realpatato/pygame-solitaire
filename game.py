import pygame
import spritesheet_files.spritesheet_slicer as slicer

pygame.init()

screen=pygame.display.set_mode((1000, 1000))

spritesheet=pygame.image.load("spritesheet_files/playingCards.png")
card_names=[["12S", "13S", "11S", "1S", "10S", "9S", "8S", "7S", "6S", "5S"],
            ["4S", "3S", "2S", "JOKER", "12H", "13H", "11H", "1H", "10H", "9H"],
            ["8H", "7H", "6H", "5H"]]

slicer.parse(spritesheet)

spritesheet_size=spritesheet.get_size()
sprite_w=140
sprite_h=190
sprites=[]

dict={"awesome":1, "peak":2, "sigma":3}
for key in dict:
    print(dict[key])

for col in range(spritesheet_size[0]//sprite_w):
    for row in range(spritesheet_size[1]//sprite_h):
        surface=pygame.Surface((sprite_w, sprite_h), pygame.SRCALPHA)
        surface.blit(spritesheet, (-sprite_w*(col), -sprite_h*(row)))
        surface=pygame.transform.scale(surface, (sprite_w//2, sprite_h//2))
        sprites.append(surface)

playing=True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing=False
    
    for i in range(len(sprites)):
        screen.blit(sprites[i], (15*i, 0))

    pygame.display.update()
    pygame.time.Clock().tick(60)