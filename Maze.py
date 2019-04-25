# maze.py starter Code

import viz
import vizshape
import vizcam
import math
from Sphere import *
# An instance of this class adds a maze to the scene along with 
# an avatar that can be navigated through it.
class Maze(viz.EventClass):

	# Constructor 
	def __init__(self):
		# base class constructor 
		viz.EventClass.__init__(self)
		
		# set up keyboard and timer callback methods
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		
		
		self.listAlien = []
		self.points = 0
		# avatar's x,z location in maze and its rotation angle
		self.theta = 0
		self.x = 2
		self.z = 2
		self.y = 1
		self.monX = 2
		self.monY = 1
		self.monZ = 27
		self.first = False
		self.bird = True
		self.birdX =20
		self.birdY = 15
		self.birdZ  =5
		self.EndGame = False
		# The 2D array below stores the representation of a maze.
		# Array entries containing a 2 represent 1 x 2 x 1 wall blocks.
		# Array entries containing a 0 represent 1 x 0.1 x 1 floor blocks.
		self.maze = []
		#bottom left
		self.maze = [[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]] + self.maze
		self.maze = [[4,0,0,2,0,0,2,0,1,0,0,2,0,0,2,1,1,0,0,2,0,0,2,0,0,2,0,4]] + self.maze
		self.maze = [[4,2,0,0,2,0,2,0,1,0,2,0,0,2,0,1,1,0,2,0,0,2,0,0,2,0,0,4]] + self.maze
		self.maze = [[4,0,2,4,4,2,0,4,4,0,0,4,4,0,2,4,4,2,0,4,4,0,0,4,4,2,0,4]] + self.maze
		self.maze = [[4,1,1,4,4,0,0,4,4,2,0,4,4,1,1,4,4,0,2,4,4,2,0,4,4,1,1,4]] + self.maze
		self.maze = [[4,0,2,4,4,0,0,4,4,0,0,4,4,2,0,4,4,2,0,4,4,0,2,4,4,2,0,4]] + self.maze
		self.maze = [[4,0,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,0,4]] + self.maze
		self.maze = [[4,0,2,0,0,2,0,0,2,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,4]] + self.maze
		self.maze = [[4,2,0,4,4,4,2,0,4,2,0,4,4,4,4,4,4,0,2,0,4,2,0,0,4,0,2,4]] + self.maze
		self.maze = [[4,0,2,4,4,4,0,2,4,0,2,4,4,4,4,4,4,2,0,0,4,0,2,4,4,2,0,4]] + self.maze
		self.maze = [[4,2,0,4,4,4,2,0,4,2,0,4,4,4,4,4,4,0,0,0,4,2,0,4,4,0,2,4]] + self.maze
		self.maze = [[4,1,1,4,4,4,0,2,4,1,1,4,4,4,4,4,4,0,0,4,4,1,1,1,4,2,0,4]] + self.maze
		s
