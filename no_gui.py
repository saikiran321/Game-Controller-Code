import pygame
 
import lcm
from exlcm import xbox
#----------lcm init
lc = lcm.LCM("udpm://224.0.0.251:7667?ttl=1")

#-------pygame initialisation-------------
pygame.init()
done = False
clock = pygame.time.Clock()
pygame.joystick.init()

preval=''

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    joystick_count = pygame.joystick.get_count()
    finalvalues={'axis':{},'buttons':{},'hat':{}}
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        name = joystick.get_name()
        axes = joystick.get_numaxes()
 
        for i in range(axes):
            axis = joystick.get_axis(i)
    
            finalvalues['axis'][i+1]=axis
        buttons = joystick.get_numbuttons()
        for i in range(buttons):
            button = joystick.get_button(i)
            finalvalues['buttons'][i+1]=button
        
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        for i in range(hats):
            hat = joystick.get_hat(i)
            finalvalues['hat'][i+1]=hat
        if preval!=str(finalvalues):
            print (str(finalvalues))
            msg=xbox()
            msg.message=str(finalvalues)    
            lc.publish("3dpro", msg.encode())
            preval=str(finalvalues)

    
pygame.quit()