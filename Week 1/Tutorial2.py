import viz
import vizshape

#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

viz.go()

#Increase the Field of View
viz.MainWindow.fov(60)

piazza = viz.addChild('piazza.osgb')
vizshape.addAxes()

viz.MainView.move([10,0,0]) 

#viz.MainView.setPosition([0,15,-15])

#viz.MainView.setEuler([0,30,0]) 



#viz.MainView.setEuler([0,90,0]) 
viz.MainView.setPosition([0,5,0]) 
viz.MainView.setEuler([0,90,0]) 
