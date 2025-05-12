from colorama import Fore, Style
from utt import uttBoard
from MonteCarlo import MCTreeSearch
from human import Human
from copy import *
from randombot import RandomBot

print(Fore.RED + "Ultimate TicTacToe using Monte Carlo Tree Search")
print(Style.RESET_ALL)

# Initializing game board
board = uttBoard()
choice = ""

# Choose first player
while True:
    print("Please decide player 1")
    print("1. MCTS\n2. Human\n3. RandomBot")
    choice = int(input())
    if choice == 1:
        p1 = MCTreeSearch('X', time_for_move=0.1)
        break
    elif choice == 2:
        p1 = Human('X')
        break
    elif choice == 3:
        p1 = RandomBot('X')
        break
    else:
        print("Invalid choice!")


# Choose second player
while True:
    print("Please decide player 2")
    print("1. MCTS\n2. Human\n3. RandomBot")
    choice = int(input())
    if choice == 1:
        p2 = MCTreeSearch('O', time_for_move=0.1)
        break
    elif choice == 2:
        p2 = Human('O')
        break
    elif choice == 3:
        p2 = RandomBot('O')
        break
    else:
        print("Invalid choice!")

# Game loop
board.print()

prevMove = None

while True:
      validMoves=board.validMoves(prevMove)[0]
      while True:
            print("It is P1's turn now")
            move=p1.getMove(deepcopy(board),prevMove)
            if move not in validMoves:
                  print("Invalid Move!")
                  continue
            break
      board.playMove(move,'X')
      print("Move played by P1 : ", move)
      prevMove=move
      board.print()
      current_state=board.getState()
      if current_state[0]=='Won':
            print("P1 Won! ")
            break
      elif current_state[0] == 'Draw':
            print("Draw! ")
            break
      
      
      validMoves=board.validMoves(prevMove)[0]
      while True:
            print("It is P2's turn now")
            move=p2.getMove(deepcopy(board),prevMove)
            if move not in validMoves:
                  print("Invalid Move!")
                  continue
            break
      board.playMove(move,'O')
      print("Move played by P2 : ", move)
      prevMove=move
      board.print()
      current_state=board.getState()
      if current_state[0]=='Won':
            print("P2 Won! ")
            break
      elif current_state[0] == 'Draw':
            print("Draw! ")
            break
