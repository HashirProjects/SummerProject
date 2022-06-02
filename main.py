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

		self.velocity = np.sqrt(2*9.81*(self.heightFromOpening+self.depthOfWater)) # from bernoulli's equation assuming water at the top of tank is moving a negligible velocity

	def advance(self, dt = 0.001):
		dv = self.velocity*dt*self.areaOfOpening # volume of 'capsule' leaving opening

		# calc new volume of tank and recalc related variables
		self.volume = self.volume - dv
		self.depthOfWater = self.volume / self.baseArea
		self.velocity = np.sqrt(2*9.81*(self.heightFromOpening+self.depthOfWater))

		return dv,self.velocity

tank = Tank(1,0.5,0.1,0.2,0.01)
energyTransfered  = []
def calcE(dv,vel):
	m=dv*997
	E=0.5*m*vel**2
	return E
for i in range(0,1000000):
	energyTransfered.append(calcE(*tank.advance()))
plt.plot(np.linspace(0,100000,len(energyTransfered)),energyTransfered)
plt.show()
	

# class Turbine():
# 	"""simulates the energy output of the turbine"""
# 	def __init__(self, mass, C, initialVelocity = 0):
# 		self.velocity = initialVelocity
# 		self.C = C
# 		self.mass = mass

# 	def advance(self,dv , waterVelocity, dt = 0.001): # uses momentum cons to calculate speed and power output of turbine
# 		#assuming capsule of water is reflected and density of water is 997 kg/m^3
# 		self.velocity = (self.C*2*dv*997*(waterVelocity-self.velocity) + self.mass*self.velocity)/self.mass
# 		#from source P = Fv = 2*dv*997*(waterVelocity-self.velocity)*self.velocity. E = P*dt
# 		energyTransfered = 2*dv*997*(waterVelocity-self.velocity)*self.velocity*dt

# 		#energyTakenByGen = (self.velocity/6)/(energyTransfered+0.0000000001)
# 		#energyAddedToSpin= energyTransfered - energyTakenByGen
# 		#self.velocity = np.sqrt(2*energyAddedToSpin/self.mass) + self.velocity

# 		return energyTransfered, self.velocity

# if __name__ == "__main__":
# 	tank= Tank(1,0.5,0.1,0.2,0.01)
# 	energyTransfered  = []
# 	velocities = []
# 	turbine = Turbine(0.015,0.00001)
# 	for i in range(0,10000000):
# 		energytransfered, velocity=(turbine.advance(*tank.advance()) )
# 		energyTransfered.append(energytransfered)
# 		velocities.append(velocity)

# 	plt.plot(np.linspace(0,100000,len(energyTransfered)),energyTransfered)
# 	plt.show()
# 	plt.plot(np.linspace(0,100000,len(velocities)),velocities)
# 	plt.show()



