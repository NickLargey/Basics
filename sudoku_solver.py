import randint
import pprint


class Board:

	def __init__(self):
		self.width = width
		self.height = height

		self.board = []
		for i in range(0, height):
			row = []
			for j in  range(0, width):
				row.append(blank)
			self.board.append(row)