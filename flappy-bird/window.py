
from random import randint
import pygame
# from bird import Bird
from util import Vector, Movable, WINDOW_W, WINDOW_H


class Window:

    surface = None
    bird = None
    pipes = []

    def __init__(self):
        self.setup()
        self.main()

    def setup(self):
        pygame.init()
        self.surface = pygame.display.set_mode((WINDOW_W, WINDOW_H))
        pygame.display.set_caption('TwR Flappy Bird')
        self.bird = Movable(
            pos=Vector(WINDOW_W / 20, WINDOW_H / 2),
            size=Vector(20, 20),
            acc=Vector(0, 0.22)
        )
        self.create_pipes()

    def create_pipes(self):
        """
        pushes list of length 2
        idx 0 - bottom
        idx 1 - top
        """
        j_top = randint(WINDOW_W / 5, WINDOW_H * 3 / 5)  # 300
        j_bottom = j_top + 140  # 340
        self.pipes.append([
            Movable(
                pos=Vector(WINDOW_W + 20, j_bottom),
                size=Vector(50, WINDOW_H - j_bottom),
                vel=Vector(-1.75, 0),
            ),
            Movable(
                pos=Vector(WINDOW_W + 20, 0),
                size=Vector(50, j_top),
                vel=Vector(-1.75, 0)
            )
        ])

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(1)
        self.bird.update()
        for pipes in self.pipes:
            for pipe in pipes:
                if self.bird.pygame_rect.colliderect(pipe.pygame_rect):
                    self.game_over()
                pipe.update()

        # bird corrector
        if self.bird.pos.j > WINDOW_H:
            self.game_over()
        # pipe corrector
        if len(self.pipes):
            first = self.pipes[0][0]
            if first.pos.i + first.size.i < 0:
                self.pipes.pop(0)
            elif first.pos.i < WINDOW_W / 2 and len(self.pipes) < 2:
                self.create_pipes()


        self.handle_keypress()

    def handle_keypress(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.game_over('Bye.')
        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
            self.bird.vel.j = -5


    def game_over(self, msg: str = None):
        print(f'\n{msg or "You Lost. Game Over."}')
        pygame.quit()
        quit()


    def draw(self):
        pygame.display.flip()
        self.draw_background()
        self.draw_bird()
        self.draw_pipes()

    def draw_background(self):
        pygame.draw.rect(self.surface,
                         (69, 135, 148),
                         pygame.Rect(0, 0, WINDOW_W, WINDOW_H))

    def draw_bird(self):
        pygame.draw.rect(self.surface,
                         (203, 208, 72),
                         pygame.Rect(*self.bird.fmt()),)

    def draw_pipes(self):
        for pipes in self.pipes:
            for pipe in pipes:
                pygame.draw.rect(self.surface,
                                 (87, 188, 93),
                                 pygame.Rect(*pipe.fmt()))

    def main(self):
        while 1:
            self.update()
            self.draw()


if __name__ == '__main__':
    Window()