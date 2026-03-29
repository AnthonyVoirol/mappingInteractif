import pygame
import config

class PygameRenderer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.FULLSCREEN)
        
    def clear_screen(self):
        self.screen.fill(config.COLOR_BLACK)
        
    def draw_balls(self, positions):
        for pos in positions:
            pygame.draw.circle(self.screen, config.COLOR_WHITE, pos, config.BALL_RADIUS)
            
    def update_display(self):
        pygame.display.update()