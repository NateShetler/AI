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

"Pre: This function will accept in a list"
"Post: This function will print out the list to standard output"
def printList(printList):
     
    for i in printList:
        print()
        for j in i:
            print(j, end = ' ')
     
"Pre: This function will accept in a list and a file"
"Post: This function will write the list to the file"
def writeList(writeList, file):
     
    for i in writeList:
        file.write("\n")
        for j in i:
            file.write(str(j) + " ")
            
    file.write("\n")
            

"Pre: This function will accept the inital state and goal state. This will check if the 8 puzzle game is solvable or not"
"Post: This function returns true if it is solvable and false otherwise"
def isSolvable(initial, goal):
    
    
    "This will be used to calculate the number of inversions needed"
    inversionNum = 0
     
    for i in range(0, NUM_ROWS):
        for j in range(0, NUM_COLUMNS):
            " "
                 
"This is the game class and will go through and play the 8 puzzle game"    
class Game:
    
    "These are the initial and goals state variables"
    initialState = []
    goalState = []
    
    "These variables keep track of the current and previous states"
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
                print()
            else:
                print("\nIt seems that you have inputed a number outside of the desired range. Please only enter numbers from 0 - 8 ")
        
        print("The initial state is: ")
        printList(self.initialState)
        print()
        
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
                print()
            else:
                print("\nIt seems that you have inputed a number outside of the desired range. Please only enter numbers from 0 - 8 ")
        
        print("The Goal State is: ")
        printList(self.goalState)
        print("\n")
             
    "Mutator function for currentState"
    def updateCurrentState(self, newState):
        self.currentState = copy.deepcopy(newState)
        
    "Mutator function for previousState"
    def updatePreviousState(self, newState):
        self.previousState = copy.deepcopy(newState)
        
    "This function calculates the Hamming priority for the game"
    def getHamming(self, numMoves, currentState):
        
        "Used for keeping track of the Hamming priority"
        hammingPriority = 0
        
        "Go through the initial and goal states to see how many are out of position"
        for i in range(0, NUM_ROWS):
            for j in range(0, NUM_COLUMNS):
                if self.goalState[i][j] != 0:
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
    
    def startGame(self):
        "Create game object"
        game = Game()
        
        "This will be the file used to store the sequence"
        file = open("8puzzlelog.txt", "w")
        
        "Get initial and goal states"
        game.getInitial()
        game.getGoal()
        
        "Set currentState to initial state"
        game.updateCurrentState(game.initialState)
        
        "Set initial previous state to all 0's"
        game.updatePreviousState([[0,0,0],[0,0,0],[0,0,0]])
        
        "For keeping track of how many moves"
        numMoves = 0
        
        "Boolean that will be used to keep track if puzzle is solved"
        solved = False
        
        "Priority Queue for the states"
        pq = PriorityQueue()
        
        "Push on intial state and neighbors"
        pq.put((game.getHamming(numMoves, game.currentState), game.initialState))
            
        "Will keep track of how many enqueus"
        numEnqueues = 1
        
        "Keep track of number of neighbors for previous state"
        numPrevNeighbors = 0
        
        "To keep track of states"
        checked = []
        
        "Play until goal is reached"
        while solved == False:
            
            "Get the current list from the priority queue"
            currentStateList = pq.get()[1]
            
            "If state is not in the checked list, add it"
            if currentStateList not in checked: 
                checked.append(currentStateList)
                
            "Make the previous state the current state"
            game.updatePreviousState(game.currentState)
            
            numPrevNeighbors = game.howManyNeighbors()
            
            "Update the currentState"
            game.updateCurrentState(currentStateList)
            
            "Add one to the move counter"
            numMoves += 1
            
            "If the currentState is the goal state"
            if (game.currentState == game.goalState):
                
                "Set solved to true"
                solved = True
                
                print("The puzzle has been sovled!\n")
                
                "Write to file the solved puzzle"
                writeList(currentStateList, file)
                
                "Close write file"
                file.close()
                
                "Open readfile"
                readFile = open("8puzzlelog.txt", "r")
                
                "Output the sequence log"
                print("The sequence that it was solved in is: ")
                print(readFile.read())
                
                "Close read file"
                readFile.close()
                
                "Subtract 1 from numMoves because it counted initial state as a move at the beginning"
                numMoves -= 1
                
                print("It took " + str(numMoves) + " moves to solve the puzzle.")
                
                print(numEnqueues)
                
            else:
                
                "Write to file"
                writeList(currentStateList, file)
                
                "Update neighborList and put the new neighbors states on the queue"
                neighborList = game.neighborStates()
                numNeighbors = game.howManyNeighbors()
                
                """"
                "Remove old neighbors"
                for i in range(0, numPrevNeighbors):
                    if pq.empty() == False:
                        pq.get()
                """
                "If the state is not the previous state and hasn't been checked before then add to pq"
                for i in range(0, numNeighbors):
                    if game.previousState != neighborList[i] and neighborList[i] not in checked: 
                        pq.put((game.getHamming(numMoves, neighborList[i]), neighborList[i]))
                        numEnqueues += 1
                
            
def n_puzzle():
    
    game = Play()
    game.startGame()
    
        
    
        
        
        