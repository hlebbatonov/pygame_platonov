import pygame
import os
import pygame.freetype
import sqlite3
import random
from tasks_generator import tasks_generator
pygame.init()
size = width, height = 700, 450
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Math ninja')
fps = 6


def load_image(name, colorkey=None):
    image = pygame.image.load(os.path.join('data', name))
    image.convert_alpha()
    return image

def answers(x):
    global task, corr_id, ans
    if x == 1:
        task = tasks_generator(1)
    else:
        task = tasks_generator(2)


    ans = task[3]
    task = str(task[0]) + task[1] + str(task[2]) + '= ?'
    labels = []
    labels.append(str(ans))
    step = random.randint(-3, 3)
    while step == 0:
        step = random.randint(-3, 3)
    step2 = step
    while step2 == step or step2 == 0:
        step2 = random.randint(-4, 3)
    labels.append(str(ans + step))
    labels.append(str(ans + step2))
    random.shuffle(labels)
    random.shuffle(labels)
    corr_id += 1
    return labels

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

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
monster2.rect.y = 180

monster3 = pygame.sprite.Sprite()
monster3 = Animatedhero(load_image("monster3_walk.png"), 6, 1, 30, 20)
monster3.rect.x = width
monster3.rect.y = 320

star = pygame.sprite.Sprite()
star.image = load_image('star.png')
star.rect = star.image.get_rect()
star.rect.x = width - 35
star.rect.y = 0
all_sprites.add(star)

heart = pygame.sprite.Sprite()
heart.image = load_image('life3.png')
heart.rect = heart.image.get_rect()
heart.rect.x = width // 2
heart.rect.y = 3
all_sprites.add(heart)

bg = Background('ground2.jpg', [0,0])
bg2 = Background('ground.jpg', [0,0])
life = 3

