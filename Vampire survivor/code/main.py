from settings import *



class Game():
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        pygame.display.set_caption("Surviva!")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            #dt

            dt = self.clock.tick() / 1000

            #event loop

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
        pygame.quit()





if __name__=="__main__":
        
    game = Game()

    game.run()


