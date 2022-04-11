#https://github.com/garlis/Tarkvaraarenduse-projekt-Garlis-Hendla

import pygame #Pygamei importimine.

pygame.init() #Pygamei käivitamine.

screenX = 640 #Akna laius 640.
screenY = 480 #Akna kõrgus 480px.
screen=pygame.display.set_mode([screenX,screenY]) #640x480 suuruse akna loomine.
pygame.display.set_caption("PingPong") #Annab aknale nime PingPong.
clock = pygame.time.Clock() #Muutuja clock saab väärtuseks Pygamei clock funktsiooni.

#Palli algpositsioon ja kiirus.
posX, posY = 0, 0 
speedX, speedY = 3, 4 

#Aluse positsioon ja kiirus.
posX2, posY2 = 0, (screenY/1.5) 
speedX2 = 2 

ball = pygame.Rect(posX, posY, 20, 20) #Luuakse rect objekt mille sisse mahutatakse palli pilt. 
ballPicture = pygame.image.load("ball.png") #Muutuja ballPicture saab väärtuseks ball.png faili.
ballPicture = pygame.transform.scale(ballPicture, [ball.width, ball.height]) #ball.png pildi suuruseks määratakse 20x20 ja see saab muutuja "ball" uueks väärtuseks.

pad = pygame.Rect(posX2, posY2, 120, 20) #Luuakse rect objekt mille sisse mahutatakse aluse pilt.
padPicture = pygame.image.load("pad.png") #Muutuja padPicture saab väärtuseks pad.png faili.
padPicture = pygame.transform.scale(padPicture, [pad.width, pad.height]) #pad.png pildi suuruseks määratakse 120x20 ja see saab muutuja "pad" uueks väärtuseks.

score = 0 #Muutuja score algväärtus on 0.

font = pygame.font.Font(pygame.font.match_font('Daytona'), 30) #Määratakse scorei font ja suurus.
text = font.render("score: " + str(score), True, [255,255,255]) #Määratakse scorei näitamine. Määratakse teksti värv.


running = True #Muutuja running saab tõeväärtuse True.
while (running): #While tsükkel mille tingimuseks on muutuja running tõene tõeväärtus.
    clock.tick(60)  #60 kaadrit sekundis.
    screen.fill([173, 216, 230])  #Taust värvitakse helesiniseks.

    screen.blit(text, [10, 20])  #Muutujale text antud väärtus kuvatakse aknas koordinaatidel x=10 ja y=20.
    text = font.render("score: " + str(score), True, [255, 255, 255])  #Määratakse scorei näitamine. Määratakse teksti värv.
    
    ball = pygame.Rect(posX, posY, 20, 20) #Luuakse rect objekt mille sisse mahutatakse palli pilt.
    screen.blit(ballPicture, ball) #Aknas kuvatakse pall, parameetriteks on muutuja "ballPicture".

    #Palli asukoht ja kiirus.
    posX += speedX 
    posY += speedY 

    #Kokkupõrke tuvastamine ja suuna muutmine.
    if posX > screenX - ballPicture.get_rect().width or posX < 0: #Kui muutuja posX on suurem kui screenX ja ballPicture.get_rect().width vahe või muutuja posX väärtus on väiksem kui 0.
        speedX = -speedX #Muudetakse muutuja speedX väärtus vastupidiseks.

    if posY > screenY - ballPicture.get_rect().height or posY < 0: #Kui muutuja posY on suurem kui screenY ja ballPicture.get_rect().width vahe või muutuja posY väärtus on väiksem kui 0.
        speedY = -speedY #Muudetakse muutuja speedY väärtus vastupidiseks.


    pad = pygame.Rect(posX2, posY2, 120, 20) #Luuakse rect objekt mille sisse mahutatakse aluse pilt.
    screen.blit(padPicture, pad) #Aknas kuvatakse alus, parameetriteks on muutuja padPicture.

    posX2 += speedX2 #Muutuja posX2 väärtus suureneb muutuja speedX2 väärtuse võrra.

    if posX2 > screenX - padPicture.get_rect().width or posX2 < 0: #Kui muutuja posX2 on suurem kui screenX ja padPicture.get_rect().width vahe või muutuja posX2 väärtus on väiksem kui 0.
        speedX2 = -speedX2 #Muudetakse muutuja speedX2 väärtus vastupidiseks.

    #Skoori kasvamine 1 võrra.
    if ball.colliderect(pad) and speedY > 0: #Kui muutujate ball ja pad vahel toimub kokkupõrge ja muutuja speedY väärtus on suurem kui 0.
        score += 1 #Muutuja score väärtus suureneb 1 võrra.
        speedY = -speedY #Muutuja speedY väärtus muudetakse vastupidiseks.

    #Skoori vähendamine 1 võrra.
    if posY > screenY - ballPicture.get_rect().height: #Kui muutuja posY on suurem kui screenY ja ballPicture.get_rect().width vahe.
        score -= 1 #Muutuja score väärtus väheneb 1 võrra.

    #Programmi ristist sulgemine.
    for event in pygame.event.get(): #Iga event väärtus pygame.event.get().
        if event.type == pygame.QUIT: #Kui event.type on võrdeline pygame.QUIT väärtusega.
            running = False #Muutuja running saab väärtuseks False ehk programm sulgub.
    pygame.display.flip() #Akna värskendamine.