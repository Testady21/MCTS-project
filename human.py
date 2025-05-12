'''
Human player class definition
'''

class Human():
	
	def __init__(self, symbol):
		
		self.symbol = symbol

	def getMove(self, board, prevMove):

		print("Enter the coordinates of the move you'd like to make, in the format \"[row] [column]\" - for example, \"2 2\" would correspond to the 2nd row, 2nd column.")
		
		try:
			move = list(map(int, input().split()))
			move = [move[0]-1,move[1]-1]
			return move
		except:
			return self.getMove(board)