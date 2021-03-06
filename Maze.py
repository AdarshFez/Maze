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
		self.maze = [[4,0,2,4,4,0,2,0,0,2,0,2,0,0,2,0,0,2,0,0,4,0,2,0,0,2,0,4]] + self.maze
		self.maze = [[4,0,2,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,2,0,4,2,0,2,0,0,2,4]] + self.maze
		self.maze = [[4,2,0,0,2,0,0,4,4,2,0,4,4,0,2,4,4,4,0,2,4,0,0,4,4,1,1,4]] + self.maze
		self.maze = [[4,0,2,4,4,0,2,4,4,0,0,4,4,2,0,4,4,0,2,0,4,0,2,4,4,0,2,4]] + self.maze
		self.maze = [[4,2,0,0,4,2,0,1,0,2,0,2,0,0,2,4,4,0,2,0,0,2,0,1,0,2,0,4]] + self.maze
		self.maze = [[4,0,0,2,0,0,2,1,2,0,0,2,0,2,0,1,0,0,2,0,0,2,0,1,2,0,0,4]] + self.maze
		self.maze = [[4,0,2,0,2,0,0,1,2,0,2,0,0,0,2,1,0,2,0,0,2,0,0,1,0,2,0,4]] + self.maze
		##################################################################################
		self.maze = [[4,0,2,0,2,0,0,1,2,0,2,0,0,0,2,1,0,2,0,0,2,0,0,1,0,2,0,4]] + self.maze
		self.maze = [[4,0,0,2,0,0,2,1,2,0,0,2,0,2,0,1,0,0,2,0,0,2,0,1,2,0,0,4]] + self.maze
		self.maze = [[4,2,0,0,4,2,0,1,0,2,0,2,0,0,2,4,4,0,2,0,0,2,0,1,0,2,0,4]] + self.maze
		self.maze = [[4,0,2,4,4,0,2,4,4,0,0,4,4,2,0,4,4,0,2,0,4,0,2,4,4,0,2,4]] + self.maze
		self.maze = [[4,2,0,0,2,0,0,4,4,2,0,4,4,0,2,4,4,4,0,2,4,0,0,4,4,1,1,4]] + self.maze
		self.maze = [[4,0,2,0,0,2,0,0,2,0,0,0,2,0,0,2,0,0,2,0,4,2,0,2,0,0,2,4]] + self.maze
		self.maze = [[4,0,2,4,4,0,2,0,0,2,0,2,0,0,2,0,0,2,0,0,4,0,2,0,0,2,0,4]] + self.maze
		self.maze = [[4,1,1,4,4,4,0,2,4,1,1,4,4,4,4,4,4,0,0,4,4,1,1,1,4,2,0,4]] + self.maze
		self.maze = [[4,2,0,4,4,4,2,0,4,2,0,4,4,4,4,4,4,0,0,0,4,2,0,4,4,0,2,4]] + self.maze
		self.maze = [[4,0,2,4,4,4,0,2,4,0,2,4,4,4,4,4,4,2,0,0,4,0,2,4,4,2,0,4]] + self.maze
		self.maze = [[4,2,0,4,4,4,2,0,4,2,0,4,4,4,4,4,4,0,2,0,4,2,0,0,4,0,2,4]] + self.maze
		self.maze = [[4,0,2,0,0,2,0,0,2,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,4]] + self.maze
		self.maze = [[4,0,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,0,4]] + self.maze
		self.maze = [[4,0,2,4,4,0,0,4,4,0,0,4,4,2,0,4,4,2,0,4,4,0,2,4,4,2,0,4]] + self.maze
		self.maze = [[4,1,1,4,4,0,0,4,4,2,0,4,4,1,1,4,4,0,2,4,4,2,0,4,4,1,1,4]] + self.maze
		self.maze = [[4,0,2,4,4,2,0,4,4,0,0,4,4,0,2,4,4,2,0,4,4,0,0,4,4,2,0,4]] + self.maze
		self.maze = [[4,2,0,0,2,0,2,0,1,0,2,0,0,2,0,1,1,0,2,0,0,2,0,0,2,0,0,4]] + self.maze
		self.maze = [[4,0,0,2,0,0,2,0,1,0,0,2,0,0,2,1,1,0,0,2,0,0,2,0,0,2,0,4]] + self.maze
		self.maze = [[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]] + self.maze
		
		view = viz.MainView
		mat = viz.Matrix()
		mat.postAxisAngle(0,1,0,270)
		mat.postAxisAngle(0,0,1,40)
		mat.postTrans(self.birdX,self.birdY,self.birdZ)
		view.setMatrix(mat)
		
		self.blocks = []
		# Code to create blocks forming the maze goes here
		for row in range(0,len(self.maze)):
			for i in range(0,len(self.maze[row])):
				#* self.maze[i]
				if(self.maze[row][i] == 4):
					block = vizshape.addCube(size = 1.0 , color = viz.RED)
				elif(self.maze[row][i] ==1):
					block = vizshape.addCube(size = 1.0 , color = viz.BLUE)
				else:
					block = vizshape.addCube(size = 1.0 , color = viz.BLACK)
				m = viz.Matrix()
				xx = 1
				yy = .5
				zz = 1
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
				self.blocks = [[xx,zz]] + self.blocks
				block.setMatrix(m)
				
		for row in range(0,len(self.maze)):
			for i in range(0,len(self.maze[row])):
				if(self.maze[row][i] == 2):
					#self.sphere = vizshape.addSphere(.125,10,10)
					self.sphere = Sphere()
					
					m = viz.Matrix()
					xx = 1
					yy = 1.5
					zz = 1
					if(row != 0 ):
						xx = xx + (row * 1)
					if(i != 0):
						zz = zz + (i*1)
					m.postTrans(xx,yy,zz)
					self.sphere.setXZ(xx,zz)
					self.listAlien.append(self.sphere)
					self.sphere.vertices.setMatrix(m)
					
		self.avatar = viz.add('vcc_female.cfg')
		m = viz.Matrix()
		m.postTrans(self.x,self.y,self.z)
		m.postAxisAngle(0,1,0,self.theta)
		self.avatar.setMatrix(m)
		
		self.monster = viz.add('vcc_female.cfg')
		m = viz.Matrix()
		m.postTrans(self.monX,self.monY,self.monZ)
		m.postAxisAngle(0,1,0,self.theta)
		self.monster.setMatrix(m)
		
	# Key pressed down event code.
	
	def onKeyDown(self,key):
		if (key == viz.KEY_RIGHT):
			self.theta = self.theta + 90
			m = viz.Matrix()
			m.postAxisAngle(0,1,0,self.theta)
			m.postTrans(self.x,self.y,self.z)
			self.avatar.setMatrix(m)
			if(self.theta == 360):
				self.theta = 0
			
		if (key == viz.KEY_LEFT):
			self.theta = self.theta - 90
			m = viz.Matrix()
			m.postAxisAngle(0,1,0,self.theta)
			m.postTrans(self.x,self.y,self.z)
			self.avatar.setMatrix(m)
			if(self.theta == -360):
				self.theta = 0
			
		if (key == ' '):
			self.isValid = False
			if(self.theta == 90 or self.theta == -270):
				if(self.maze[int(self.x)][int(self.z-1)] == 1):
					self.isValid = True
			elif(self.theta == 0):
				if(self.maze[int(self.x-1)][int(self.z)] == 1):
					self.isValid = True
			elif(self.theta == 270 or self.theta == -90):
				if(self.maze[int(self.x-2)][int(self.z-1)] == 1):
					self.isValid = True
			elif(self.theta == 180 or self.theta == -180):
				if(self.maze[int(self.x-1)][int(self.z-2)] == 1):
					self.isValid = True										
			if(self.isValid and self.EndGame == False):
				if(self.theta == 90 or self.theta == -270):
					self.x = self.x + 2
				elif(self.theta == 0):
					self.z = self.z + 2
				elif(self.theta == 270 or self.theta == -90):
					self.x = self.x - 2
				elif(self.theta == 180 or self.theta == -180):
					self.z = self.z - 2
				m = viz.Matrix()
				m.postAxisAngle(0,1,0,self.theta)
				m.postTrans(self.x,self.y,self.z)
				self.avatar.setMatrix(m)
			
		if (key == viz.KEY_DOWN):
			self.isValid = False
			if(self.theta == 270 or self.theta == -90):
				if(self.maze[int(self.x)][int(self.z-1)] == 0 or self.maze[int(self.x)][int(self.z-1)] == 2):
					self.isValid = True
			elif(self.theta == 180 or self.theta == -180):
				if(self.maze[int(self.x-1)][int(self.z)] == 0 or self.maze[int(self.x-1)][int(self.z)] == 2):
					self.isValid = True
			elif(self.theta == 90 or self.theta == -270):
				if(self.maze[int(self.x-2)][int(self.z-1)] == 0 or self.maze[int(self.x-2)][int(self.z-1)] == 2):
					self.isValid = True
			elif(self.theta == 0):
				if(self.maze[int(self.x-1)][int(self.z-2)] == 0 or self.maze[int(self.x-1)][int(self.z-2)] == 2):
					self.isValid = True										
			if(self.isValid and self.EndGame == False):
				m = viz.Matrix()
				self.moveZ = math.cos(math.radians(self.theta))
				self.moveX = math.sin(math.radians(self.theta))				
				self.x = self.x - self.moveX
				self.z = self.z - self.moveZ				
				m.postAxisAngle(0,1,0,self.theta)
				m.postTrans(self.x,self.y,self.z)
				self.avatar.setMatrix(m)
			
		if (key == viz.KEY_UP):
			self.isValid = False
			if(self.theta == 90 or self.theta == -270):
				if(self.maze[int(self.x)][int(self.z-1)] == 0 or self.maze[int(self.x)][int(self.z-1)] == 2):
					self.isValid = True
					
			elif(self.theta == 0):
				if(self.maze[int(self.x-1)][int(self.z)] == 0 or self.maze[int(self.x-1)][int(self.z)] == 2):
					self.isValid = True
			elif(self.theta == 270 or self.theta == -90):
				if(self.maze[int(self.x-2)][int(self.z-1)] == 0 or self.maze[int(self.x-2)][int(self.z-1)] == 2):
					self.isValid = True
			elif(self.theta == 180 or self.theta == -180):
				if(self.maze[int(self.x-1)][int(self.z-2)] == 0 or self.maze[int(self.x-1)][int(self.z-2)] == 2):
					self.isValid = True										
			if(self.isValid and self.EndGame == False):
				m = viz.Matrix()
				self.moveZ = math.cos(math.radians(self.theta))
				self.moveX = math.sin(math.radians(self.theta))				
				self.x = self.x + self.moveX
				self.z = self.z + self.moveZ				
				m.postAxisAngle(0,1,0,self.theta)
				m.postTrans(self.x,self.y,self.z)
				self.avatar.setMatrix(m)
		for spheres in self.listAlien:
						if(spheres.getX() == self.x and spheres.getZ() == self.z):
							spheres.setXZ(0,1000)	
							self.points = self.points + 1
							print(self.points)
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
		self.monsterMove()
		
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
				
			elif (key == 'w'):
				view = viz.MainView
				self.birdX = self.birdX - 1
				mat = viz.Matrix()
				mat.postAxisAngle(0,1,0,270)
				mat.postAxisAngle(0,0,1,40)
				mat.postTrans(self.birdX,self.birdY,self.birdZ)
				view.setMatrix(mat)
				
			elif (key == 's'):
				view = viz.MainView
				self.birdX = self.birdX +1
				mat = viz.Matrix()
				mat.postAxisAngle(0,1,0,270)
				mat.postAxisAngle(0,0,1,40)
				mat.postTrans(self.birdX,self.birdY,self.birdZ)
				view.setMatrix(mat)
		
			
	def monsterMove(self):
		self.shortest = 9999
		self.decidedX = -1
		self.decidedZ = -1
		if (self.monX == self.x and self.monZ == self.z):
			self.EndGame = True
			t = viz.addText("Total Points: "+ str(self.points),viz.SCREEN, pos = [0,0,0])
			p = viz.addText(str(self.points), viz.SCREEN, pos = [5,0,0])


		if(self.EndGame == False):
			
			
			if(self.x > self.monX and self.maze[int(self.monX+1)][int(self.monZ)] != 4):
				self.monX = self.monX + 1
			elif(self.x < self.monX and self.maze[int(self.monX-1)][int(self.monZ)] != 4):
					self.monX = self.monX -1
			elif(self.z > self.monZ and self.maze[int(self.monX)][int(self.monZ+1)] != 4):
					self.monX = self.monX + 1
			elif(self.z< self.monZ and self.maze[int(self.monX)][int(self.monZ-1)] != 4):
						self.monZ = self.monZ -1
			elif(self.monX == self.x and self.monZ == self.z):
				self.EndGame = True
			
			m = viz.Matrix()
			m.postTrans(int(self.monX),self.monY,int(self.monZ))
			
			self.monster.setMatrix(m)
			
