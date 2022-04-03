#https://github.com/garlis/Tarkvaraarenduse-projekt-Garlis-Hendla

import pygame #Impordib PyGamei.
import sys #Impordib sys
pygame.init() #Käivitab PyGamei.

Roheline = [153, 255, 153] #Defineerib rohelise värvi.
Punane = [255, 0, 0] #Defineerib punase värvi.
Aken=pygame.display.set_mode([640,480]) #Loob õige suurusega akna.
pygame.display.set_caption("Harjutamine") #Akna nimi.
Aken.fill(Roheline) #Teeb akna tausta roheliseks.


def ruudud(ruudusuurus, värv, veerud, read): #Defineerib funktsiooni ruudud ja tema argumendid.
    veerud = (veerud * 20) #Muutuja veerud väärtus on veerud korda 20.
    read = (read * 20) #Muutuja read väärtus on read korda 20.
    for x in range(0, veerud, ruudusuurus): #Alustab for tsüklit x vahemikus 0, veerud, ruudusuurus.
        for y in range(0, read, ruudusuurus): #For tsükli kasutamine, y  vahemikus 0, read, suurus.
            ruut = pygame.Rect(x, y, ruudusuurus, ruudusuurus) #Muutuja ruut saab väärtuseks kujundi alguskoordinaadid, laius, kõrgus.
            pygame.draw.rect(Aken, värv, ruut, 1) #Kujundi ehk ruudu joonistamine.

ruudud(20, Punane, 32, 24) #Eelnevalt defineeritud funktsiooni kasutamine.
pygame.display.flip() #Akna värskendamine.

mängläbi = False #Muutuja mille väärtus on vale.
while not mängläbi: #While kasutamine kuni väärtus ei ole vale.

    #Mängu ristist sulgemine.
    for i in pygame.event.get(): #Tsükkli kasutamine i saab mooduli parameetrid.
       if i.type == pygame.QUIT: #Kui võrdne.
           sys.exit() #Sys kasutamine mängu sulgemiseks.

pygame.quit() #Sulgeb mängu.