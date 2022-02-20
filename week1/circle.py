class Circle:
	def __init__(self,radius):
		#history
		self.circles = []
		self.radius = radius
	def __add__(self, circle):
		bigger = Circle(self.radius + circle.radius)
		bigger.circles.extend([self, circle])
		return bigger
	def perimeter(self):
		return (22/7)*(self.radius*2)
	def area(self):
		return (22/7)*(self.radius**2)
"""c1 = Circle(3)
print(c1.radius)
c2 = Circle(5)
print(c2.radius)
c3 = c1 + c2

print(c3.radius)"""