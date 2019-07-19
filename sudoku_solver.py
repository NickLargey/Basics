import random
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Board:

	def __init__(self):
		# self.width = width
		# self.height = height

		self.height = 9
		self.width = 9

		self.board = []
		for i in range(0, self.height):
			self.row = []
			for j in  range(0, self.width):
				self.row.append('')
			self.board.append(self.row)

		pp.pprint(self.board)

Board()