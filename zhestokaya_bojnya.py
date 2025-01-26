import sys
import pygame
import os
import random


pygame.init()
pygame.display.set_caption('Шаурмичная яндексоидов')
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()


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

tile_images = {
        'bleu': pygame.transform.scale(load_image('blue.png'), (60, 60)),
        'violet': pygame.transform.scale(load_image('violet.png'), (60, 60)),
        'jaune': pygame.transform.scale(load_image('jaune.png'), (60, 60)),
        'vert': pygame.transform.scale(load_image('vert.png'), (60, 60)),
        'rouge': pygame.transform.scale(load_image('rouge.png'), (60, 60))}

tile_width = tile_height = 80

class Hod:
    ...


class Bleu(pygame.sprite.Sprite):
    image1 = load_image("blue.png")
    image = pygame.transform.scale(image1, (60, 60))


    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bleu.image
        self.rect = self.image.get_rect()
        self.rect.x = 210
        self.rect.y = 130


class Violet(pygame.sprite.Sprite):
    image1 = load_image("violet.png")
    image = pygame.transform.scale(image1, (60, 60))


    def __init__(self, *group):
        super().__init__(*group)
        self.image = Violet.image
        self.rect = self.image.get_rect()
        self.rect.x = 290
        self.rect.y = 130


class Jaune(pygame.sprite.Sprite):
    image1 = load_image("jaune.png")
    image = pygame.transform.scale(image1, (60, 60))


    def __init__(self, *group):
        super().__init__(*group)
        self.image = Jaune.image
        self.rect = self.image.get_rect()
        self.rect.x = 290 + 80
        self.rect.y = 130


class Vert(pygame.sprite.Sprite):
    image1 = load_image("vert.png")
    image = pygame.transform.scale(image1, (60, 60))


    def __init__(self, *group):
        super().__init__(*group)
        self.image = Vert.image
        self.rect = self.image.get_rect()
        self.rect.x = 290 + 160
        self.rect.y = 130


class Rouge(pygame.sprite.Sprite):
    image1 = load_image("rouge.png")
    image = pygame.transform.scale(image1, (60, 60))


    def __init__(self, *group):
        super().__init__(*group)
        self.image = Rouge.image
        self.rect = self.image.get_rect()
        self.rect.x = 290 + 160 + 80
        self.rect.y = 130


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.color = pygame.Color(255, 110, 60)
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
        return self.cell_x, self.cell_y

    def print_click(self):
        if self.cell_x is None:
            print("None")
        else:
            print(f"({self.cell_x}, {self.cell_y})")


def load_level(filename):
    filename = "фишки"
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return list(level_map)

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
                tile_width * pos_x + 170, tile_height * pos_y + 220)


def generate_couleurs(level):
    blue = []
    violet = []
    jaune = []
    vert = []
    rouge =[]
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '*':
                Tile('bleu', x, y)
                blue.append((x, y))
            elif level[y][x] == '.':
                Tile('violet', x, y)
                violet.append((x, y))
            elif level[y][x] == '+':
                Tile('jaune', x, y)
                jaune.append((x, y))
            elif level[y][x] == '-':
                Tile('vert', x, y)
                vert.append((x, y))
            elif level[y][x] == '=':
                Tile('rouge', x, y)
                rouge.append((x, y))
    return blue, violet, jaune, vert, rouge

def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '*':
                Tile('bleu', x, y)
            elif level[y][x] == '.':
                Tile('violet', x, y)
            elif level[y][x] == '+':
                Tile('jaune', x, y)
            elif level[y][x] == '-':
                Tile('vert', x, y)
            elif level[y][x] == '=':
                Tile('rouge', x, y)
    return new_player, x, y

player, level_x, level_y = generate_level(load_level('map.txt'))


class Game:
    def __init__(self, bleu, violet, jaune, vert, rouge):
        self.bleu = generate_couleurs(bleu)
        self.violet = generate_couleurs(violet)
        self.jaune = generate_couleurs(jaune)
        self.vert = generate_couleurs(vert)
        self.rouge = generate_couleurs(rouge)


    def get_position(self):
        for cords in self.bleu:
            ...

    def place(self, b, v, j, ve, r):
        print(b, v, j, ve, r, sep='\n')



def main():
    bleu = Bleu(all_sprites)
    violet = Violet(all_sprites)
    jaune = Jaune(all_sprites)
    vert = Vert(all_sprites)
    rouge = Rouge(all_sprites)
    game = Game

    fps = 60
    clock = pygame.time.Clock()
    board = Board(6, 6)
    board.set_view(160, 210, 80)
    running = True
    background = pygame.image.load('фон.jpg').convert()
    gameDisplay = pygame.display.set_mode(size)
    background = pygame.transform.smoothscale(background, gameDisplay.get_size())
    pygame.mixer.music.load("Магистр.mp3")
    pygame.mixer.music.play(-1)
    while running:
        gameDisplay.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 2:
                    board.get_click(event.pos)

        all_sprites.draw(screen)

        clock.tick(fps)
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    sys.exit(main())
