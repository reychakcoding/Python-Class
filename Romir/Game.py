
import pygame as py
import math

#setup
py.init()
windowwidth = 500
windowheight = 500
window = py.display.set_mode((windowwidth,windowheight))
py.display.set_caption("My First Game")
clock = py.time.Clock()
player = py.Rect(20,20,30,30)
bullet = py.Rect(50,50,10,10)#x,y,width,height
zombie = py.Rect(400,400,20,20)
# can access multiple properties of the rect
# top, bottom, right,left,top-right, x,y,width,height

def getangle(x1,y1,x2,y2):
  return math.atan2(y2-y1,x2-x1)

#draw loop
while True:
    #check for events
    ev = py.event.poll() # gets the latest event
    if ev.type == py.QUIT:
        break
    keys = py.key.get_pressed() # a list of all current keys pressed
    if keys[py.K_d]:
      player.x+=10    
    if keys[py.K_a]:
      player.x-=10
    if keys[py.K_w]:
      player.top-=10
    if keys[py.K_s]:
      player.top+=10 

      
    if ev.type == py.MOUSEBUTTONDOWN:
      print(getangle(player.centerx, player.centery, mouseX, mouseY))
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


    if player.right >= 500:
      player.right -= 10
      
    if player.left <= 0:
      player.left += 10
      
    if player.bottom >= 500:
      player.bottom -= 10
      
    if player.top <= 0:
      player.top += 10

    #draw here
    py.draw.rect(window,(0,0,0),player)
    py.draw.rect(window,(255,0,0),bullet)
    py.draw.rect(window,(0,255,0),zombie)# surface,color (RGB), x,y,width,height
    py.display.flip()
    clock.tick(60)
py.quit()
