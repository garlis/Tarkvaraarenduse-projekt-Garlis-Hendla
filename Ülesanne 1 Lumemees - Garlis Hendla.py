
import pygame #Impordib pygamei.
pygame.init()

screen=pygame.display.set_mode([300,300]) #Määrab akna suuruse.
pygame.display.set_caption("Lumemees - Garlis Hendla") #Määrab aknale nime.

#Defineeritakse värvid.
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0) 


pygame.draw.circle(screen, [255, 255, 255], [150,85], 30, 100) #Joonistab lumemehe keha.
pygame.display.flip()

pygame.draw.circle(screen, [255, 255, 255], [150,140], 40, 100) #Joonistab lumemehe keha.
pygame.display.flip()

pygame.draw.circle(screen, [255, 255, 255], [150,230], 60, 100) #Joonistab lumemehe keha.
pygame.display.flip()

pygame.draw.circle(screen, [0, 0, 0], [140,80], 5, 100) #Joonistab lumemehe silma.
pygame.display.flip()

pygame.draw.circle(screen, [0, 0, 0], [160,80], 5, 100) #Joonistab lumemehe silma.
pygame.display.flip()

pygame.draw.polygon(screen, (255, 0, 0), [(145, 80), (155, 80), (150, 95)]) #Joonistab lumemehe nina.
pygame.display.flip()








