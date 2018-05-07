import pygame


class Ball:

    def __init__(self, x, y, vx, vy, screen):
        self.rect = pygame.Rect(x, y, 5, 5)
        self.vx = vx
        self.vy = vy
        self.screen = screen

    def display(self):
        pygame.draw.rect(self.screen, [255, 0, 0], self.rect)

    def move(self):
        # checks to see if the screens bounds we passed
        self.collides_with_screen()

        self.rect = self.rect.move(self.vx, self.vy)

    def collides_with_screen(self):
        if self.rect.x < 0 or self.rect.x + self.rect.w > self.screen.get_width():
            self.vx *= -1
        if self.rect.y < 0 or self.rect.y + self.rect.h > self.screen.get_height():
            self.vy *= -1

    def is_colliding_with_left_goal(self):
        return self.rect.x < 0

    def is_colliding_with_right_goal(self):
        return self.rect.x + self.rect.w > self.screen.get_width()
