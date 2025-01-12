import os
import sys
import pygame

pygame.init()
pygame.display.set_caption("распили меня болгаркой...")
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('jj (1).png')
pygame.mixer.init()
pygame.mixer.music.load("qqq.mp3")
pygame.mixer.music.play()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class MySprite(pygame.sprite.Sprite):
    image = load_image("se.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = MySprite.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.start = False

    def update(self, *args):
        if args and args[0] is not None and args[0].type == pygame.KEYDOWN and self.start:
            if args[0].key == pygame.K_DOWN:
                self.rect.top += 50
            elif args[0].key == pygame.K_UP:
                self.rect.top -= 50
            elif args[0].key == pygame.K_LEFT:
                self.rect.left -= 50
            elif args[0].key == pygame.K_RIGHT:
                self.rect.left += 50
            self.start = False


def main():
    all_sprites = pygame.sprite.Group()
    hero = MySprite(all_sprites)

    running = True
    fps = 60
    clock = pygame.time.Clock()
    event_key = None
    while running:
        screen.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                event_key = event
                hero.start = True
        all_sprites.draw(screen)
        all_sprites.update(event_key)

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())
