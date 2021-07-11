import pygame
import random

pygame.init()

size = (800, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Rhythm")

running = True
clock = pygame.time.Clock()

blocks = list()
panjung = list()


class Block:
    def __init__(self, pos):
        self.rect = pygame.Rect(100 * pos, 0, 100, 40)
        self.color = [0, 0, 255]
        self.position = [100 * pos, 0]
        self.num = pos
        self.move = 5

    def hitcheck(self, col):
        print(col, self.num)

        if self.num == col and self.position[1] <= 700 and self.position[1] >= 500:
            print("del")
            blocks[self.num].remove(self)

    def update(self):
        self.position[1] += self.move

        self.rect.top = self.position[1]
        # self.hitcheck(self.num)
        if self.position[1] > 700:
            self.move = 1
            self.color = (255, 0, 0)
        if self.position[1] >= 800 + 40:
            blocks[self.num].remove(self)
            print("del!")
            del self


class Columb(Block):
    def __init__(self, pos):
        self.rect = pygame.Rect(100 * pos, 0, 100, size[1])
        self.color = [255, 255, 255]

    def update(self):
        for i, j in enumerate(self.color):
            if j <= 0:
                self.color[i] = 0
            else:
                self.color[i] -= 5
        if self.color[0] <= 0:
            panjung.remove(self)
            del self


panjung = [Columb(0), Columb(1), Columb(2), Columb(3)]
blocks = [
    [Block(0), Block(0)],
    [Block(1), Block(1)],
    [Block(2), Block(2)],
    [Block(3), Block(3)],
    [Block(4), Block(4)],
    [Block(5), Block(5)],
    [Block(6), Block(6)],
    [Block(7), Block(7)],
]
i = 0
while running:
    clock.tick(144)
    i += 1
    # print(blocks)
    if i >= 144 / 8:
        r = random.randint(0, 7)
        blocks[r].append(Block(r))
        i = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                panjung.append(Columb(0))
                list(map(lambda x: x.hitcheck(0), blocks[0]))
            if event.key == pygame.K_s:
                panjung.append(Columb(1))
                list(map(lambda x: x.hitcheck(1), blocks[1]))
            if event.key == pygame.K_d:
                panjung.append(Columb(2))
                list(map(lambda x: x.hitcheck(2), blocks[2]))
            if event.key == pygame.K_f:
                panjung.append(Columb(3))
                list(map(lambda x: x.hitcheck(3), blocks[3]))
            if event.key == pygame.K_j:
                panjung.append(Columb(4))
                list(map(lambda x: x.hitcheck(4), blocks[4]))
            if event.key == pygame.K_k:
                panjung.append(Columb(5))
                list(map(lambda x: x.hitcheck(5), blocks[5]))
            if event.key == pygame.K_l:
                panjung.append(Columb(6))
                list(map(lambda x: x.hitcheck(6), blocks[6]))
            if event.key == pygame.K_SEMICOLON:
                panjung.append(Columb(7))
                list(map(lambda x: x.hitcheck(7), blocks[7]))

    screen.fill((0, 0, 0))

    list(map(lambda x: pygame.draw.rect(screen, x.color, x.rect), panjung))
    list(map(lambda x: x.update(), panjung))

    for blk in blocks:
        list(map(lambda x: pygame.draw.rect(screen, x.color, x.rect), blk))
        list(map(lambda x: x.update(), blk))
    pygame.draw.rect(
        screen, (0, 255, 0), pygame.Rect(0, 600 - 10, 800, 10)
    )  # 700 - 710

    pygame.display.flip()
