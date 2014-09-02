import viz

#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

viz.go()

#Increase the Field of View
viz.MainWindow.fov(60)

piazza = viz.addChild('piazza.osgb')

male = viz.addAvatar('vcc_male.cfg')
male.setPosition([4.5, 0, 7])
male.setEuler([0,0,0])

female = viz.addAvatar('vcc_female.cfg')
female.setPosition([4.5,0,9])
female.setEuler([180,0,0]) 

male.state(14)
female.state(14)

import random

pigeons = []
for i in range(10):
    
    #Generate random values for position and orientation
    x = random.randint(-4,3)
    z = random.randint(4,8)
    yaw = random.randint(0,360)
    
    #Load a pigeon
    pigeon = viz.addAvatar('pigeon.cfg')
    
    #Set position, orientation, and state
    pigeon.setPosition([x,0,z])
    pigeon.setEuler([yaw,0,0])
    pigeon.state(1)
    
    #Append the pigeon to a list of pigeons
    pigeons.append(pigeon) 
 

