from .base_object import BaseMovingObject

class MovingVertical(BaseMovingObject):
    def update(self, screen_width, screen_height):
        self.y += self.speed
        # Wrap both directions
        if self.speed > 0 and self.y > screen_height:
            self.y = -self.height
        elif self.speed < 0 and self.y < -self.height:
            self.y = screen_height