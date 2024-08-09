import pygame as py
#setup
py.init()
windowwidth = 500
windowheight = 500
window = py.display.set_mode((windowwidth,windowheight))
clock = py.time.Clock()

#draw loop
while True:
    #check for events
    ev = py.event.poll()
    if ev.type == py.QUIT:
        break

    window.fill("white")
    
    #draw here
    
    py.display.flip()
    clock.tick(60)
py.quit()