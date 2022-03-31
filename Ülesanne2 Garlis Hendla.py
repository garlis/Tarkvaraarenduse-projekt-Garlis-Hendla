#https://github.com/garlis/Tarkvaraarenduse-projekt-Garlis-Hendla

import pygame #Impordib pygamei.
pygame.init() #Paneb pygamei käima.
screen=pygame.display.set_mode([640, 480]) #Tekitab 640x480 suurusega akna.
pygame.display.set_caption("Ülesanne2 Garlis Hendla") #Paneb aknale nime.

shop = pygame.image.load("bg_shop.webp") #Teeb lahti taustapildi ehk poe.
screen.blit(shop,[0,0]) #Paneb paika pildi asukoha.

müüja = pygame.image.load("seller.webp") #Avab müüja pildi.
müüja = pygame.transform.scale(müüja, [260, 310]) #Paneb paika pildi mõõtmed, et se korralikult aknasse ära mahuks.
screen.blit(müüja,[105,155]) #Paneb paika pildi asukoha.

chat = pygame.image.load("chat.webp") #Avab teksti ala pildi.
chat = pygame.transform.scale(chat, [255, 205]) #Paneb paika pildi mõõtmed, et se korralikult aknasse ära mahuks.
screen.blit(chat, [245,65]) #Paneb paika pildi asukoha.

font = pygame.font.Font(pygame.font.match_font('arial'), 20) #Valib teksti fondi ja suuruse.
text = font.render("Tere, olen Garlis Hendla", True, [255, 255, 255]) #Lisab valge teksti.
text_width = text.get_rect().width #Teksti ala laius.
text_height = text.get_rect().height #Teksti ala kõrgus.
screen.blit(text, [370-text_width/2, 145-text_height/2]) # Paneb paika teksti asukoha.

pygame.display.flip() #Uuendab akent, et kõik asjad oleksid aknas kuvatud.

from sys import exit #Impordib sysist pygamei exit funktsiooni.
while True: #Alustab while tsükklit.
        for event in pygame.event.get(): #Registreerib kõik kasutaja sündmused.
            if event.type == pygame.QUIT: #Loob tingumuse, kui kasutaja sündmus on võrdeline pygamei sulgemisega, siis
                pygame.quit() #Sulgeb pygamei akna.
                exit() #Lõpetab while tsükkli.
