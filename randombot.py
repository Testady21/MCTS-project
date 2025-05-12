import random

class RandomBot():
	
	def __init__(self, symbol):
		
		self.symbol = symbol

	def getMove(self, board, prevMove):

		nextMoves, nextSymbol = board.validMoves(prevMove)

		return random.choice(nextMoves)