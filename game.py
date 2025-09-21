import pygame, random
from utils.config import *
from utils.colors import WHITE, PALETTE
from rules.addition_rule import AdditionRule
from objects.horizontal import MovingHorizontal
from objects.vertical import MovingVertical

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Logic tung hoành')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FONT_PATH, FONT_SIZE)

        # Rule preparation
        self.rule = AdditionRule()
        self.horizontal_groups = []
        self.vertical_groups = []
        self._generate_objects()

    def _generate_objects(self):
        # Create 8 lines
        for i in range(8):
            data = self.rule.generate(length = 6, is_horizontal = True)
            texts = data['sequence']
            row = []
            for j, text in enumerate(texts):
                obj = MovingHorizontal(
                    x = j * 150, y = 25 + i * 75,
                    width = 100, height = 50,
                    color = random.choice(PALETTE),
                    text = text,
                    speed = 5 * (1 if i % 2 == 0 else -1),
                    font = self.font
                )
                row.append(obj)
            self.horizontal_groups.append(row)

        # Create 5 columns
        for i in range(5):
            data = self.rule.generate(length = 5, is_horizontal = False)
            texts = data['sequence']
            col = []
            for j, text in enumerate(texts):
                obj = MovingVertical(
                    x = 100 + i * 150, y = j * 150,
                    width = 50, height = 100,
                    color = random.choice(PALETTE),
                    text = text,
                    speed = 5 * (1 if i % 2 == 0 else -1),
                    font = self.font
                )
                col.append(obj)
            self.vertical_groups.append(col)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            self.screen.fill(WHITE)

            for group in self.horizontal_groups:
                for obj in group:
                    obj.update(SCREEN_WIDTH, SCREEN_HEIGHT)
                    obj.draw(self.screen)

            for group in self.vertical_groups:
                for obj in group:
                    obj.update(SCREEN_WIDTH, SCREEN_HEIGHT)
                    obj.draw(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)