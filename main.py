import pygame
import os
import pygame.freetype
import sqlite3
import random

pygame.init()
size = width, height = 800, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Math ninja')
fps = 6


def load_image(name, colorkey=None):
    image = pygame.image.load(os.path.join('data', name))
    image.convert_alpha()
    return image


def load_db(name):
    return os.path.join('data', name)


def answers():
    global task, corr_id, ans
    task = cur.execute(
        f'''SELECT number1,
       operator,
       number2,
       answer
  FROM tasks
 WHERE id = {corr_id}''').fetchone()
    ans = task[3]
    task = str(task[0]) + task[1] + str(task[2]) + '= ?'
    labels = []
    labels.append(str(ans))
    labels.append(str(ans + random.randint(-3, 3)))
    random.shuffle(labels)
    corr_id += 1
    return labels


class Animatedhero(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        if pygame.sprite.collide_mask(self, monster1):
            print(12)

con = sqlite3.connect(load_db('tasks.db'))
cur = con.cursor()

font = pygame.freetype.Font("C:/Windows/Fonts/arial.ttf", 32)

all_sprites = pygame.sprite.Group()

hero = pygame.sprite.Sprite()
hero = Animatedhero(load_image("hero_walk.png"), 5, 1, 30, 20)

monster1 = pygame.sprite.Sprite()
monster1 = Animatedhero(load_image("monster1_walk.png"), 6, 1, 30, 20)
monster1.rect.x = width
monster1.rect.y = 30

monster2 = pygame.sprite.Sprite()
monster2 = Animatedhero(load_image("monster2_walk.png"), 6, 1, 30, 20)
monster2.rect.x = width
monster2.rect.y = 200

star = pygame.sprite.Sprite()
star.image = load_image('star.png')
star.rect = star.image.get_rect()
star.rect.x = width - 35
star.rect.y = 0
all_sprites.add(star)

heart = pygame.sprite.Sprite()
heart.image = load_image('heart.png')
heart.rect = heart.image.get_rect()
heart.rect.x = width // 2
heart.rect.y = 3
all_sprites.add(heart)
life = 3

if __name__ == '__main__':

    coins = 0
    running = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    corr_id = 1
    labels = answers()
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and hero.rect.x > 0:
                    hero.rect.x -= 30
                if event.key == pygame.K_RIGHT and hero.rect.x < width // 3:
                    hero.rect.x += 30
                if event.key == pygame.K_UP and hero.rect.y > 30:
                    hero.rect.y -= 30
                if event.key == pygame.K_DOWN and hero.rect.y < height:
                    hero.rect.y += 30

        monster1.rect.x -= 7
        monster2.rect.x -= 7
        font.render_to(screen, (monster1.rect.x + 90, monster1.rect.y), labels[0], (0, 0, 0))
        font.render_to(screen, (monster2.rect.x + 90, monster2.rect.y), labels[1], (0, 0, 0))
        font.render_to(screen, (width - 60, 5), str(coins), (0, 0, 0))
        font.render_to(screen, (5, 5), task)

        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
