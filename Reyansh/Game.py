import random as ran
import pygame as py
#setup
py.init()
windowwidth = 500
windowheight = 500
window = py.display.set_mode((windowwidth,windowheight))
py.display.set_caption("My First Game")
clock = py.time.Clock()
player = py.Rect(20,20,20,20) #x,y,width,height
rock = py.Rect(0,0,30,30)
# can access multiple properties of the rect
# top, bottom, right,left,top-right, x,y,width,height

#draw loop
while True:
    #check for events
    ev = py.event.poll() # gets the latest event
    if ev.type == py.QUIT:
        break
    keys = py.key.get_pressed() # a list of all current keys pressed
    if keys[py.K_d]:
      player.x+=5    
    if keys[py.K_a]:
      player.x-=5
    if keys[py.K_w]:
      player.top-=5
    if keys[py.K_s]:
      player.top+=5 

      
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
    mouseX,mouseY = py.mouse.get_pos()

    #player.centerx = mouseX
    #player.centery = mouseY


    #draw here
    py.draw.rect(window,(0,0,0),player) # surface,color (RGB), x,y,width,height
    py.draw.rect(window,(0,0,255),rock) 
    if(player.colliderect(rock)==True):  #if blue square collided with black square
      print("collided")
      rock = (ran.randint(0,400),ran.randint(0,400),30,30)
    py.display.flip()
    clock.tick(60)
py.quit()
