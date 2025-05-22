from abc import ABC, abstractmethod
 
pi = 3.141592653589793238462643

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

	@abstractmethod
	def volume(self):
		pass

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
		
	def perimeter(self):
		return 2 * 3.14 * self.radius

	def area(self):
		return 3.14 * self.radius ** 2
	
	def volume(self):
		return 4/3 * pi * self.radius**3
	

class Rectangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
	def perimeter(self):
		return 2 * (self.width + self.height)
	
	def area(self):
		return self.width * self.height
	
	def volume(self):
		return self.width**2 * self.height
	

class Square(Shape):
	def __init__(self, breadth):
		self.breadth = breadth

	def perimeter(self):
		return 4 * self.breadth

	def area(self):
		return self.breadth**2

	def volume(self):
		return self.breadth**3