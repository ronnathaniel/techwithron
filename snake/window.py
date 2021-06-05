

import pygame
import random
from util import (
    CELL_W, CELL_H, WINDOW_W, WINDOW_H, Vector, Movable
)


class Window:

    def __init__(self):
        self.setup_pygame()
        self.setup()
        self.main()

    def setup_pygame(self):
        self.surface = pygame.display.set_mode((WINDOW_W, WINDOW_H))
        pygame.display.set_caption('snakers')

    def setup(self):
        self.paused = False
        self.snake: [Movable] = [
            Movable(
                pos=Vector(random.randint(3, 15) * CELL_W, random.randint(3, 15) * CELL_H),
                size=Vector(CELL_W, CELL_H),
                vel=Vector(0, 0),
            )
        ]
        self.create_food()

    def create_food(self):

        for v in self.snake:
            food = Movable(
                pos=Vector(random.randint(1, 19) * CELL_W, random.randint(1, 19) * CELL_H),
                size=Vector(CELL_W, CELL_H)
            )
            if food.pos != v.pos:
                break
        else:
            print('could not cerate food')
            self.game_over()



        self.food = food
        print(self.food)

    def update(self):
        if self.paused:
            return
        pygame.time.Clock().tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                break
        self.check_game_over()
        self.handle_keypress()
        self.check_eat_food()
        for i, v in enumerate(self.snake):
            # for i, v in enumerate(self.snake[:-1:-1]):
            v.update()
            if i:
                v.vel = self.snake[i - 1].vel


    def handle_keypress(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_q]:
            self.game_over()
        elif pressed[pygame.K_SPACE]:
            self.paused = True
        else:
            movement = None
            if (pressed[pygame.K_UP] or pressed[pygame.K_w]) and self.snake[0].vel != Vector(0, CELL_H):
                print('snake[0] vel::', self.snake[0].vel)
                movement = Vector(0, -1)
            if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and self.snake[0].vel != Vector(0, -CELL_H):
                movement = Vector(0, 1)
            if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and self.snake[0].vel != Vector(-CELL_H, 0):
                movement = Vector(1, 0)
            if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and self.snake[0].vel != Vector(CELL_H, 0):
                movement = Vector(-1, 0)
            # if movement:
            # print('calling move_snake() with mvmt:', movement)
            self.move_snake(movement)

    def move_snake(self, movement: Vector = None):
        movement = Vector(*movement.fmt(scalar=CELL_H)) if movement else self.snake[0].vel

        self.snake[0].vel = movement

    def check_eat_food(self):
        if self.snake[0].pos == self.food.pos:
            print('ate food')
            self.eat_food()
            self.create_food()

    def eat_food(self):
        self.snake.insert(
            0,
            Movable(
                pos=self.snake[0].pos.add_components_new(self.snake[0].vel),
                size=Vector(CELL_W, CELL_H),
                vel=self.snake[0].vel,
            )
        )

    def check_game_over(self):
        for i, v in enumerate(self.snake):
            if (
                not (0 <= v.pos.i <= WINDOW_W)
                or
                not (0 <= v.pos.j <= WINDOW_H)
            ):
                self.__init__()
            for j, _v in enumerate(self.snake):
                if (
                    v == _v
                    and
                    i != j
                ):
                    self.__init__()

    def game_over(self):
        pygame.quit()
        quit(0)

    def draw_background(self):
        pygame.draw.rect(self.surface, (0, 0, 0), pygame.Rect(
            0, 0, WINDOW_W, WINDOW_H,
        ))

    def draw_lines(self):
        for i in range(1, 20, 1):
            offset = i * CELL_W

            pygame.draw.line(self.surface, (255, 255, 255),
                             (offset, 0), (offset, WINDOW_H), 1)
            pygame.draw.line(self.surface, (255, 255, 255),
                             (0, offset), (WINDOW_W, offset), 1)

            # print((offset, 0), (offset, WINDOW_H))
            # print((0, offset), (WINDOW_W, offset))

    def draw_snake(self):
        for v in self.snake:
            pygame.draw.rect(self.surface, (0, 255, 0),
                             pygame.Rect(*v.pygame_rect))

    def draw_food(self):
        pygame.draw.rect(self.surface, (255, 0, 0),
                         pygame.Rect(*self.food.pygame_rect))

    def draw(self):
        pygame.display.flip()
        self.draw_background()
        self.draw_lines()
        self.draw_snake()
        self.draw_food()

    def main(self):
        while 1:
            self.update()
            self.draw()

if __name__ == '__main__':
    Window()