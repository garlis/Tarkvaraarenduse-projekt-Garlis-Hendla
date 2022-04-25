#https://github.com/garlis/Tarkvaraarenduse-projekt-Garlis-Hendla

import pygame #Pygame importimine.
import random #Random inportimine.

pygame.init() #Käivitatakse pygame moodul.

(width, height) = (640, 480) #Akna laius ja kõrgus 640x480.
screen = pygame.display.set_mode((width, height)) #Tekib aken mille laiuseks on 640px ja kõrguseks on 480px.
pygame.display.set_caption("Ringid")  #Akna pealkirjaks määratakse Ringid.
screen.fill([173, 216, 230]) #Aken värvitakse helesiniseks.

min_strenght= 0 #Värvikoodi miinimum väärtus.
max_strenght= 255 #Värvikoodi maksimaalne väärtus.

radius = 10 #Muutuja radius väärtus on 10 ehk ringi raadiuseks on algväärtusena 10px.

running = True #Kuni muutuja running väärtus on True.
while running: #While tsükkel, tingimuseks on muutuja running tõene väärtus.
    ev = pygame.event.get() #Muutuja ev sisaldab mooduli pygame.event meetodit .get().
    pygame.display.flip() #Akna värskendamine.

    #Hiirega ringide joonistamine (random värvid ja suurus suureneb.)
    for event in ev: #Iga tsüklimuutuja event väärtus muutujas ev.
        if event.type == pygame.MOUSEBUTTONUP: #Kui klikitakse vasakul hiire nupul ja lastakse se lahti.
            pos = pygame.mouse.get_pos() #Muutujasse pos salvestatakse hiire koordinaat.
            varv = (random.randint(min_strenght, max_strenght), random.randint(min_strenght, max_strenght),
            random.randint(min_strenght, max_strenght)) #Genereeritakse random värv.
            pygame.draw.circle(screen, varv, pos, radius, 1) #Joonistatakse random värviga ring, positsiooniks on hiire kursori asukoht ja radiuseks on algselt 10px.
            radius += 5 #Iga klikiga muutub ring 5px suuremaks.

        #Ristist sulgemine
        if event.type == pygame.QUIT: #Kui sündmuse tüüp on QUIT ehk ristist sulgemine.
            running = False #While tsükkel lõpetatakse ehk mäng saab läbi.