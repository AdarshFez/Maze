# maze.py starter Code

import viz
import vizshape
import vizcam
import math

# An instance of this class adds a maze to the scene along with 
# an avatar that can be navigated through it.
class Maze(viz.EventClass):

	# Constructor 
	def __init__(self):
		# base class constructor 
		viz.EventClass.__init__(self)
		
		# set up keyboard and timer callback methods
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		
		# avatar's x,z location in maze and its rotation angle
		self.theta = 0
		self.x = 5
		self.z = 2
		self.y = 1
		self.first = False
		self.bird = True
		self.birdX =20
		self.birdY = 15
		self.birdZ  =5
		# The 2D array below stores the representation of a maze.
		# Array entries containing a 2 represent 1 x 2 x 1 wall blocks.
		# Array entries containing a 0 represent 1 x 0.1 x 1 floor blocks.
		self.maze = []
		self.maze = [[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]] + self.maze
		self.maze = [[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]] + self.maze # row 8
		self.maze = [[4,0,0,0,0,0,0,0,1,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,4]] + self.maze
		self.maze = [[4,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,4]] + self.maze # row 7
		self.maze = [[4,0,0,4,4,0,0,4,4,0,0,4,4,0,0,4,4,0,0,4,4,0,0,4,4,0,0,4]] + self.maze
		self.maze = [[4,1,1,4,4,0,0,4,4,0,0,4,4,1,1,4,4,0,0,4,4,0,0,4,4,1,1,4]] + self.maze
		self.maze = [[4,0,0,4,4,0,0,4,4,0,0,4,4,0,0,4,4,0,0,4,4,0,0,4,4,0,0,4]] + self.maze
		self.maze = [[4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4]] + self.maze
		self.maze = [[4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4]] + self.maze
		self.maze = [[4,0,0,4,4,4,0,0,4,0,0,4,4,4,4,4,4,0,0,0,4,0,0,0,4,0,0,4]] + self.maze
		self.maze = [[4,0,0,4,4,4,0,0,4,0,0,4,4,4,4,4,4,0,0,0,4,0,0,4,4,0,0,4]] + self.maze
		self.maze = [[4,0,0,4,4,4,0,0,4,0,0,4,4,4,4,4,4,0,0,0,4,0,0,4,4,0,0,4]] + self.maze
		self.maze = [[4,1,1,4,4,4,0,0,4,1,1,4,4,4,4,4,4,0,0,4,4,1,1,1,4,0,0,4]] + self.maze
		self.maze = [[4,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,4]] + self.maze
		self.maze = [[4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,4]] + self.maze
		self.maze = [[4,0,0,0,0,0,0,4,4,0,0,4,4,0,0,4,4,4,0,0,4,0,0,4,4,1,1,4]] + self.maze
		self.maze = [[4,0,0,4,4,0,0,4,4,0,0,4,4,0,0,4,4,0,0,0,4,0,0,4,4,0,0,4]] + self.maze
		self.maze = [[4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,1,0,0,0,4]] + self.maze
		self.maze = [[4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,4]] + self.maze
		self.maze = [[4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,4]] + self.maze
		self.maze = [[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]] + self.maze
		self.maze = [[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]] + self.maze
		
		view = viz.MainView
		mat = viz.Matrix()
		mat.postAxisAngle(0,1,0,270)
		mat.postAxisAngle(0,0,1,40)
		mat.postTrans(self.birdX,self.birdY,self.birdZ)
		view.setMatrix(mat)
		# Add +x,+y,+z coordinate axes to scene to help with placing the blocks correctly
		self.addCoordinateAxes()
		
		# Code to create blocks forming the maze goes here
		for row in range(0,len(self.maze)):
			for i in range(0,len(self.maze[row])):
				#* self.maze[i]
				if(self.maze[row][i] == 4):
					block = vizshape.addCube(size = 1.0 , color = viz.GREEN)
				elif(self.maze[row][i] ==1):
					block = vizshape.addCube(size = 1.0 , color = viz.BLUE)
				else:
					block = vizshape.addCube(size = 1.0 , color = viz.YELLOW)
				m = viz.Matrix()
				xx = .5
				yy = .5
				zz = .5
				if(row != 0 ):
					xx = xx + (row * 1)
				if(i != 0):
					zz = zz + (i*1)
				m.postTrans(xx,yy,zz)
				
				if(self.maze[row][i] == 4):
					
					m.postScale(1,4.0,1)
				elif(self.maze[row][i] == 1):
					m.postScale(1,1.5,1)	
				else:
					m.postScale(1,1,1)
				block.setMatrix(m)	
				
		self.avatar = viz.add('vcc_female.cfg')
		self.theta = 0
		m = viz.Matrix()
		m.postTrans(self.x,self.y,self.z)
		
		m.postAxisAngle(0,1,0,self.theta)
		self.avatar.setMatrix(m)
		
		############################################HERE##########################
		if(False):
			for i in range(0,15):
				self.avatar = viz.add('vcc_female.cfg')
				self.theta = 0
				m = viz.Matrix()
				m.postTrans(5,.5,2)
				self.avatar.state(i)
				m.postAxisAngle(0,1,0,self.theta)
				self.avatar.setMatrix(m)
			
		
		
	# Key pressed down event code.
	
	def onKeyDown(self,key):
		
		
		if (key == viz.KEY_RIGHT):
			self.theta = self.theta + 5
			m = viz.Matrix()
			
			
			m.postAxisAngle(0,1,0,self.theta)
			m.postTrans(self.x,self.y,self.z)
			self.avatar.setMatrix(m)
			
		if (key == viz.KEY_LEFT):
			self.theta = self.theta - 5
			m = viz.Matrix()
			
			
			m.postAxisAngle(0,1,0,self.theta)
			m.postTrans(self.x,self.y,self.z)
			self.avatar.setMatrix(m)
			
		if (key == viz.KEY_DOWN):
			m = viz.Matrix()
			self.moveZ = math.cos(math.radians(self.theta))
			self.moveX = math.sin(math.radians(self.theta))
			#m.postTrans(self.moveX,self.y,self.moveZ)
			self.x = self.x - self.moveX
			self.z = self.z - self.moveZ
			m.postAxisAngle(0,1,0,self.theta)
			m.postTrans(self.x,self.y,self.z)
			self.avatar.setMatrix(m)
			print(self.x)
			print(self.z)
			
			
		if (key == viz.KEY_UP):
			m = viz.Matrix()
			self.moveZ = math.cos(math.radians(self.theta))
			self.moveX = math.sin(math.radians(self.theta))
			#m.postTrans(self.moveX,self.y,self.moveZ)
			self.x = self.x + self.moveX
			self.z = self.z + self.moveZ
			m.postAxisAngle(0,1,0,self.theta)
			m.postTrans(self.x,self.y,self.z)
			self.avatar.setMatrix(m)
			
			print(self.x)
			print(self.z)
		if (key == '1'):
			view = viz.MainView
			mat = viz.Matrix()
			mat.postAxisAngle(1,0,0,90)
			mat.postTrans(0,20,0)
			view.setMatrix(mat)
			self.first = False
			self.bird = False
		if (key == '2'):
			view = viz.MainView
			mat = viz.Matrix()
			mat.postAxisAngle(0,1,0,270)
			
			mat.postAxisAngle(0,0,1,40)
			mat.postTrans(self.birdX,self.birdY,self.birdZ)
			view.setMatrix(mat)
			self.first = False
			self.bird = True
		if (key == '3' or self.first):
			view = viz.MainView
			mat = viz.Matrix()
			mat.postAxisAngle(0,1,0,self.theta)
			mat.postTrans(self.x,self.y+1.0,self.z)
			view.setMatrix(mat)
			self.first = True
			self.bird = False
		if (self.bird == True):
			if (key == 'a'):
				self.birdZ = self.birdZ -1
				view = viz.MainView
				mat = viz.Matrix()
				mat.postAxisAngle(0,1,0,270)
				mat.postAxisAngle(0,0,1,40)
				mat.postTrans(self.birdX,self.birdY,self.birdZ)
				view.setMatrix(mat)
			elif (key == 'd'):
				view = viz.MainView
				self.birdZ = self.birdZ + 1
				mat = viz.Matrix()
				mat.postAxisAngle(0,1,0,270)
				mat.postAxisAngle(0,0,1,40)
				mat.postTrans(self.birdX,self.birdY,self.birdZ)
				view.setMatrix(mat)
				print(self.birdZ)
			elif (key == 'w'):
				view = viz.MainView
				self.birdX = self.birdX - 1
				mat = viz.Matrix()
				mat.postAxisAngle(0,1,0,270)
				mat.postAxisAngle(0,0,1,40)
				mat.postTrans(self.birdX,self.birdY,self.birdZ)
				view.setMatrix(mat)
				print(self.birdX)
			elif (key == 's'):
				view = viz.MainView
				self.birdX = self.birdX +1
				mat = viz.Matrix()
				mat.postAxisAngle(0,1,0,270)
				mat.postAxisAngle(0,0,1,40)
				mat.postTrans(self.birdX,self.birdY,self.birdZ)
				view.setMatrix(mat)
				print(self.birdX)
				
	# Adds coodinate system that originates at (0,0,0) and extends
	# down the +x, +y, and +z directions.  Locations 1 and 2 units
	# in each direction are marked on the axis.
	def addCoordinateAxes(self):
		viz.startLayer(viz.LINES)
		viz.linewidth(7)
		viz.vertexColor( viz.RED )
		# positive y axis
		viz.vertex(0,0,0); 	   viz.vertex(0,20,0)
		#positive x axis
		viz.vertex(0,0,0); 	   viz.vertex(20,0,0)
		#positive z axis
		viz.vertex(0,0,0); 	   viz.vertex(0,0,20)
		#y=1 tick mark
		viz.vertex(-0.25,1,0); viz.vertex(0.25,1,0)
		#y=2 tick mark
		viz.vertex(-0.25,2,0); viz.vertex(0.25,2,0)
		#x=1 tick mark
		viz.vertex(1,0,-.25);  viz.vertex(1,0,.25)
		#x=2 tick mark
		viz.vertex(2,0,-.25);  viz.vertex(2,0,+.25)
		#z=1 tick mark
		viz.vertex(-.25,0,1);  viz.vertex(.25,0,1)
		#z=2 tick mark
		viz.vertex(-.25,0,2);  viz.vertex(.25,0,2)
		viz.endLayer()
		

