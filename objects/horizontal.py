from .base_object import BaseMovingObject

class MovingHorizontal(BaseMovingObject):
    def update(self, screen_width, screen_height):
        self.x += self.speed

        # Wrap both directions on the X‐axis
        if self.speed > 0 and self.x > screen_width:
            self.x = -self.width
        elif self.speed < 0 and self.x < -self.width:
            self.x = screen_width