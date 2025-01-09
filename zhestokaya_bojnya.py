import sys
import pygame
import os


pygame.init()
pygame.display.set_caption('Шаурмичная яндексоидов')
size = width, height = 800, 800
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('fishki', name)
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
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    image1 = load_image("blue.png")
    image = pygame.transform.scale(image1, (60, 60))
    image2 = load_image("violet.png")
    imagea = pygame.transform.scale(image2, (60, 60))
    image3 = load_image("jaune.png")
    imageb = pygame.transform.scale(image3, (60, 60))
    image4 = load_image("vert.png")
    imagec = pygame.transform.scale(image4, (60, 60))
    image5 = load_image("rouge.png")
    imaged = pygame.transform.scale(image5, (60, 60))


    def __init__(self, *group):
        super().__init__(*group)
        self.image = MySprite.image
        self.rect = self.image.get_rect()
        self.rect.x = 210
        self.rect.y = 90
        self.imagea = MySprite.imagea
        self.rect1 = self.imagea.get_rect()
        self.rect1.x = 300
        self.rect1.y = 90



class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.color = pygame.Color(110, 110, 255)
        self.cell_x = self.cell_y = None

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                coords = (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, self.color, coords, 1)

    def get_click(self, pos):
        self.cell_x = (pos[0] - self.left) // self.cell_size
        self.cell_y = (pos[1] - self.top) // self.cell_size
        if (pos[0] < self.left or pos[1] < self.top or pos[0] > self.left + self.cell_size * self.width or pos[
            1] > self.top + self.cell_size * self.height):
            self.cell_x = self.cell_y = None
        self.print_click()

    def print_click(self):
        if self.cell_x is None:
            print("None")
        else:
            print(f"({self.cell_x}, {self.cell_y})")


def main():
    all_sprites = pygame.sprite.Group()
    hero = MySprite(all_sprites)

    fps = 60
    clock = pygame.time.Clock()
    board = Board(6, 6)
    board.set_view(160, 170, 80)
    running = True
    while running:
        screen.fill((240, 255, 240))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        all_sprites.draw(screen)

        clock.tick(fps)
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    sys.exit(main())
