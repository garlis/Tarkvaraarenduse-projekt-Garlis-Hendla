#https://github.com/garlis/Tarkvaraarenduse-projekt-Garlis-Hendla

import pygame #Impordib pygamei.
pygame.init()

screen=pygame.display.set_mode([300,300]) #Määrab akna suuruse.
pygame.display.set_caption("Valgusfoor - Garlis Hendla") #Määrab akna pealkirja.

#Defineeritakse värvid.
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

pygame.draw.rect(screen, [255, 225, 255], [100, 10, 100, 280], 2) #Joonistab foori ümbrise ristküliku.
pygame.display.flip()

pygame.draw.circle(screen, [255, 0, 0], [150,60], 40, 100) #Joonistab punase foori tule ringi.
pygame.display.flip()

pygame.draw.circle(screen, [255, 255, 0], [150,150], 40, 100) #Joonistab kollase foori tule ringi.
pygame.display.flip()

pygame.draw.circle(screen, [0, 255, 0], [150,245], 40, 100) #Joonistab rohelise foori tule ringi.
pygame.display.flip()
