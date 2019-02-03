import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

 #COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
#rainyhearts.ttf
#PrStart.ttf
#prstartk.ttf
font = pygame.font.Font("resources/prstartk.ttf", 14)


class Sprite(pygame.sprite.Sprite):
	
    def __init__(self, imagelist, startpos, show=False):
        pygame.sprite.Sprite.__init__(self)
        #self.image = image
        self.imagelist = imagelist
        self.surface = pygame.Surface([10, 10])
        self.rect = self.surface.get_rect()
        #self.rect.bottom = 0
        #self.startpos = startpos
        self.frame = 0
        self.show = show
        self.go_to(startpos[0], startpos[1])

    def draw(self):
        if self.show:
            image = self.imagelist[self.frame]
            screen.blit(image, self.rect.topleft)

    def next_frame(self):
        if self.frame >= len(self.imagelist) - 1:
            self.frame = 0
        else:
            self.frame += 1

    def go_to(self, x, y):
        self.rect.centerx = x
        self.rect.bottom = y



class Map():

    def __init__(self, image, scrolling):
        self.image = image
        self.surface = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.rect = self.surface.get_rect()
        self.scrolling = scrolling

    def draw(self):
        screen.blit(self.image, self.rect.topleft)



class TextBox(Sprite):
    
    def __init__(self, imagelist, startpos, show, textcolor):
        Sprite.__init__(self, imagelist, startpos, show)
        self.textcolor = textcolor
        self.pos = startpos
        self.rect.topleft = self.pos
        self.text = ""

    def update(self):
        '''
        self.draw()
        pygame.display.update()
        dialogue_text = font.render(self.text, True, self.textcolor)
        text_x = self.pos[0] + 20
        text_y = self.pos[1] + 20
        screen.blit(dialogue_text, [text_x, text_y])
        pygame.display.update()
        '''
        self.draw()
        pygame.display.update()
        #dialogue_text = font.render(self.text, True, self.textcolor)
        text_x = self.pos[0] + 20
        text_y = self.pos[1] + 20
        for i in range(len(self.text)):
            dialogue_text = font.render(self.text[i], True, self.textcolor)
            screen.blit(dialogue_text, [text_x, text_y])
            text_y += 15
        pygame.display.update()



class Mode():
    
    def __init__(self, name, ordered_events, running_events, running_events_incomplete):
        self.name = name
        self.ordered_events = ordered_events
        self.running_events = running_events
        self.running_events_incomplete = running_events_incomplete



class Event():
    
    def __init__(self, name, trigger_map, trigger_range):
        self.name = name
        self.trigger_map = trigger_map
        self.trigger_range = trigger_range
        #self.complete = False






















