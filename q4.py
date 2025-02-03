import pygame
import sys

icon = pygame.image.load("н.jpg")
pygame.display.set_icon(icon)  # Установка иконки окна

pygame.init()
pygame.display.set_caption("Шаурмичная Яндексоидов")
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('ФЫРФЫР.webp')
pygame.mixer.init()
pygame.mixer.music.load("qqq.mp3")
pygame.mixer.music.play()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background_image, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()
