import pygame

SIZE = WIDTH, HEIGHT = 600, 400  # the width and height of our screen
BACKGROUND_COLOR = pygame.image.load("j.jpg")  # The background colod of our window

FPS = 10  # Frames per second
pygame.mixer.init()
pygame.mixer.music.load("qqq.mp3")
pygame.mixer.music.play()


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()

        self.images = []
        self.images.append(pygame.image.load('sticker.png'))
        self.images.append(pygame.image.load('sticker0.png'))

        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        my_group.update()
        screen.blit(BACKGROUND_COLOR, (0, 0))
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()
