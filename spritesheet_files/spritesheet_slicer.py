#This is the file that handles the parsing/slicing of the cards spritesheet

#First pygame is imported in order to create surfaces and load in images
import pygame

#Function created in order to allow for a more versatile use of the parser, to allow for any file to be parsed;
#assuming each sprite is the same width and height on the spritesheet
def parse(spritesheet, sprite_w, sprite_h, sprite_names, vertical=True):
    '''
        Here's an explanation of all of the parameters:\n
        spritesheet is an preloaded image file, the image should be your spritesheet\n
        sprite_w is the width of each sprite in pixels;\n
        sprite_h is the height of each sprite in pixels;\n
        sprite_names is a list of strings used to create a dictionary, with the strings being the keys for each value;\n
        vertical is will change the how the loop runs, either going up and down or left and right;
    '''
    #creates an empty dictionary that will be filled and then returned
    sprites={}
    #creates a variable in order to store the size of the spritesheet in pixels
    spritesheet_size=spritesheet.get_size()
    #loop for running parsing a spritesheet that runs vertically
    if vertical:
        #used to iterate over each column, uses the size of the spritesheet divided by the width of each sprite in order to run for each sprite
        for col in range(spritesheet_size[0]//sprite_w):
            #used to iterate over each row, uses the size of the spritesheet divided by the width of each sprite in order to run for each sprite
            for row in range(spritesheet_size[1]//sprite_h):
                #creates a surface with the size of the sprite that will store the image, SCRALPHA gives it a transparent background
                surface=pygame.Surface((sprite_w, sprite_h), pygame.SRCALPHA)
                #draws the spritesheet at a specific point on the surface in surface in order to get only a specific portion of the image, or the sprite
                surface.blit(spritesheet, (-sprite_w*(col), -sprite_h*(row)))
                #scales the image before adding it to the dictionary, comment out if you don't need to scale it
                surface=pygame.transform.scale(surface, (sprite_w//2, sprite_h//2))
                #statement here in a try block in case you don't have enough key's in sprite_names, or if there is empty space in the sprite sheet were a sprite would maybe go
                try:
                    #adds the sprite to sprite list with the given name of the sprite, uses a 2D list, change if you so need
                    sprites[sprite_names[col][row]]=surface
                except IndexError:
                    pass
    #if it's not vertical
    #works identically, just some things are swapped
    else:
        #row and col are swapped, this changes the order that the sprites are iterated over
        for row in range(spritesheet_size[1]//sprite_h):
            for col in range(spritesheet_size[0]//sprite_w):
                #identical
                surface=pygame.Surface((sprite_w, sprite_h), pygame.SRCALPHA)
                surface.blit(spritesheet, (-sprite_w*(col), -sprite_h*(row)))
                surface=pygame.transform.scale(surface, (sprite_w//2, sprite_h//2))
                try:
                    #row and col are swapped, meaning the dictionary key is also different
                    sprites[sprite_names[row][col]]=surface
                except IndexError:
                    pass
    
    #returns the newly created dictionary of sprite
    return sprites