import random as ran
import pygame as py
#setup
py.init()
windowwidth = 500
windowheight = 500
window = py.display.set_mode((windowwidth,windowheight))
py.display.set_caption("My First Game")
clock = py.time.Clock()
player = py.Rect(windowwidth/2,windowheight/2,20,20) #x,y,width,height
rock = py.Rect(100,100,30,30)
font = py.font.Font(None,20)
score = 0
xspeed = 0
yspeed = 0
jetpack = 100
# can access multiple properties of the rect
# top, bottom, right,left,top-right, x,y,width,height

#draw loop
while True:
    #check for events
    ev = py.event.poll() # gets the latest event
    if ev.type == py.QUIT:
        break
    keys = py.key.get_pressed()# a list of all current keys pressed
    if (jetpack > 0):
      if keys[py.K_a]:
        xspeed = 2
        yspeed = 0
        jetpack=jetpack-0.25
      if keys[py.K_d]:
        xspeed= -2
        yspeed = 0
        jetpack=jetpack-0.25
      if keys[py.K_s]:
        yspeed = 2
        xspeed = 0
        jetpack=jetpack-0.25
      if keys[py.K_w]:
        yspeed = -2 
        xspeed = 0
        jetpack=jetpack-0.25
    rock.top-=yspeed
    rock.left+=xspeed
    if(player.colliderect(rock)==True):  #if blue square collided with black square
      print("collided")
      score = score+1
      rock = py.Rect(ran.randint(0,400),ran.randint(0,400),30,30) 
    if ev.type == py.MOUSEBUTTONDOWN:
      print("mouse is clicked")
    # event options
    # QUIT              none
    # KEYDOWN           key, mod, unicode, scancode
    # KEYUP             key, mod, unicode, scancode
    # MOUSEMOTION       pos, rel, buttons, touch
    # MOUSEBUTTONUP     pos, button, touch
    # MOUSEBUTTONDOWN   pos, button, touch
    
    window.fill("white")
    text = font.render("Your score is " + str(score) +". Jetpack fuel is " + str(jetpack),True,(0,0,0))
    mouseX,mouseY = py.mouse.get_pos()

    #player.centerx = mouseX
    #player.centery = mouseY


    #draw here
    py.draw.rect(window,(0,0,0),player) # surface,color (RGB), x,y,width,height
    py.draw.rect(window,(128,128,128),rock) 
    window.blit(text,(100,75))
    
    py.display.flip()
    clock.tick(60)
py.quit()
