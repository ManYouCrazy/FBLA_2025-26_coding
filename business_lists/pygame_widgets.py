import pygame

pygame.init()

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, pos, action=None, secondary_action=None):
        self.pos = pos
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.secondary_action = secondary_action
        self.font = pygame.font.Font(None, 30) 
        self.isflagged = False

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.color

        if self.rect.collidepoint(mouse_pos):
            current_color = self.hover_color

        pygame.draw.rect(screen, current_color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255)) # White text
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Left click
            if self.rect.collidepoint(event.pos):
                if self.action and not self.isflagged:
                    self.action()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2: # Right click
            if self.rect.collidepoint(event.pos):
                if self.secondary_action and not self.isflagged:
                    self.secondary_action()

    def get_coords(self):
        return self.pos

    
    

def draw_flag(screen,x,y,size):
    flag_points = [(x,y-(20*size)),(x+(10*size),y-(15*size)),(x,y-(10*size)),(x,y+(3*size))]
    pygame.draw.polygon(screen,(255, 255, 255),flag_points,5)

class text:
    def __init__(self,screen,x,y,size,text,color=(0,0,0),font="arial"):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = size
        self.font = font
        self.text = str(text)
        self.color = color
        self.renderer = pygame.font.SysFont(self.font,self.size)

    def render(self):
        surf = self.renderer.render(self.text, True, self.color)
        self.screen.blit(surf,(self.x,self.y))

    def texts(self):
        self.text = "huh"

class shape:
    def __init__(self,screen, initial_points, fill_color=(255,255,255), line_color = (255,255,255),line_thickness = 0):
        self.screen = screen
        self.points = initial_points
        self.fill = fill_color
        self.line = line_color
        self.thickness = line_thickness

    def draw_shape(self):
        pygame.draw.polygon(self.screen,self.line,self.points,self.thickness)