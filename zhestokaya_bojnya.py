import sys

import pygame
import os

pygame.init()
lines = ['+*--++', '.+...+', '=*+*--', '+*+**-', '+--.==', '-.==-+']
lines = [line.ljust(6) for line in lines]
with open('фишки', 'w') as file:
    file.writelines(line + '\n' for line in lines)
pygame.display.set_caption('Шаурмичная яндексоидов')
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
icon = pygame.image.load("аб.png")
pygame.display.set_icon(icon)


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
    'b': pygame.transform.scale(load_image('claire.png'), (60, 60)),
    'violet': pygame.transform.scale(load_image('violet.png'), (60, 60)),
    'v': pygame.transform.scale(load_image('purple.png'), (60, 60)),
    'jaune': pygame.transform.scale(load_image('jaune.png'), (60, 60)),
    'j': pygame.transform.scale(load_image('yellow.png'), (60, 60)),
    'vert': pygame.transform.scale(load_image('vert.png'), (60, 60)),
    'z': pygame.transform.scale(load_image('green.png'), (60, 60)),
    'rouge': pygame.transform.scale(load_image('rouge.png'), (60, 60)),
    'r': pygame.transform.scale(load_image('rose.png'), (60, 60))}

tile_width = tile_height = 80



def text():
    hod = 25
    bleu = 0
    violet = 0
    jaune = 0
    vert = 0
    rouge = 0
    f = pygame.font.Font('gaijin-shodo.regular.otf', 60)
    text1 = f.render(str(hod), True, (230, 150, 30))
    screen.blit(text1, (707, 43))
    fishki = pygame.font.Font('gaijin-shodo.regular.otf', 25)
    b = fishki.render(f"{str(bleu)}/15", True, (255, 50, 15))
    v = fishki.render(f"{str(violet)}/15", True, (255, 50, 15))
    j = fishki.render(f"{str(jaune)}/15", True, (255, 50, 15))
    z = fishki.render(f"{str(vert)}/15", True, (255, 50, 15))
    r = fishki.render(f"{str(rouge)}/15", True, (255, 50, 15))
    screen.blit(b, (218, 90))
    screen.blit(v, (298, 90))
    screen.blit(j, (298 + 80, 90))
    screen.blit(z, (298 + 160, 90))
    screen.blit(r, (298 + 240, 90))


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
        self.left = 160
        self.top = 210
        self.cell_size = 80
        self.color = pygame.Color(255, 110, 60)
        self.cell_x = self.cell_y = None

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                coords = (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, self.color, coords, 1)


def load_level(filename):
    with open('фишки', 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    # print(list(level_map))
    return list(level_map)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 170, tile_height * pos_y + 220)


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
            elif level[y][x] == 'b':
                Tile('b', x, y)
            elif level[y][x] == 'v':
                Tile('v', x, y)
            elif level[y][x] == 'j':
                Tile('j', x, y)
            elif level[y][x] == 'z':
                Tile('z', x, y)
            elif level[y][x] == 'r':
                Tile('r', x, y)
    return new_player, x, y


def generate_couleurs(level):
    blue = []
    claire = []
    violet = []
    purple = []
    jaune = []
    yellow = []
    vert = []
    green = []
    rouge = []
    rose = []
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
            elif level[y][x] == 'b':
                Tile('b', x, y)
                claire.append((x, y))
            elif level[y][x] == 'v':
                Tile('v', x, y)
                purple.append((x, y))
            elif level[y][x] == 'j':
                Tile('j', x, y)
                yellow.append((x, y))
            elif level[y][x] == 'z':
                Tile('z', x, y)
                green.append((x, y))
            elif level[y][x] == 'r':
                Tile('r', x, y)
                rose.append((x, y))
    tous = [blue] + [violet] + [jaune] + [vert] + [rouge] + [claire] + [purple] + [yellow] + [green] + [rose]
    return tous


