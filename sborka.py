import pygame
import sys

pygame.init()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Шаурмичная Яндексоидов")
background_image = pygame.image.load('k.jpg')
# Устанавливаем размеры окна

sprite_image = pygame.image.load('та.png')
sprite_rect = sprite_image.get_rect(centerx=280, centery=700)  # 1спрайт

q = pygame.image.load('пом.webp')
qr = q.get_rect(centerx=170, centery=150)  # 2 спрайт
s = pygame.image.load('пом.webp')
sr = s.get_rect(centerx=140, centery=100)  # 3спрайт
w = pygame.image.load('пом.webp')
wr = s.get_rect(centerx=120, centery=150)  # 4 спрайт

e = pygame.image.load('глаз.webp')
er = e.get_rect(centerx=125, centery=145)  # 5 спрайт

r = pygame.image.load('мяс.webp')
rr = r.get_rect(centerx=405, centery=145)  # 6 спрайт

dragging = False
qd = False
d = False
wd = False
ed = False
rd = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if sprite_rect.collidepoint(event.pos):
                dragging = True
                d = False
                qd = False
                ed = False
                wd = False
                rd = False
                offset_x = sprite_rect.x - event.pos[0]
                offset_y = sprite_rect.y - event.pos[1]

            if qr.collidepoint(event.pos):
                qd = True
                dragging = False
                d = False
                ed = False
                rd = False
                wd = False
                ofxq = qr.x - event.pos[0]
                ofyq = qr.y - event.pos[1]

            if sr.collidepoint(event.pos):
                d = True
                dragging = False
                qd = False
                ed = False
                rd = False
                wd = False
                ofx = sr.x - event.pos[0]
                ofy = sr.y - event.pos[1]

            if wr.collidepoint(event.pos):
                wd = True
                d = False
                rd = False
                ed = False
                dragging = False
                qd = False
                ofxw = wr.x - event.pos[0]
                ofyw = wr.y - event.pos[1]

            if er.collidepoint(event.pos):
                ed = True
                d = False
                rd = False
                wd = False
                dragging = False
                qd = False
                ofxe = er.x - event.pos[0]
                ofye = er.y - event.pos[1]

            if rr.collidepoint(event.pos):
                ed = False
                d = False
                rd = True
                wd = False
                dragging = False
                qd = False
                ofxr = rr.x - event.pos[0]
                ofyr = rr.y - event.pos[1]
        # перетаскивание
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            d = False
            qd = False
            wd = False
            ed = False
            rd = False
        # Заканчиваем перетаскивание
        if event.type == pygame.MOUSEMOTION and dragging:
            sprite_rect.x = event.pos[0] + offset_x
            sprite_rect.y = event.pos[1] + offset_y

        if event.type == pygame.MOUSEMOTION and d:
            sr.x = event.pos[0] + ofx
            sr.y = event.pos[1] + ofy

        if event.type == pygame.MOUSEMOTION and qd:
            qr.x = event.pos[0] + ofxq
            qr.y = event.pos[1] + ofyq

        if event.type == pygame.MOUSEMOTION and wd:
            wr.x = event.pos[0] + ofxw
            wr.y = event.pos[1] + ofyw

        if event.type == pygame.MOUSEMOTION and ed:
            er.x = event.pos[0] + ofxe
            er.y = event.pos[1] + ofye

        if event.type == pygame.MOUSEMOTION and rd:
            rr.x = event.pos[0] + ofxr
            rr.y = event.pos[1] + ofyr
    # Перемещение спрайта

    screen.fill((255, 255, 255))
    screen.blit(background_image, (0, 0))
    screen.blit(e, er)
    screen.blit(s, sr)
    screen.blit(sprite_image, sprite_rect)
    screen.blit(q, qr)
    screen.blit(w, wr)
    screen.blit(r, rr)
    pygame.display.flip()
    # Отображение спрайта на экране
