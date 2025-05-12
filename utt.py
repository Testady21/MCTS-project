#File implements the internal logic for the game ultimate tic-tac-toe

from colorama import Fore, Style

#class normalboard is the normal tictactoe board with move structure implemented
class normalBoard():
    #fundamental fields inside smallboard
    def __init__(self):

        self.board=[['_', '_', '_'],
					['_', '_', '_'],
					['_', '_', '_']]

    #get all valid moves inside small board, which are just spaces without any move  
    def validMoves(self):
        moves=[]
        if self.getState()[0] == 'Ongoing' :
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '_' :
                         moves.append([i,j])
        return moves
    
    #play symbol at move in board
    def playMove(self,move,symbol):
        self.board[move[0]][move[1]]=symbol
    
    #check if the game is won, if so by whom, or drawn, or ongoing
    def getState(self):

        #check if someone has won vertically
        for i in range(3):
            if self.board[0][i]==self.board[1][i] and self.board[1][i]==self.board[2][i] and self.board[2][i] != "_" :
                return 'Won',self.board[0][i]

        #check if someone has won horizontally
        for i in range(3):
            if self.board[i][0]==self.board[i][1] and self.board[i][1]==self.board[i][2] and self.board[i][2] != "_" :
                return 'Won',self.board[i][0]
            
        #check if someone has won diagonally
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != '_':
            return 'Won', self.board[0][0]
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != '_':
            return 'Won', self.board[0][2]

        #check for draw
        draw=True
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_' :
                    draw=False
                    break
            if(draw==False):
                break
        
        return 'Draw' if draw else 'Ongoing', '_'
    
    def print(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end=' ')
            print()

#Ultimate tic-tac-toe board
class uttBoard():
    def __init__(self):
        
        #fundamental fields inside uttBoard
        self.board = [[normalBoard(), normalBoard(), normalBoard()], 
					  [normalBoard(), normalBoard(), normalBoard()], 
					  [normalBoard(), normalBoard(), normalBoard()]]
        
        #for printing
        self.colorMap = {
			'X': Fore.RED,
			'O': Fore.BLUE,
			'|': Fore.GREEN,
			'-': Fore.GREEN,
			'_': Fore.YELLOW
		}
        
        self.opponentMap = {
			'X': 'O',
			'O': 'X'
		}

    #convert a move in small board to a move in big board
    def get_big_board_index(self,moves,cell_in_utt):
        for i in range(len(moves)):
            moves[i]=[3*cell_in_utt[0] + moves[i][0] , 3*cell_in_utt[1] + moves[i][1]]
        return moves
    
    def get_empty_cells(self):
        cells=[]
        for i in range(3):
            for j in range(3):
                cells = cells + self.get_big_board_index(self.board[i][j].validMoves() , [i,j])
        return cells
        
    def validMoves(self, previous_move):

        if previous_move == None:
            return self.get_empty_cells(), 'X'
        
        cell_in_utt = [previous_move[0]%3,previous_move[1]%3]

        if self.board[cell_in_utt[0]][cell_in_utt[1]].getState()[0] != 'Ongoing' :
            return (self.get_empty_cells(),self.opponentMap[self.board[previous_move[0]//3][previous_move[1]//3].board[cell_in_utt[0]][cell_in_utt[1]]])
        
        else:
            return (self.get_big_board_index(self.board[cell_in_utt[0]][cell_in_utt[1]].validMoves(),cell_in_utt),
                    self.opponentMap[self.board[previous_move[0]//3][previous_move[1]//3].board[cell_in_utt[0]][cell_in_utt[1]]])
        

    def playMove(self, move, symbol):
        self.board[move[0]//3][move[1]//3].playMove([move[0]%3, move[1]%3], symbol)

    def getState(self):
	# Creating a small Board to log results of big board
        smallVer = normalBoard()
        for i in range(3):
            for j in range(3):
                curState = self.board[i][j].getState()
                if curState[0] == 'Won':
                    smallVer.board[i][j] = curState[1]
        curState = smallVer.getState()
        if curState[0] == 'Won':
            return 'Won', curState[1]
            
        if len(self.get_empty_cells()) == 0:
            return 'Draw', '_'
        return 'Ongoing', '_'
        
    def print(self):
        for i in range(3):
            for k in range(3):
                for j in range(3):
                    for l in range(3):
                        print(self.colorMap[self.board[i][j].board[k][l]] + self.board[i][j].board[k][l], end=' ')
                    if j < 2:
                        print(self.colorMap['|'] + '|', end=' ')
                print()
            if i < 2:
                print(self.colorMap['-'] + 11*'--')
        print(Style.RESET_ALL)

