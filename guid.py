import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
import random
import pgzrun
import pygame
import uuid

pygame.mixer.music.load("song.mp3") #cynicmusic
pygame.mixer.music.play(-1)

level=-1
message=""
gemacht=False

def generate_guid():
    global message,gemacht,guid
    if not gemacht:
        guid = uuid.uuid4()
        gemacht=True
        print(guid)
    message+="Created GUID: "+str(guid)
    return guid

def draw():
    global level,message
    screen.clear()
    if level == -1:
        screen.blit("title", (0, 0))
    elif level == 0:
        screen.blit("intro", (0, 0))
    elif level == 1:
        screen.blit("back", (0, 0))
        screen.draw.text("GUID:", center=(400, 300), fontsize=24, color=(25, 200, 255))
        screen.draw.text(str(generate_guid()), center=(400, 400), fontsize=24, color=(255, 255, 0))

def on_key_down(key, unicode=None):
    global level
    if key==keys.ESCAPE:
        pygame.quit()
        
def update():
    global level,gemacht
    if (level == 0 or level==-2) and keyboard.RETURN:
        level +=1
        gemacht=False
    elif level -1 and keyboard.space:
        level = 0
    if level==1:
        if not gemacht:
            generate_guid()
            gemacht=True
    if level==1 and keyboard.space:
        level=0

pgzrun.go()

