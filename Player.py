from random import randint

class Player:
	def __init__(self, char):
		self.char = char
		
		
	def throw_die(self):
		return randint(1, 6)
	