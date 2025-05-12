import time
import numpy as np
import random
from copy import *

class Node():

    def __init__(self, state, starting_move, parent_node):
        self.simulations=0
        self.score=0
        self.parent=parent_node
        self.state=state
        self.children=[]
        self.starting_move = starting_move

    def propogate(self):
        next_moves,next_symbol = self.state.validMoves(self.starting_move)
        for move in next_moves:
            child_state = deepcopy(self.state)
            child_state.playMove(move,next_symbol)
            child=Node(child_state,move,self)
            self.children.append(child)
    
    def backPropogate(self,result):
        self.simulations+=1
        self.score+=result
        if self.parent!=None:
            self.parent.backPropogate(result)
    def getExplorationTerm(self):
        return np.sqrt(np.log(self.parent.simulations)/(self.simulations or 1))
    
    def getExploitationTerm(self):
        return self.score/(self.simulations or 1)

class MCTreeSearch():

    def __init__(self,symbol,time_for_move):
        self.C=np.sqrt(2)
        self.time_for_move=time_for_move
        self.symbol=symbol
        self.opponentMap={'O':'X','X':'O'}

    def simulate(self,board,previous_move):
        curr_state=board.getState()

        if curr_state[0] == "Ongoing" :
            nextMoves,nextSymbol = board.validMoves(previous_move)
            move=random.choice(nextMoves)
            board.playMove(move,nextSymbol)
            return self.simulate(board,move)
        else:
            if curr_state[0] == "Won" :
                if curr_state[1] == self.symbol:
                    return 1
                else:
                    return -1
            else:
                return 0
            
    def selection(self, currNode, symbol):
        curState = currNode.state.getState()
        if curState[0] != 'Ongoing': 
            return currNode
        
        if len(currNode.children) == 0: 
            return currNode

		# Selecting best child based on exploration Term and exploitation term
        if symbol == self.symbol:
            sortedChildren = sorted(currNode.children, key=lambda child: child.getExploitationTerm() + self.C*child.getExplorationTerm(), reverse=True)
        else:
            sortedChildren = sorted(currNode.children, key=lambda child: -child.getExploitationTerm() + self.C*child.getExplorationTerm(), reverse=True)
        
        return self.selection(sortedChildren[0], self.opponentMap[symbol])
    
    def getMove(self, board, previous_move):
        rootNode= Node(deepcopy(board),previous_move,None)

        start_time = time.time()
        while(time.time()-start_time<self.time_for_move):
            selectedNode=self.selection(rootNode,self.symbol)
            if selectedNode.simulations == 0 :
                result = self.simulate(deepcopy(selectedNode.state),selectedNode.starting_move)
                selectedNode.backPropogate(result)
            else:
                selectedNode.propogate()

        sortedChildren = sorted(rootNode.children, key=lambda child: child.getExploitationTerm(), reverse=True)

        return sortedChildren[0].starting_move
