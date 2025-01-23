import pygame
import subprocess
import sys
from moviepy.editor import VideoFileClip

pygame.init()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Шаурмичная Яндексоидов")
background_image = pygame.image.load('k.jpg')
pygame.mixer.init()
pygame.mixer.music.load("2ч.mp3")
pygame.mixer.music.play()
# Устанавливаем размеры окна и АТМОСФЕРНЫЙ МУЗОН

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
rr = r.get_rect(centerx=380, centery=145)  # 6 спрайт
t = pygame.image.load('мяс.webp')
tr = r.get_rect(centerx=420, centery=110)  # 7 спрайт
a = pygame.image.load('мяс.webp')
ar = r.get_rect(centerx=450, centery=170)  # 8 спрайт
f = pygame.image.load('колбаса.webp')
fr = s.get_rect(centerx=640, centery=100)  # 9 спрайт
g = pygame.image.load('колбаса.webp')
gr = s.get_rect(centerx=670, centery=150)  # 10 спрайт
h = pygame.image.load('чили.webp')
hr = s.get_rect(centerx=670, centery=700)  # 11 спрайт

j = pygame.image.load('огурец.webp')
jr = s.get_rect(centerx=110, centery=660)  # 12 спрайт

dragging, d, qd, wd, td, gd, fd, hd, ad, ed, rd, jd = False, False, False, False, False, False, \
    False, False, False, \
    False, False, False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if sprite_rect.collidepoint(event.pos):
                dragging = True
                d, qd, wd, td, gd, fd, hd, ad, ed, rd, jd = False, False, False, False, False, False, \
                    False, False, False, \
                    False, False
                offset_x = sprite_rect.x - event.pos[0]
                offset_y = sprite_rect.y - event.pos[1]

            if qr.collidepoint(event.pos):
                qd = True
                dragging, d, wd, td, gd, fd, hd, ad, ed, rd, jd = False, False, False, False, False, \
                    False, False, False, False, \
                    False, False
                ofxq = qr.x - event.pos[0]
                ofyq = qr.y - event.pos[1]

            if sr.collidepoint(event.pos):
                d = True
                dragging, qd, wd, td, gd, fd, hd, ad, ed, rd, jd = False, False, False, False, False, \
                    False, False, False, False, \
                    False, False
                ofx = sr.x - event.pos[0]
                ofy = sr.y - event.pos[1]

            if tr.collidepoint(event.pos):
                dragging, d, qd, wd, gd, fd, hd, ad, ed, rd, jd = False, False, False, False, False, \
                    False, False, False, False, \
                    False, False
                td = True

                ofxt = tr.x - event.pos[0]
                ofyt = tr.y - event.pos[1]

            if ar.collidepoint(event.pos):
                dragging, d, qd, wd, td, gd, fd, hd, ed, rd, jd = False, False, False, False, False, \
                    False, False, False, False, \
                    False, False
                ad = True

                ofxa = ar.x - event.pos[0]
                ofya = ar.y - event.pos[1]

            if wr.collidepoint(event.pos):
                wd = True
                dragging, d, qd, td, gd, fd, hd, ad, ed, rd, jd = False, False, False, False, False, \
                    False, False, False, False, \
                    False, False
                ofxw = wr.x - event.pos[0]
                ofyw = wr.y - event.pos[1]

            if er.collidepoint(event.pos):
                ed = True
                dragging, d, qd, wd, td, gd, fd, hd, ad, rd, jd = False, False, False, False, False, False, \
                    False, False, False, \
                    False, False
                ofxe = er.x - event.pos[0]
                ofye = er.y - event.pos[1]

            if rr.collidepoint(event.pos):
                dragging, d, qd, wd, td, gd, fd, hd, jd, ad, ed = False, False, False, False, False, False, \
                    False, False, False, \
                    False, False
                rd = True

                ofxr = rr.x - event.pos[0]
                ofyr = rr.y - event.pos[1]

            if fr.collidepoint(event.pos):
                dragging, d, qd, wd, td, gd, hd, ad, jd, ed, rd = False, False, False, False, False, False, False, \
                    False, False, \
                    False, False
                fd = True

                ofxf = fr.x - event.pos[0]
                ofyf = fr.y - event.pos[1]

            if gr.collidepoint(event.pos):
                dragging, d, qd, wd, td, fd, hd, ad, ed, rd, jd = False, False, False, False, False, False, False, \
                    False, False, \
                    False, False
                gd = True

                ofxg = gr.x - event.pos[0]
                ofyg = gr.y - event.pos[1]

            if hr.collidepoint(event.pos):
                dragging, d, qd, wd, td, gd, fd, ad, jd, ed, rd = False, False, False, False, False, False, False, \
                    False, False, \
                    False, False
                hd = True

                ofxh = hr.x - event.pos[0]
                ofyh = hr.y - event.pos[1]

            if jr.collidepoint(event.pos):
                dragging, d, qd, wd, td, gd, fd, ad, hd, ed, rd = False, False, False, False, False, False, False, \
                    False, False, \
                    False, False
                jd = True

                ofxj = jr.x - event.pos[0]
                ofyj = jr.y - event.pos[1]
        # перетаскивание
        if event.type == pygame.MOUSEBUTTONUP:
            dragging, d, qd, wd, td, gd, jd, fd, hd, ad, ed, rd = False, False, False, False, \
                False, False, False, False, False, \
                False, False, False

        # Заканчиваем перетаскивание
        if event.type == pygame.MOUSEMOTION and dragging:
            sprite_rect.x = event.pos[0] + offset_x
            sprite_rect.y = event.pos[1] + offset_y

        if event.type == pygame.MOUSEMOTION and d:
            sr.x = event.pos[0] + ofx
            sr.y = event.pos[1] + ofy

        if event.type == pygame.MOUSEMOTION and td:
            tr.x = event.pos[0] + ofxt
            tr.y = event.pos[1] + ofyt

        if event.type == pygame.MOUSEMOTION and ad:
            ar.x = event.pos[0] + ofxa
            ar.y = event.pos[1] + ofya

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

        if event.type == pygame.MOUSEMOTION and fd:
            fr.x = event.pos[0] + ofxf
            fr.y = event.pos[1] + ofyf

        if event.type == pygame.MOUSEMOTION and gd:
            gr.x = event.pos[0] + ofxg
            gr.y = event.pos[1] + ofyg

        if event.type == pygame.MOUSEMOTION and hd:
            hr.x = event.pos[0] + ofxh
            hr.y = event.pos[1] + ofyh

        if event.type == pygame.MOUSEMOTION and jd:
            jr.x = event.pos[0] + ofxj
            jr.y = event.pos[1] + ofyj
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                video_clip = VideoFileClip("заставка.mp4")
                video_clip.preview()
                subprocess.Popen('main.py')

    # Перемещение спрайта
    myfont = pygame.font.SysFont("monospace", 30)
    label = myfont.render("Соберите ШАУРМУ", 1, (60, 170, 60))
    button_font = pygame.font.Font(None, 36)
    button_text = button_font.render('ГОТОВО', True, (0, 250, 30))
    button_rect = button_text.get_rect(center=(400, 750))
    # ТЕКСТ
    screen.fill((255, 255, 255))
    screen.blit(background_image, (0, 0))
    screen.blit(e, er)
    screen.blit(s, sr)
    screen.blit(q, qr)
    screen.blit(w, wr)
    screen.blit(r, rr)
    screen.blit(t, tr)
    screen.blit(a, ar)
    screen.blit(h, hr)
    screen.blit(f, fr)
    screen.blit(g, gr)
    screen.blit(label, (265, 650))
    screen.blit(j, jr)
    screen.blit(button_text, button_rect)
    screen.blit(sprite_image, sprite_rect)
    pygame.display.flip()
    # Отображение спрайта на экране
