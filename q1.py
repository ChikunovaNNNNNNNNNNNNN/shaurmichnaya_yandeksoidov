import pygame
import subprocess
import sys
from moviepy.editor import VideoFileClip
icon = pygame.image.load("н.jpg")
pygame.display.set_icon(icon)
# Установка иконки окна
pygame.init()
pygame.display.set_caption("Шаурмичная Яндексоидов")
size = WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('jj (1).png')
# задний фон
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

video_clip = VideoFileClip("заставка.mp4")
# заставка
video_clip.preview()
pygame.mixer.init()
pygame.mixer.music.load("пр.mp3")
pygame.mixer.music.play()
# добавляем песню
button_font = pygame.font.Font(None, 36)
button_text = button_font.render('Играть', True, (250, 0, 30))
button_rect = button_text.get_rect(center=(380, 700))
qwq = ['Предупреждение!', 'Встречаются элементы хоррора, но будет не страшно...', '',
       'Правила:', 'На этапе передвижения по шаурмичной,', 'персонаж управляется кнопками WASD,',
       'а на этапе готовки, объекты перетаскиваются мышью.', '',
       'На этапе игры с фишками, вам нужно собрать n количество', 'фишек за определенное количество ходов.',
       'Собираются минимум по 3 фишки, находящиеся рядом.']
# добавляем текст с правилами
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                video_c = VideoFileClip("ананас.mp4")
                video_c.preview()
                # запускаем видео с сюжетом
                subprocess.Popen('main.py')

    screen.fill((0, 0, 0))
    screen.blit(button_text, button_rect)
    for i in range(len(qwq)):
        qw = qwq[i]
        qw = pygame.font.Font(None, 36)
        qwqt = button_font.render(qwq[i], True, (250, 0, 30))
        qwqr = button_text.get_rect(center=(50, 50 + i * 40))
        screen.blit(qwqt, qwqr)
        # вывод текста
    pygame.display.flip()

pygame.quit()
sys.exit()
