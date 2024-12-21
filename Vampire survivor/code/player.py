from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self,pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("Vampire survivor", "images", "player", "down", "0.png")).convert_alpha()
        self.rect = self.image.get_rect(center = pos)

    

    def move_right(self):
        self.x += 1
    
    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    