# main.py
# Driver code for graphics hw
  
import viz
import vizshape
import vizcam
import math

from Maze import *

# set size (in pixels) and title of application window
viz.window.setSize( 640, 480 )
viz.window.setName( "Maze runner Scene" )

# get graphics window
window = viz.MainWindow
# setup viewing volume

# set background color of window to blue 
#black
#viz.MainWindow.clearcolor( [0,0,0] ) 
#blue
#viz.MainWindow.clearcolor( [0,0,150] )
#new color
viz.MainWindow.clearcolor( [0,0,200] )

# allows mouse to rotate, translate, and zoom in/out on object
pivotNav = vizcam.PivotNavigate()

c = Maze()

# render the scene in the window
viz.go()
