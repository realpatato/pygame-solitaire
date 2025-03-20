#This is the file that handles the parsing/slicing of the cards spritesheet

#First pygame is imported in order to create surfaces and load in images
import pygame

#Function created in order to allow for a more versatile use of the parser, to allow for any file to be parsed;
#assuming each sprite is the same width and height on the spritesheet
def parse(spritesheet, sprite_w, sprite_h, sprite_names, vertical=True):
    '''
        Here's an explanation of all of the parameters:
        spritesheet is an preloaded image file, the image should be your spritesheet;
        sprite_w is the width of each sprite in pixels;
        sprite_h is the height of each sprite in pixels;
        sprite_names is a list of strings used to create a dictionary, with the strings being the keys for each value;
        vertical is will change the how the loop runs, either going up and down or left and right;
    '''
    #creates an empty dictionary that will be filled and then returned
    sprites={}
    #creates a variable in order to store the size of the spritesheet in pixels
    spritesheet_size=spritesheet.get_size()
    #loop for running parsing a spritesheet that runs vertically
    if vertical:
        for col in range(spritesheet_size[0]//sprite_w):
            for row in range(spritesheet_size[1]//sprite_h):
                surface=pygame.Surface((sprite_w, sprite_h), pygame.SRCALPHA)
                surface.blit(spritesheet, (-sprite_w*(col), -sprite_h*(row)))
                surface=pygame.transform.scale(surface, (sprite_w//2, sprite_h//2))
                sprites[sprite_names[col][row]]=surface
    
    return sprites