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
        
    def draw_calibration_pattern(self):
        rect = pygame.Rect(0, 0, config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
        pygame.draw.rect(self.screen, (255, 0, 0), rect, 10)
        center_x = config.SCREEN_WIDTH // 2
        center_y = config.SCREEN_HEIGHT // 2
        pygame.draw.line(self.screen, (255, 0, 0), (center_x - 20, center_y), (center_x + 20, center_y), 2)
        pygame.draw.line(self.screen, (255, 0, 0), (center_x, center_y - 20), (center_x, center_y + 20), 2)