import pygame

class BaseMovingObject:
    def __init__(self, x, y, width, height, color,
                 text = '', text_color = (0, 0, 0), speed = 5, font = None):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.speed = speed
        self.font = font

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,(
            self.x, self.y, self.width, self.height
        ))
        if self.text and self.font:
            text_surface = self.font.render(str(self.text), True, self.text_color)
            text_rect = text_surface.get_rect(
                center = (self.x + self.width // 2, self.y + self.height // 2)
            )
            surface.blit(text_surface, text_rect)

    def update(self, screen_width, screen_height):
        raise NotImplementedError