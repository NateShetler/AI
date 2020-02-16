# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:09:00 2020

@author: adm_nds39
"""

from queue import PriorityQueue
import copy

"Constants for the Program"
NUM_ROWS = 3
NUM_COLUMNS = 3

def printList(printList):
     
    for i in printList:
        print()
        for j in i:
            print(j, end = ' ')

"This class is may or may not be used"           
class currentState:
    
    currentStateList = []
    possibleStateList = []
    
    def __init__(self, currentList):
        
        "Initialize the currentStateList with list entered in parameter"
        for i in range(0, NUM_ROWS):
            for j in range(0, NUM_COLUMNS):
                self.currentStateList[i][j] = currentList[i][j]
                
    def possibleMoves(self):
        
        if len(self.currentStateList) < 3:
            print("\nThe current state is not valid")
        else:
            
            "Row and column variables"
            row = 0
            column = 0
            
            "Get the position of 0"
            for i in range(0, NUM_ROWS):
                for j in range(0, NUM_COLUMNS):
                    if self.currentStateList[i][j] == 0:
                        row = i
                        column = j
            
                    
"This is the game class and will go through and play the 8 puzzle game"    
class Game:
    
    "These are the initial and goals state variables"
    initialState = []
    goalState = []
    
    "This variable keeps track of the current state"
    previousState = []
    currentState = []
    
    "This function gets a valid initial state from the user"
    def getInitial(self):
        
        "This variable will be used to make sure the input is valid"
        validInitial = False 
        
        while validInitial == False:
            
            "Reset initialState and veriftyList if initalState already has something in it"
            if len(self.initialState) > 0:
                self.initialState.clear()
                verifyList = []
                
            print("\nPlease enter an initial state consisting of 3 rows and 3 columns.")
            
            "Get the input"
            for i in range(0,NUM_ROWS):
                listString = input("Enter a 3 number row with each number seperated by spaces: ")
                row = listString.split() 
                self.initialState.append(row)
        
            "Verify that the input is valid and convert to int"
            verifyList = []
            for i in range(0, NUM_ROWS):
                for j in range(0, NUM_COLUMNS):
                    try:
                        self.initialState[i][j] = int(self.initialState[i][j])
                        verifyList.append(self.initialState[i][j])
                    except:
                        print("Incorrect input. Please enter only numbers from 0 - 8")
            
            sorted_verify = sorted(verifyList)
            
            "Check to see if the list contains the numbers that it should"
            if sorted_verify == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                validInitial = True
                print("\nYour input was valid. Thank you!")
            else:
                print("\nIt seems that you have inputed a number outside of the desired range. Please only enter numbers from 0 - 8 ")
            
        printList(self.initialState)
        
    "This function gets a valid goal state from the user"
    def getGoal(self):
        
        "This variable will be used to make sure the input is valid"
        validGoal = False 
        
        while validGoal == False:
            
            "Reset initialState and veriftyList if initalState already has something in it"
            if len(self.goalState) > 0:
                self.goalState.clear()
                verifyList = []
                
            print("\nPlease enter a goal state consisting of 3 rows and 3 columns.")
            
            "Get the input"
            for i in range(0,NUM_ROWS):
                listString = input("Enter a 3 number row with each number seperated by spaces: ")
                row = listString.split() 
                self.goalState.append(row)
        
            "Verify that the input is valid and convert to int"
            verifyList = []
            for i in range(0, NUM_ROWS):
                for j in range(0, NUM_COLUMNS):
                    try:
                        self.goalState[i][j] = int(self.goalState[i][j])
                        verifyList.append(self.goalState[i][j])
                    except:
                        print("Incorrect input. Please enter only numbers from 0 - 8")
            
            sorted_verify = sorted(verifyList)
            
            "Check to see if the list contains the numbers that it should"
            if sorted_verify == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                validGoal = True
                print("\nYour input was valid. Thank you!")
            else:
                print("\nIt seems that you have inputed a number outside of the desired range. Please only enter numbers from 0 - 8 ")
            
        printList(self.goalState)
             
    "Mutator function for currentState"
    def updateCurrentState(self, newState):
        self.currentState = copy.deepcopy(newState)
        
    "This function calculates the Hamming priority for the game"
    def getHamming(self, numMoves, currentState):
        
        "Used for keeping track of the Hamming priority"
        hammingPriority = 0
        
        "Go through the initial and goal states to see how many are out of position"
        for i in range(0, NUM_ROWS):
            for j in range(0, NUM_COLUMNS):
                if currentState[i][j] != 0:
                    if self.goalState[i][j] != currentState[i][j]:
                        hammingPriority += 1
                    
        hammingPriority += numMoves
        
        return hammingPriority
    
    "Pre: This will take in the list (in form described by NUM_ROWS & NUM_COLUMNS) and then convert it to a hash value"
    "Post: This will return a hash value"
    def hashList(self, hashList):
        
        "List for converting the list passed in"
        convertList = []
        for i in range(0, NUM_ROWS):
            for j in range(0, NUM_COLUMNS):
                convertList.append(hashList[i][j])
                
        return(hash(tuple(convertList)))
    
    def howManyNeighbors(self):
        "Will return how many neighbor states there are"
        if self.currentState[1][1] == 0:
            return 4
        elif self.currentState[0][0] == 0 or self.currentState[0][2] == 0 or self.currentState[2][0] == 0 or self.currentState[2][2] == 0:
            return 2
        else:
            return 3
    
    "This function will return a list of possible states (neighbor states)"
    def neighborStates(self):
        
        "The neigboring state list that will be returned"
        neighborList = []
        
        if self.currentState[0][0] == 0:
            neighborList.append([[self.currentState[0][1],0,self.currentState[0][2]],[self.currentState[1][0],self.currentState[1][1],self.currentState[1][2]],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            neighborList.append([[self.currentState[1][0],self.currentState[0][1],self.currentState[0][2]],[0,self.currentState[1][1],self.currentState[1][2]],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            return neighborList
        elif self.currentState[0][1] == 0:
            neighborList.append([[0,self.currentState[0][0],self.currentState[0][2]], [self.currentState[1][0],self.currentState[1][1],self.currentState[1][2]],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            neighborList.append([[self.currentState[0][0],self.currentState[1][1],self.currentState[0][2]],[self.currentState[1][0],0,self.currentState[1][2]],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            neighborList.append([[self.currentState[0][0],self.currentState[0][2],0], [self.currentState[1][0],self.currentState[1][1],self.currentState[1][2]],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            return neighborList
        elif self.currentState[0][2] == 0:
            neighborList.append([[self.currentState[0][0],0,self.currentState[0][1]],[self.currentState[1][0],self.currentState[1][1],self.currentState[1][2]],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[1][2]],[self.currentState[1][0],self.currentState[1][1],0],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            return neighborList
        elif self.currentState[1][0] == 0:
            neighborList.append([[0,self.currentState[0][1],self.currentState[0][2]],[self.currentState[0][0],self.currentState[1][1],self.currentState[1][2]],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[self.currentState[1][1],0,self.currentState[1][2]],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[self.currentState[2][0],self.currentState[1][1],self.currentState[1][2]],[0,self.currentState[2][1],self.currentState[2][2]]])
            return neighborList
        elif self.currentState[1][1] == 0:
            neighborList.append([[self.currentState[0][0],0,self.currentState[0][2]],[self.currentState[1][0],self.currentState[0][1],self.currentState[1][2]],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[0,self.currentState[1][0],self.currentState[1][2]],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[self.currentState[1][0],self.currentState[1][2],0],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[self.currentState[1][0],self.currentState[2][1],self.currentState[1][2]],[self.currentState[2][0],0,self.currentState[2][2]]])
            return neighborList
        elif self.currentState[1][2] == 0:
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],0],[self.currentState[1][0],self.currentState[1][1],self.currentState[0][2]],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[self.currentState[1][0],0,self.currentState[1][1]],[self.currentState[2][0],self.currentState[2][1],self.currentState[2][2]]])
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[self.currentState[1][0],self.currentState[1][1],self.currentState[2][2]],[self.currentState[2][0],self.currentState[2][1],0]])
            return neighborList
        elif self.currentState[2][0] == 0:
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[0,self.currentState[1][1],self.currentState[1][2]],[self.currentState[1][0],self.currentState[2][1],self.currentState[2][2]]])
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[self.currentState[1][0],self.currentState[1][1],self.currentState[1][2]],[self.currentState[2][1],0,self.currentState[2][2]]])
            return neighborList
        elif self.currentState[2][1] == 0:
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[self.currentState[1][0],self.currentState[1][1],self.currentState[1][2]],[0,self.currentState[2][0],self.currentState[2][2]]])
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[self.currentState[1][0],0,self.currentState[1][2]],[self.currentState[2][0],self.currentState[1][1],self.currentState[2][2]]])
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[self.currentState[1][0],self.currentState[1][1],self.currentState[1][2]],[self.currentState[2][0],self.currentState[2][2],0]])
            return neighborList
        else:
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[self.currentState[1][0],self.currentState[1][1],self.currentState[1][2]],[self.currentState[2][0],0,self.currentState[2][1]]])
            neighborList.append([[self.currentState[0][0],self.currentState[0][1],self.currentState[0][2]],[self.currentState[1][0],self.currentState[1][1],0],[self.currentState[2][0],self.currentState[2][1],self.currentState[1][2]]])
            return neighborList
            
class Play:
    
    game = Game()
    
    def playGame(self):
        "Create game object"
        game = Game()
    
        "Get initial and goal states"
        game.getInitial()
        game.getGoal()
    
        "Boolean that will be used to keep track if puzzle is solved"
        solved = False
        
        "Priority Queue for the states"
        pq = PriorityQueue()
        
        "Push on intial state and neighbors"
        
        "Play until goal is reached"
        while solved == False:
            
            
def n_puzzle():
    
    "Create game object"
    game = Game()
    
    "Get initial and goal states"
    game.getInitial()
    game.getGoal()
    
    "Boolean that will be used to keep track if puzzle is solved"
    solved = False
    
        
    
        
        
        