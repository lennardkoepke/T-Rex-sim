import pygame
import random
import sys
import time

#constants
DINO_SIZE = (100,100)
MEAT_SIZE = (50,50)
SCREEN_WIDTH = (800)
SCREEN_HEIGHT = (600)
BACKGROUND_COLOR = (255, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COUNTDOWN_TIME = (30)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dino Meat Collector')
font = pygame.font.SysFont(None, 36)

img = pygame.image.load("dino.png").convert_alpha()
img = pygame.transform.scale(img, DINO_SIZE)

meat_img = pygame.image.load("meat.png").convert_alpha()
meat_img = pygame.transform.scale(meat_img, MEAT_SIZE)

print("ROAAAR\n move the dino with the arrow keys and eat as much as possible!")
time.sleep(3)
print("lets go!")
time.sleep(0.5)
class Game():
    def __init__(self):
        self.dino_x = 100
        self.dino_y = 100
        self._meat_x = random.randint(0,SCREEN_WIDTH-50)
        self._meat_y = random.randint(0,SCREEN_HEIGHT-50)
        self.score = 0
        self.start_time = time.time()

    def get_meat_position(self):
        return (self._meat_x, self._meat_y)

    def set_meat_position(self):
        self._meat_x = random.randint(0,SCREEN_WIDTH-50)
        self._meat_y = random.randint(0,SCREEN_HEIGHT-50)

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(200)
            elapsed = time.time() - self.start_time
            remaining_time = max(0, int(COUNTDOWN_TIME - elapsed))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.dino_x -= 5
            if keys[pygame.K_RIGHT]:
                self.dino_x += 5
            if keys[pygame.K_UP]:
                self.dino_y -= 5
            if keys[pygame.K_DOWN]:
                self.dino_y += 5

            # Collision Detection
            dino_rect = pygame.Rect(self.dino_x, self.dino_y, *DINO_SIZE)
            meat_rect = pygame.Rect(*self.get_meat_position(), *MEAT_SIZE)

            if dino_rect.colliderect(meat_rect):
                self.set_meat_position()
                self.score += 1

            # Drawing
            screen.fill(BACKGROUND_COLOR)
            screen.blit(img, (self.dino_x, self.dino_y))
            screen.blit(meat_img, self.get_meat_position())

            score_text = font.render(f"Score: {self.score}", True, BLACK)
            timer_text = font.render(f"Time Left: {remaining_time}s", True, BLACK)
            screen.blit(score_text, (10, 10))
            screen.blit(timer_text, (10, 50))

            pygame.display.flip()

            if remaining_time <= 0:
                self.game_over()

        pygame.quit()
        sys.exit()

    def game_over(self):
        print("Times up ⏰")
        print("your score is",self.score)
        if self.score >= 30:
            print("good job the dino is very full now")
        if 20 < self.score < 30:
            print("good start but the dino is still hungry")
        if self.score <= 20:
            print("oh no the dino is straving")
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

Game().run()