start_bg = Background('start_bg1.jpg', [0,0])
if __name__ == '__main__':
    clock = pygame.time.Clock()
    start_it = True
    end_anim = True
    start_anim = True
    running = True
    running2 = True
    end_it = True
    result = True
    while start_it:
        screen.fill((0, 0, 0))
        screen.blit(start_bg.image, start_bg.rect)
        myfont = pygame.font.SysFont("Britannic Bold", 40)
        nlabel = myfont.render('START', 1, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_it = False
            if event.type == pygame.QUIT:
                start_it = False
                start_anim = False
                end_anim = False
                end_it = False
                running = False
                running2 = False
                result = False
        screen.blit(nlabel, (10, height - 90))
        pygame.display.flip()

    i = 1
    while start_anim:
        if i >= 8:
            start_anim = False
        start_bg = Background(f'start_bg{i}.jpg', [0,0])
        screen.fill((0, 0, 0))
        screen.blit(start_bg.image, start_bg.rect)
        i += 1

        clock.tick(fps)
        pygame.display.flip()
    coins = 0
    pygame.mouse.set_visible(False)
    corr_id = 1
    labels = answers(1)
    while running:
        if life == 0 or coins == 10:
            running = False
            break
        screen.fill([255, 255, 255])
        screen.blit(bg.image, bg.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                start_it = False
                start_anim = False
                end_anim = False
                end_it = False
                running2 = False
                result = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and hero.rect.x > 0:
                    hero.rect.x -= 30
                if event.key == pygame.K_RIGHT and hero.rect.x < width // 3:
                    hero.rect.x += 30
                if event.key == pygame.K_UP and hero.rect.y > 30:
                    hero.rect.y -= 30
                if event.key == pygame.K_DOWN and hero.rect.y < height - 98:
                    hero.rect.y += 30
        if pygame.sprite.collide_mask(hero, monster1) or pygame.sprite.collide_mask(hero,
                                                                                    monster2) or pygame.sprite.collide_mask(
            hero, monster3):

            if pygame.sprite.collide_mask(hero, monster1):
                if int(labels[0]) == ans:
                    coins += 1
                else:
                    life -= 1
            if pygame.sprite.collide_mask(hero, monster2):
                if int(labels[1]) == ans:
                    coins += 1
                else:
                    life -= 1
            if pygame.sprite.collide_mask(hero, monster3):
                if int(labels[2]) == ans:
                    coins += 1
                else:
                    life -= 1
            monster1.rect.x = width
            monster2.rect.x = width
            monster3.rect.x = width
            corr_id += 1
            labels = answers(1)

        monster1.rect.x -= 7
        monster2.rect.x -= 7
        monster3.rect.x -= 7
        font.render_to(screen, (monster1.rect.x + 90, monster1.rect.y), labels[0], (0, 0, 0))
        font.render_to(screen, (monster2.rect.x + 90, monster2.rect.y), labels[1], (0, 0, 0))
        font.render_to(screen, (monster3.rect.x + 90, monster3.rect.y), labels[2], (0, 0, 0))
        font.render_to(screen, (width - 60, 5), str(coins), (0, 0, 0))
        font.render_to(screen, (5, 5), task)

        if life == 2:
            heart.image = load_image('life2.png')
            heart.rect = heart.image.get_rect()
            heart.rect.x = width // 2
            heart.rect.y = 3
        elif life == 1:
            heart.image = load_image('life1.png')
            heart.rect = heart.image.get_rect()
            heart.rect.x = width // 2
            heart.rect.y = 3

        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(fps)
        pygame.display.flip()
    while running2:
        if life == 0:
            running2 = False
            break
        screen.fill([255, 255, 255])
        screen.blit(bg2.image, bg2.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                start_it = False
                start_anim = False
                end_anim = False
                end_it = False
                running2 = False
                result = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and hero.rect.x > 0:
                    hero.rect.x -= 30
                if event.key == pygame.K_RIGHT and hero.rect.x < width // 3:
                    hero.rect.x += 30
                if event.key == pygame.K_UP and hero.rect.y > 30:
                    hero.rect.y -= 30
                if event.key == pygame.K_DOWN and hero.rect.y < height - 98:
                    hero.rect.y += 30
        if pygame.sprite.collide_mask(hero, monster1) or pygame.sprite.collide_mask(hero,
                                                                                    monster2) or pygame.sprite.collide_mask(
            hero, monster3):

            if pygame.sprite.collide_mask(hero, monster1):
                if int(labels[0]) == ans:
                    coins += 1
                else:
                    life -= 1
            if pygame.sprite.collide_mask(hero, monster2):
                if int(labels[1]) == ans:
                    coins += 1
                else:
                    life -= 1
            if pygame.sprite.collide_mask(hero, monster3):
                if int(labels[2]) == ans:
                    coins += 1
                else:
                    life -= 1
            monster1.rect.x = width
            monster2.rect.x = width
            monster3.rect.x = width
            corr_id += 1
            labels = answers(2)
        monster1.rect.x -= 13
        monster2.rect.x -= 13
        monster3.rect.x -= 13
        font.render_to(screen, (monster1.rect.x + 90, monster1.rect.y), labels[0], (255, 255, 255))
        font.render_to(screen, (monster2.rect.x + 90, monster2.rect.y), labels[1], (255, 255, 255))
        font.render_to(screen, (monster3.rect.x + 90, monster3.rect.y), labels[2], (255, 255, 255))
        font.render_to(screen, (width - 70, 5), str(coins), (255, 255, 255))
        font.render_to(screen, (5, 5), task, (255, 255, 255))

        if life == 2:
            heart.image = load_image('life2.png')
            heart.rect = heart.image.get_rect()
            heart.rect.x = width // 2
            heart.rect.y = 3
        elif life == 1:
            heart.image = load_image('life1.png')
            heart.rect = heart.image.get_rect()
            heart.rect.x = width // 2
            heart.rect.y = 3

        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(fps)
        pygame.display.flip()
    i = 8
    while end_anim:
        if i <= 1:
            end_anim = False
            break
        start_bg = Background(f'start_bg{i}.jpg', [0,0])
        screen.fill((0, 0, 0))
        screen.blit(start_bg.image, start_bg.rect)
        i -= 1

        clock.tick(fps)
        pygame.display.flip()
    while end_it:
        screen.fill((0, 0, 0))
        start_bg = Background(f'end_bg.jpg', [0,0])
        screen.blit(start_bg.image, start_bg.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_it = False
                result = False
        myfont = pygame.font.SysFont("Britannic Bold", 60)
        nlabel = myfont.render(str(coins), 1, (255, 255, 255))
        screen.blit(nlabel, (30, height - 140))
        pygame.display.flip()

    pygame.quit()
