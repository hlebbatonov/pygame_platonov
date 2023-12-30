import pygame
import os

pygame.init()
size = width, height = 800, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Math ninja')


def load_image(name, colorkey=None):
    image = pygame.image.load(os.path.join('data', name))
    image.convert_alpha()
    return image



class Animatedhero(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

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
if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("walk1.png")
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    fps = 60
    running = True
    paint = False
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while running:
        for event in pygame.event.get():
            screen.fill((255, 255, 255))
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and sprite.rect.x > 0:
                    sprite.rect.x -= 10
                if event.key == pygame.K_RIGHT:
                    sprite.rect.x += 10
                if event.key == pygame.K_UP and sprite.rect.y > 0:
                    sprite.rect.y -= 10
                if event.key == pygame.K_DOWN:
                    sprite.rect.y += 10
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
