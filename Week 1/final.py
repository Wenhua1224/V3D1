import viz
import random
import vizact


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


def walkAvatars():
    walk1 = vizact.walkTo([4.5, 0,-40])
    vizact.ontimer2(0.5,0,female.addAction,walk1)

    walk2 = vizact.walkTo([3.5,0,-40])
    male.addAction(walk2)

	

def pigeonsFeed():

    random_speed = vizact.method.setAnimationSpeed(0,vizact.randfloat(0.7,1.5))
    random_walk = vizact.walkTo(pos=[vizact.randfloat(-4,4),0,vizact.randfloat(3,7)])
    random_animation = vizact.method.state(vizact.choice([1,3],vizact.RANDOM))
    random_wait = vizact.waittime(vizact.randfloat(5.0,10.0))
    pigeon_idle = vizact.sequence( random_speed, random_walk, random_animation, random_wait, viz.FOREVER)

    for pigeon in pigeons:
        pigeon.addAction(pigeon_idle)
        


vizact.onkeydown('w',walkAvatars) 
vizact.onkeydown('p',pigeonsFeed) 



'''
duck = viz.addAvatar('duck.cfg')
duck.setPosition([-4, 0, 7])
duck.setScale(0.3,0.3,0.3)

duck.setEuler([90,0,0])


duck_walk = vizact.walkTo([4, 0, 7])
duck.addAction(duck_walk )


image1=viz.addChild('body.cfg')
image1.setPosition([0,0.2,0])
image1.setScale(0.02,0.02,0.02)
image1.addAction( vizact.spin(0,1,0,20) )

image2= viz.addChild('wheel.cfg',parent=image1)
image2.setScale(0.2,0.2,0.2)


baby= viz.addChild('vcc_male2.cfg',parent=duck)
baby.setPosition([-4,0,10])
baby.setScale(0.2,0.2,0.2)

'''

carousel = viz.addChild('carousel.wrl')
carousel.setPosition([0,0,5])
carousel.setScale(0.3,0.3,0.3)
carousel.addAction( vizact.spin(0,1,0,20) )

pole = viz.addChild('pole.wrl',parent=carousel)
pole.setPosition([2,0,0])

horse = viz.addChild('horse.wrl',parent=pole)
horse.setEuler([180,0,0])
