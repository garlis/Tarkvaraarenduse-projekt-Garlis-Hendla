#https://github.com/garlis/Tarkvaraarenduse-projekt-Garlis-Hendla

import pygame, sys, random #Pygamei sysi ja randomi importimine.
pygame.init()  #Pygamei käivitamine.

screenX = 640  #Määrab akna laiuse.
screenY = 480  #Määrab akna kõrguse.
screen=pygame.display.set_mode([screenX,screenY]) #Akna suuruse määramine, 640x480.
pygame.display.set_caption("Ülesanne4") #Aknale nime andmine.
bg = pygame.image.load("bg_rally.jpg") #Avab taustapildi.
screen.blit(bg,[0,0]) #Määrab pildi asukoha mis hetkel on terve aken.                                         
clock = pygame.time.Clock() #Lisab pygamei kella funktsiooni.

red = pygame.image.load("f1_red.png")  #Avab punase auto pildi.
red = pygame.transform.scale(red, [50, 100]) #Muudab punase auto mõõtmeid.             
screen.blit(red,[295,370]) #Määrab punase auto asukoha.

blue = pygame.image.load("f1_blue.png") #Avab sinise auto pildi.
blue = pygame.transform.scale(blue, [50, 100])  #Muudab sinise auto mõõtmeid.

skoor = 0 #Muutuja skoor algväärtus on 0.
font = pygame.font.Font(pygame.font.match_font('Daytona'), 30) #Defineerib skoori suuruse ja fonti.
tekst = font.render("SKOOR: " + str(skoor), True, [255,255,255])  #Muutuja tekst saab väärtuse "font.render" ja ekraanile tuleb skoor.

#Asukoht ja kiirus.
posX, posY = 0, 0
speedX, speedY = 3, 3

coords = []  #Kordinaatide loomine.
for i in range(2): #Alustab for tsükklit ja määrab 2 objekti.
    posX = random.randint(180, 460) #Muutuja juhuslik koht x teljel.
    posY = random.randint(1, screenY) #Muutuja juhuslik koht y teljel.
    coords.append([posX, posY]) #Positsioonide määramine.

gameover = False  #Muutuja gameover saab väärtuse False.
while not gameover:  #Algab while tsükkel, kui ei ole gameover.
    #Mängu ristist sulgemine kasutades tsüklit.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
    
    #FPS - Frames per second.
    clock.tick(120) #Määrab ekraaniliikumise kiiruse, ehk 120 kaadrit sekundis.

    for i in range(len(coords)): #i saab koordinaadid vastavalt objektide arvule.
        screen.blit(blue, [coords[i][0], coords[i][1], 20, 20]) #blue auto liigub juhuslike kordinaatide abil.
        coords[i][1] += 1 #Muutuja väärtus on enda väärtus +1.

        if coords[i][1] > screenY: #Kui blue auto jõuab lõppu, muudetakse auto algus kohta.
            skoor += 1 #Skoorile lisandub üks punkt igakord kui blue auto jõuab lõppu.
            coords[i][1] = random.randint(-20, -15) #Valitakse uued random väärtused Y teljel.
            coords[i][0] = random.randint(135, 460) #Valitakse random väärtused X telje vahemikus, kuhu auto tekib.

    screen.blit(tekst, [525, 20])  #Aknal kuvatakse muutujale tekst omistatud väärtus kordinaatidel x=525 ja y=20.
    tekst = font.render("SKOOR: " + str(skoor), True, [255, 255, 255]) #Arvutab kokku skoori saadud on ja kuvab seda ekraanil.
    pygame.display.flip() #Ekraani värskendamine.
    screen.blit(bg, [0, 0]) #Joonistatakse taust uuesti.
    screen.blit(red, [295, 370]) #Joonistatakse red auto uuesti.
    


pygame.quit()