
import pygame as pg
from .. import tools

class Controls(tools.States):
    def __init__(self, screen_rect):
        tools.States.__init__(self)
        self.screen_rect = screen_rect
        self.listings = [
            #'W = Left Paddle move up',
            #'S = Left Paddle move down',
            'Up Arrow = Right paddle move up',
            'Down Arrow = Right paddle move down',
            'Esc = Go to main menu',
            'P = Pause game'
        ]
        self.options = ['Back']
        self.next_list = ['MENU']
        self.title, self.title_rect = self.make_text('Controls', (75,75,75), (self.screen_rect.centerx, 75), 150)
        self.pre_render_options()
        self.pre_render_listings()
        self.from_bottom = 400
        self.from_bottom_listings = 225
        self.spacer = 25
        self.movement_image = pg.image.load('resources/graphics/movement.png').convert_alpha()
        self.movement_image_rect = self.movement_image.get_rect(center=(self.screen_rect.centerx, 150))
    
    def get_event(self, event, keys):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                #self.button_sound.sound.play()
                self.done = True
                self.next = 'MENU'
        self.mouse_menu_click(event)

    def update(self, now, keys):
        pg.mouse.set_visible(True)
        self.mouse_hover_sound()

    def render(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.title,self.title_rect)
        screen.blit(self.movement_image, self.movement_image_rect)
        for i,opt in enumerate(self.rendered["des"]):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom+i*self.spacer)
            if opt[1].collidepoint(pg.mouse.get_pos()):
                rend_img,rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                screen.blit(rend_img,rend_rect)
            else:
                screen.blit(opt[0],opt[1])
        for i,opt in enumerate(self.rendered_listing['des']):
            opt[1].center = (self.screen_rect.centerx, self.from_bottom_listings + i * self.spacer)
            screen.blit(opt[0],opt[1])
                
    def make_text(self,message,color,center,size):
        font = pg.font.Font("resources/fonts/Megadeth.ttf", size)
        text = font.render(message,True,color)
        rect = text.get_rect(center=center)
        return text,rect
        
    def pre_render_listings(self):
        listing_text = pg.font.Font("resources/fonts/impact.ttf",25)
        rendered_msg = {"des":[],"sel":[]}
        for listing in self.listings:
            text = listing_text.render(listing, 1, (255,255,255))
            text_rect = text.get_rect()
            rendered_msg["des"].append((text, text_rect))
        self.rendered_listing = rendered_msg
        
    def pre_render_options(self):
        font_deselect = pg.font.Font("resources/fonts/Megadeth.ttf",50)
        font_selected = pg.font.Font("resources/fonts/Megadeth.ttf",75)

        rendered_msg = {"des":[],"sel":[]}
        for option in self.options:
            d_rend = font_deselect.render(option, 1, (255,255,255))
            d_rect = d_rend.get_rect()
            s_rend = font_selected.render(option, 1, (255,0,0))
            s_rect = s_rend.get_rect()
            rendered_msg["des"].append((d_rend,d_rect))
            rendered_msg["sel"].append((s_rend,s_rect))
        self.rendered = rendered_msg

    def cleanup(self):
        pass
        
    def entry(self):
        pass
