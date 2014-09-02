import viz
import vizshape

viz.go()

# load the pre-made scene
piazza = viz.addChild('piazza.osgb')

# enable collision detection so we can't move through objects
viz.collision(viz.ON)


# add the axes model
vizshape.addAxes()

# add the plant
plant = viz.addChild('plant.osgb')
# plant will be at X=4, Y=0, Z=6; relative to the origin
plant.setPosition(4, 0, 6)