class Game:
    def __init__(self, tous):
        self.width = width
        self.height = height
        self.left = 160
        self.top = 210
        self.cell_x = self.cell_y = None
        self.cell_size = 80
        self.fishki = ' '
        self.tous = tous
        self.coords = []
        (self.bleu, self.violet, self.jaune, self.vert, self.rouge, self.claire, self.purple, self.yellow, self.green,
         self.rose) = self.tous

    def get_position(self, pos):
        self.cell_x = (pos[0] - self.left) // self.cell_size
        self.cell_y = (pos[1] - self.top) // self.cell_size
        if 0 <= self.cell_x < self.width and 0 <= self.cell_y < self.height:
            self.place()
        else:
            self.cell_x = self.cell_y = None

    def place(self):
        if self.cell_x is None or self.cell_y is None:
            return
        self.fishki = ''
        for b in self.bleu:
            if (self.cell_x, self.cell_y) == b:
                self.fishki += "*"
                self.coords.append((self.cell_x, self.cell_y))
        for vi in self.violet:
            if (self.cell_x, self.cell_y) == vi:
                self.fishki += "."
                self.coords.append((self.cell_x, self.cell_y))
        for j in self.jaune:
            if (self.cell_x, self.cell_y) == j:
                self.fishki += "+"
                self.coords.append((self.cell_x, self.cell_y))
        for ve in self.vert:
            if (self.cell_x, self.cell_y) == ve:
                self.fishki += "-"
                self.coords.append((self.cell_x, self.cell_y))
        for r in self.rouge:
            if (self.cell_x, self.cell_y) == r:
                self.fishki += "="
                self.coords.append((self.cell_x, self.cell_y))
        for r in self.claire:
            if (self.cell_x, self.cell_y) == r:
                self.fishki += "b"
                self.coords.append((self.cell_x, self.cell_y))
        for r in self.purple:
            if (self.cell_x, self.cell_y) == r:
                self.fishki += "v"
                self.coords.append((self.cell_x, self.cell_y))
        for r in self.yellow:
            if (self.cell_x, self.cell_y) == r:
                self.fishki += "j"
                self.coords.append((self.cell_x, self.cell_y))
        for r in self.green:
            if (self.cell_x, self.cell_y) == r:
                self.fishki += "z"
                self.coords.append((self.cell_x, self.cell_y))
        for r in self.rose:
            if (self.cell_x, self.cell_y) == r:
                self.fishki += "r"
                self.coords.append((self.cell_x, self.cell_y))
        one = self.coords[0]
        l = []
        for cord in self.coords:
            if ((cord[0] == one[0] + 1 and cord[1] == one[1]) or (cord[1] == one[1] + 1 and cord[0] == one[0])
                    or (cord == one) or (cord[0] + 1 == one[0] and cord[1] == one[1]) or (cord[1] + 1 == one[1]
                                                                                          and cord[0] == one[0])):
                l.append("Yes")
            else:
                l = []
            one = cord
        if len(l) != 0:
            for f in self.fishki:
                if f != self.fishki[0]:
                    self.fishki = ' '
                    self.coords = []

            lines = load_level('фишки')

            if 0 <= self.cell_y < len(lines):
                current_line = list(lines[self.cell_y])

                if 0 <= self.cell_x < len(current_line):
                    znak = current_line[self.cell_x]
                    if znak == '*':
                        current_line[self.cell_x] = 'b'
                    elif znak == '.':
                        current_line[self.cell_x] = 'v'
                    elif znak == '+':
                        current_line[self.cell_x] = 'j'
                    elif znak == '-':
                        current_line[self.cell_x] = 'z'
                    elif znak == '=':
                        current_line[self.cell_x] = 'r'
                    elif znak == 'b':
                        current_line[self.cell_x] = '*'
                    elif znak == 'v':
                        current_line[self.cell_x] = '.'
                    elif znak == 'j':
                        current_line[self.cell_x] = '+'
                    elif znak == 'z':
                        current_line[self.cell_x] = '-'
                    elif znak == 'r':
                        current_line[self.cell_x] = '='

                    lines[self.cell_y] = ''.join(current_line)

                    lines = [line.ljust(6) for line in lines]

                    with open('фишки', 'w') as fp:
                        fp.writelines(line + '\n' for line in lines)

    def echages(self):
        ...


def main():
    bleu = Bleu(all_sprites)
    violet = Violet(all_sprites)
    jaune = Jaune(all_sprites)
    vert = Vert(all_sprites)
    rouge = Rouge(all_sprites)
    level = load_level('map.txt')
    tous = generate_couleurs(level)

    fps = 60
    clock = pygame.time.Clock()
    board = Board(6, 6)
    game = Game(tous)
    running = True
    background = pygame.image.load('фон.jpg').convert()
    gameDisplay = pygame.display.set_mode(size)
    background = pygame.transform.smoothscale(background, gameDisplay.get_size())
    pygame.mixer.music.load("Небожители.mp3")
    pygame.mixer.music.play(-1)
    while running:
        gameDisplay.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    game.get_position(event.pos)
                    level = load_level('фишки')
                    tiles_group.empty()
                    generate_level(level)
                else:
                    game.echages()
        text()
        all_sprites.draw(screen)
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == "__main__":
    sys.exit(main())
