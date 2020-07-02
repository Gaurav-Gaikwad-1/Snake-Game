import pygame
import random
import time
from pygame.locals import *

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,155,0)
maroon=(128,0,0)
yellow=(255,255,0)
orange=(187,154,23)

width=800                                                     #width and height for display window  size
height=600
pygame.init()
gamedisplay=pygame.display.set_mode((width,height))           #to set display screen
pygame.display.set_caption("GAURAV SNAKE'S GAME")

block_size=15                                               #size of snake(block)
clock=pygame.time.Clock()                                  #for small pauses on each iteration of gameloop so that our prog dont run 2 fast
fps=10      

applethickness=15

smallfont=pygame.font.Font(None,25)                             #loads the fonts
medfont=pygame.font.Font(None,50)
largefont=pygame.font.Font(None,80)

img = pygame.image.load('snakhead.png')                     #loading image of snake head
appleimg=pygame.image.load('apple.png')                     #loading image of apple

icon=pygame.image.load('snakeicon1.png')                    #loading image of window icon
pygame.display.set_icon(icon)

#bg=pygame.image.load('back .png')
#gamedisplay.blit(bg, [width, height])
direction="right"                                           #Setting initial direction of snake's head
def pause():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                quit()
            if event.type==KEYDOWN:
                if event.key== K_c:
                    paused=False
                elif event.key==K_q:
                    pygame.quit()
                    quit()
            gamedisplay.fill(green)
            message_to_screen("PAUSED",
                               black,
                               -80,
                               size="largefont"
                               )
            message_to_screen("PRESS C TO CONTINUE AND Q TO QUIT",
                               black,
                               -10,
                               size="medfont"
                               )
            pygame.display.update()
            clock.tick(5)

def score(score):                                                               #to keep count of apples eaten 
    text=smallfont.render("SCORE: "+str(score),True,black)
    gamedisplay.blit(text,[0,0])

def randapplegen():                                                             #to generate new positon for apple after eaten
    RandAppleX=round(random.randrange(0 ,width-applethickness))                   #to generate random x cordinate for position of apple
    RandAppleY=round(random.randrange(0 ,height-applethickness))
    return RandAppleX,RandAppleY


def snake(block_size, snakelist):                                                  #funt for rotating the snake's head as per user 
    if direction=="right":
        head=pygame.transform.rotate(img,270)
    elif direction=="left":
        head=pygame.transform.rotate(img,90)
    elif direction=="up":
        head=img
    elif direction=="down":
        head=pygame.transform.rotate(img,180)

    gamedisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))                   #only changing initial heads coordinate
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gamedisplay,orange,[XnY[0],XnY[1],block_size,block_size])                 #to display snake

def gameintro():                                                                    #entry window
    intro=True

    while intro==True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                quit()
            if event.type==KEYDOWN:
                if event.key== K_p:
                    intro=False
                if event.key==K_q:
                    pygame.quit()
                    quit()
        gamedisplay.fill(black)
        message_to_screen("WELCOME TO SNAKE GAME",
                               red,
                               y_displace=-70,
                               size="largefont")
        message_to_screen("PRESS P TO PLAY AGAIN AND Q TO QUIT",
                               green,
                               y_displace=30,
                               size="medfont")
        pygame.display.update()
        clock.tick(15)

def text_objects(text,color,size):
    if size=="smallfont":
        textsurface=smallfont.render(text,True,color) 
    elif size=="medfont":
        textsurface=medfont.render(text,True,color) 
    elif size=="largefont":
        textsurface=largefont.render(text,True,color)                          #render the text in new surface
    return textsurface,textsurface.get_rect()  

def message_to_screen(msg,color,y_displace=0,size="small"):                                     #function to print message on screen
    textsurf,textrect=text_objects(msg,color,size)
    textrect.center=(width/2),(height/2)+y_displace
    gamedisplay.blit(textsurf,textrect)                      

def gameloop():
    global direction
    val=False
    gameover= False

    lead_x=width/2                                                   #starting location of snake x coord
    lead_y=height/2                                                  # y coord...

    lead_x_change=0
    lead_y_change=0
    
    snakelist=[]                    #contains x & y values of snakes corrd
    snakelength=1
    point=0

    RandAppleX,RandAppleY=randapplegen()
    
    while not val:
        while gameover==True:

            gamedisplay.fill(white)
            message_to_screen("GAME OVER",
                               red,
                               y_displace=-50,
                               size="largefont")
            message_to_screen("PRESS P TO PLAY AGAIN AND Q TO QUIT",
                               maroon,
                               y_displace=20,
                               size="medfont")
            pygame.display.update()

            for event in pygame.event.get():
                if(events.type==QUIT):                  #to exit the window by clicking close button in window (right corner)
                    val=True
                    gameover=False

                if event.type==KEYDOWN:
                    if event.key==K_q:
                        gameover=False
                        val=True
                    if event.key==K_p:
                        gameloop() 
                 
        for events in pygame.event.get():
            if(events.type==QUIT):                  #to exit the window by clicking close button in window (right corner)
                val=True
            if(events.type==KEYDOWN):
                if(events.key==K_LEFT):
                    direction="left"
                    lead_x_change=-block_size                 
                    lead_y_change=0
                elif(events.key==K_RIGHT):
                    direction="right"
                    lead_x_change=block_size
                    lead_y_change=0
                elif(events.key==K_UP):
                    direction="up"
                    lead_y_change=-block_size        #while going up only y axis should be changing thats y
                    lead_x_change=0                  #we r setting x axis to 0
                elif(events.key==K_DOWN):
                    direction="down"
                    lead_y_change=block_size 
                    lead_x_change=0
                elif(events.key==K_p):
                    pause()
            # if(events.type==KEYUP):                                         if we want to move left or right only by pressing key n when we release button 
            #     if events.key==K_LEFT or events.key==K_RIGHT :              then it should stop moving use this but in snake game we want snake to move until
            #        lead_x_change=0                                      we press another key like up or down
                                                                                   
        if lead_x<=0 or lead_x>=width or lead_y<=0 or lead_y>=height:        #condn for quit if snake hits the boundaries
            gameover=True

        lead_x+=lead_x_change
        lead_y+=lead_y_change

        gamedisplay.fill(green)
        
        
        applethickness=15
        #pygame.draw.rect(gamedisplay,red,[RandAppleX,RandAppleY,applethickness,applethickness])       #to display apple
        gamedisplay.blit(appleimg,(RandAppleX,RandAppleY))

        snakehead=[]                    #to store head of snake (x coord & y coord)
        
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist)>snakelength:
            del snakelist[0]    

        for eachsegment in snakelist[: -1]:
            if eachsegment == snakehead:
                gameover=True  

        snake(block_size,snakelist)
        
        score(point)
        pygame.display.update()

        if lead_x > RandAppleX and lead_x < RandAppleX + applethickness or lead_x + block_size >RandAppleX and lead_x + block_size < RandAppleX + applethickness :
            if lead_y > RandAppleY and lead_y < RandAppleY + applethickness:
                RandAppleX,RandAppleY=randapplegen()
                snakelength+=1
                point+=10
            elif lead_y + block_size >RandAppleY and lead_y + block_siq6ze < RandAppleY + applethickness :
                RandAppleX,RandAppleY=randapplegen()
                snakelength+=1
                point+=10

        clock.tick(fps)

    pygame.quit()
    quit()
gameintro()
gameloop()