import os
import pygame
import subprocess
import sys
from moviepy.editor import VideoFileClip

icon = pygame.image.load("н.jpg")
pygame.display.set_icon(icon)  # Установка иконки окна

pygame.init()
pygame.display.set_caption("Шаурмичная Яндексоидов")
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('jj (1).png')
pygame.mixer.init()
pygame.mixer.music.load("qqq.mp3")
pygame.mixer.music.play()

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

qwq = ['Шаверма закрыта,', 'Вы хотите есть...',
       'остались ингредиенты', 'на последнюю шаурму!!!',
       'Приготовьте ее.']
button_font = pygame.font.Font(None, 32)
button_text = button_font.render('', True, (250, 0, 30))
button_rect = button_text.get_rect(center=(600, 700))


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
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
    image = load_image("semm.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = MySprite.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.start = False

    def update(self, *args):
        if args and args[0] is not None and args[0].type == pygame.KEYDOWN and self.start:
            if args[0].key == pygame.K_s:
                self.rect.top += 50
            elif args[0].key == pygame.K_w:
                self.rect.top -= 50
            elif args[0].key == pygame.K_a:
                self.rect.left -= 50
            elif args[0].key == pygame.K_d:
                self.rect.left += 50
            self.start = False

        if pygame.sprite.spritecollideany(self, horizontal_borders):
            if args and args[0] is not None and args[0].type == pygame.KEYDOWN and self.start:
                if args[0].key == pygame.K_a:
                    self.rect.left += 50
                elif args[0].key == pygame.K_d:
                    self.rect.left -= 50
        if pygame.sprite.spritecollideany(self, vertical_borders):
            if args and args[0] is not None and args[0].type == pygame.KEYDOWN and self.start:
                if args[0].key == pygame.K_s:
                    self.rect.top -= 50
                elif args[0].key == pygame.K_w:
                    self.rect.top += 50


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


def main():
    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)

    st = pygame.image.load("СТ.webp")
    sr = st.get_rect(centerx=400, centery=764)  # 3спрайт
    all_sprites = pygame.sprite.Group()
    hero = MySprite(all_sprites)

    running = True
    fps = 60
    clock = pygame.time.Clock()
    event_key = None
    qdf = pygame.font.Font(None, 36)
    qt = qdf.render('СЮДА', True, (250, 0, 30))
    qr = qt.get_rect(center=(585, 710))

    while running:
        screen.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                event_key = event
                hero.start = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if qr.collidepoint(event.pos):
                    running = False

        for i in range(len(qwq)):
            qwqt = button_font.render(qwq[i], True, (250, 0, 30))
            qwqr = button_text.get_rect(center=(520, 10 + i * 25))
            screen.blit(qwqt, qwqr)

        all_sprites.draw(screen)
        all_sprites.update(event_key)
        clock.tick(fps)
        screen.blit(qt, qr)
        screen.blit(st, sr)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    sys.exit(main())
