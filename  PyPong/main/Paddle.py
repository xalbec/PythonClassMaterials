import pygame


class Paddle:

    def __init__(self, x, y, screen):
        self.screen = screen
        self.rect = pygame.Rect(x, y, 10, 50)

    def move_up(self):
        self.rect.y -= 3
        if self.collide_with_wall():
            self.rect.y = 0

    def move_down(self):
        self.rect.y += 3
        if self.collide_with_wall():
            self.rect.y = self.screen.get_height() - self.rect.height

    def collide_with_wall(self):
        return self.rect.y + self.rect.height > self.screen.get_height() or self.rect.y < 0

    def display(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect, 0)
