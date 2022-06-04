import numpy as np
import matplotlib.pyplot as plt

class Tank():
	"""Simulates tank and rate of water flow from tank."""
	def __init__(self, heightFromOpening, depthOfWater, width, length, diameterOfOpening):
		self.depthOfWater = depthOfWater
		self.heightFromOpening = heightFromOpening #height from base of tank to opening 
		self.volume = depthOfWater*width*length
		self.baseArea = length*width
		self.areaOfOpening = np.pi*(diameterOfOpening/2)**2
		self.timeElapsed = 0
		self.volumeLost = 0

		self.velocity = np.sqrt(2*9.81*(self.heightFromOpening+self.depthOfWater)) # from bernoulli's equation assuming water at the top of tank is moving a negligible velocity

	def advance(self, dt = 0.001):

		dv = self.velocity*dt*self.areaOfOpening # volume of 'capsule' of water leaving opening
		
		self.volumeLost += dv
		self.timeElapsed = self.timeElapsed + dt
		
		# calc new volume of tank and recalc related variables
		self.volume = self.volume - dv
		self.depthOfWater = self.volume / self.baseArea
		if self.depthOfWater < 0:
			return 
		self.velocity = np.sqrt(2*9.81*(self.heightFromOpening+self.depthOfWater))

		return dv,self.velocity,self.timeElapsed , self.volumeLost

tank = Tank(0.5,0.5,0.1,0.2,0.01)
energyTransfered  = []
velocities = []
times= []

def calcE(dv,vel,rho):
	m=dv*rho
	E=0.5*m*vel**2
	return E

while True:
	try:
		dv, vel, timeElapsed, volumeLost = tank.advance()
	except:
		break

	times.append(timeElapsed)
	velocities.append(vel)
	energyTransfered.append(calcE(dv,vel,997))

print(volumeLost)
plt.plot(times,energyTransfered)
plt.show()
plt.plot(times,velocities)
plt.show()




