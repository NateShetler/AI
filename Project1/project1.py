# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:09:00 2020

@author: Nathaniel Shetler
UANet ID: nds39
ID: 4015423
Class: Artificial Intelligence & Heuristic Programming
"""

from queue import PriorityQueue
import copy
import time

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

"This function calculates the Hamming priority for the game"
"Pre: It accepts in the number of moves (numMoves), and the currentState and goalState"
"Post: It will return the hamming priority"
def getHamming(numMoves, currentState, goalState):
        
    "Used for keeping track of the Hamming priority"
    hammingPriority = 0
        
    "Go through the initial and goal states to see how many are out of position"
    for i in range(0, NUM_ROWS):
        for j in range(0, NUM_COLUMNS):
            if goalState[i][j] != 0:
                if goalState[i][j] != currentState[i][j]:
                    hammingPriority += 1
                    
    hammingPriority += numMoves
    
    return hammingPriority

"Pre: This function will accept in a currentState and goalState"
"Post: The function will determine how close the states are to each other and return the number"
"(Similar to hamming but without keeping track of the number of moves)"
def closeToState(currentState, goalState):
    
    "Used for keeping track of the Hamming priority"
    howClose = 0
        
    "Go through the initial and goal states to see how many are out of position"
    for i in range(0, NUM_ROWS):
        for j in range(0, NUM_COLUMNS):
            if goalState[i][j] != 0:
                if goalState[i][j] != currentState[i][j]:
                    howClose += 1
    
    return howClose

"Pre: This function will accept in 2 states"
"Post: This function will determine if 2 states are neighbors (1 move away from each other)"
"and it will return true if they are and false if they are not"
def nextTo(state1, state2):
    
    "Will be used to determine if a neighbor is found"
    neighborFound = False
    
    "See if the currentState is a neighbor of the top value"
    if state1[0][0] == 0:
        if state2[0][1] == 0:
            neighborFound = True
        elif state2[1][1] == 0:
            neighborFound = True
    elif state1[0][1] == 0:
        if state2[0][0] == 0:
            neighborFound = True
        elif state2[0][2] == 0:
            neighborFound = True
        elif state2[1][1] == 0:
            neighborFound = True
    elif state1[0][2] == 0:
        if state2[0][1] == 0:
            neighborFound = True
        elif state2[1][2] == 0:
            neighborFound = True
    elif state1[1][0] == 0:
        if state2[0][0] == 0:
            neighborFound = True
        elif state2[1][1] == 0:
            neighborFound = True
        elif state2[2][0] == 0:
            neighborFound = True
    elif state1[1][1] == 0:
        if state2[0][1] == 0:
            neighborFound = True
        elif state2[1][0] == 0:
            neighborFound = True
        elif state2[1][2] == 0:
            neighborFound = True
        elif state2[2][1] == 0:
            neighborFound = True
    elif state1[1][2] == 0:
        if state2[0][2] == 0:
            neighborFound = True
        elif state2[1][1] == 0:
            neighborFound = True
        elif state2[2][2] == 0:
            neighborFound = True
    elif state1[2][0] == 0:
        if state2[1][0] == 0:
            neighborFound = True
        elif state2[2][1] == 0:
            neighborFound = True
    elif state1[2][1] == 0:
        if state2[1][1] == 0:
            neighborFound = True
        elif state2[2][0] == 0:
            neighborFound = True
        elif state2[2][2] == 0:
            neighborFound = True
    elif state1[2][2]:
        if state2[1][2] == 0:
            neighborFound = True
        elif state2[2][1] == 0:
            neighborFound = True
            
    return neighborFound
            
            
"Pre: This function will accept the inital state and goal state. This will check if the 8 puzzle game is solvable or not"
"Post: This function returns true if it is solvable and false otherwise"
def isSolvable(initial, goal):
    
    "Used for the 1D arrays"
    initial1D = []
    goal1D = []
    
    "Convert the 2d lists to 1d lists"
    for i in range(0, NUM_ROWS):
        for j in range(0, NUM_COLUMNS):
            initial1D.append(initial[i][j])
            goal1D.append(goal[i][j])
    
    "This will keep track of how many inversions there are"
    invCount = 0
    
    "This will go through the states and figure out the inversions"
    for i in range(0, len(goal1D) - 1):
        for j in range(i + 1, len(goal1D)):
            if initial1D.index(goal1D[i]) > initial1D.index(goal1D[j]):
                invCount += 1

    
    "This keeps track of the distance the states are from each other"
    distance = 0
    
    "Used to keep track of value in initial state"
    valueInInitial = 0
    
    "This will go through the initial and goal states and determine the distance they"
    "are from each other (similar to manhattan distance)"
    for i in range(0, NUM_ROWS):
        for j in range(0, NUM_COLUMNS):
            valueInInitial = initial[i][j]
            
            for k in range(0, NUM_ROWS):
                for l in range(0, NUM_COLUMNS):
                    if valueInInitial == goal[k][l] and goal[k][l] != 0:
                        distance += abs(i - k)
                        distance += abs(j - l)
                 
                
    "Return true if both the distance and inversion counts are odd or both even"
    "Return false if they are mix matched"
    if (distance % 2 == 0 and invCount % 2 == 0) or (distance % 2 != 0 and invCount % 2 != 0):
        return True
    else:
        return False
                 
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
        
        "Make sure the initial state is clear"
        self.initialState.clear()
        
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
            try:
                verifyList = []
                for i in range(0, NUM_ROWS):
                    for j in range(0, NUM_COLUMNS):
                        self.initialState[i][j] = int(self.initialState[i][j])
                        verifyList.append(self.initialState[i][j])
            except:
                print("\nIncorrect input.")
            
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
        
        "Make sure the goal state is clear"
        self.goalState.clear()
        
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
            try: 
                verifyList = []
                for i in range(0, NUM_ROWS):
                    for j in range(0, NUM_COLUMNS):
                        self.goalState[i][j] = int(self.goalState[i][j])
                        verifyList.append(self.goalState[i][j])
            except:
                print("\nIncorrect input.")
            
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
    
    "Will return how many neighbor states there are for the current state"
    def howManyNeighbors(self):
        
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
        
    "Pre This function will take in the stack of all checked states"
    "Post: This item will return a stack of the winning sequence"
    def winningSequence(self, stack):
            
        "For the top state/item on the stack/list"
        topItem = []
        
        "Stack/list for the winning sequence"
        winningSequence = []
        
        "Put the goalState on the stack/list"
        winningSequence.append(self.goalState)
        
        "Make currentState the goal state"
        currentState = copy.deepcopy(self.goalState)
        
        "Loop for going through the stack/list until a neighbor is found or end of stack is reached"
        while len(stack) > 0:
            
            "Get the next item off the stack/list"
            topItem = stack.pop()
            
            "Make sure the states are neighbors"
            if closeToState(currentState, topItem) == 1:              
                
                "If the states are next to each other (1 move away)"
                if nextTo(currentState, topItem) == True or nextTo(topItem, currentState) == True:
                    
                    "Write the state/item to the winningSequence and change to current state"
                    "to the topItem/state"
                    winningSequence.append(topItem)
                    currentState = copy.deepcopy(topItem)
        
        return winningSequence
            
                    
class Play:
    
    "This will play the 8 puzzle game informed using the hamming priority function"
    def startGame(self):
        "Create game object"
        game = Game()
        
        "This will be the file used to store the sequence"
        file = open("8puzzlelog.txt", "w")
        
        "This will be for making sure the puzzle is solvable"
        solvable = False
        
        "Loop until a valid puzzle is given"
        while solvable == False:
            
            "Get initial and goal states"
            game.getInitial()
            game.getGoal()
            
            solvable = isSolvable(game.initialState, game.goalState)
            
            if solvable == False:
                print("\nThe puzzle that you entered is not solvable! Please enter another puzzle.")
                
        
        "Set currentState to initial state"
        game.updateCurrentState(game.initialState)
        
        "Set initial previous state to all 0's"
        game.updatePreviousState([[0,0,0],[0,0,0],[0,0,0]])
        
        "For keeping track of how many moves/checks there are"
        numMoves = 0
        
        "Boolean that will be used to keep track if puzzle is solved"
        solved = False
        
        "This will be used to time the function"
        start = time.time()
        
        "Priority Queue for the states"
        pq = PriorityQueue()
        
        "Push on intial state and neighbors"
        pq.put((getHamming(numMoves, game.currentState, game.goalState), game.initialState))
        
        "To keep track of states"
        checked = []
        
        "This list that will function as a stack will keep track of the correct wining sequence"
        stack = []
        
        "Append the initial state to the stack"
        stack.append(game.initialState)
        
        "This stack/list will be used to keep track of the winning sequence"
        winningSequence = []
        
        "Play until goal is reached"
        while solved == False:
            
            "Get the current list from the priority queue"
            currentStateList = pq.get()[1]
            
            "If state is not in the checked list, add it"
            if currentStateList not in checked: 
                checked.append(currentStateList)
            
            "Make the previous state the current state"
            game.updatePreviousState(game.currentState)
            
            "Update the currentState"
            game.updateCurrentState(currentStateList)
            
            "Add one to the move counter"
            numMoves += 1
            
            "If the currentState is the goal state"
            if (game.currentState == game.goalState):
                
                "Set solved to true"
                solved = True
                
                "Output that the puzzle has been solved"
                print("The puzzle has been sovled!\n")
                
                "Fill the winningSequence stack/list"
                winningSequence = game.winningSequence(checked)
                
                "Reverse stack/list to have it output correctly"
                winningSequence.reverse()
                
                "Write it to the file"
                for i in range(0, len(winningSequence)):
                    writeList(winningSequence[i], file)
                
                "Close write file"
                file.close()
                
                """" 
                This was for if the user would like the sequence outputted
                "Open readfile"
                readFile = open("8puzzlelog.txt", "r")
                
                "Output the sequence log"
                print("The sequence that it was solved in is: ")
                print(readFile.read())
                
                "Close read file"
                readFile.close()
                """
                
                "Subtract 1 from numMoves because it counted initial state as a try at the beginning"
                numMoves -= 1
                
                print("It took ", str(numMoves), " state checks and ", str(len(winningSequence) - 1), " moves/steps to solve the puzzle.")
                
                "Output how long it took"
                end = time.time()
                
                "Set the time variable"
                timeElapsed = end - start
                
                print("\nIt took ", str(round(end - start, 2)), " to solve the puzzle informed.")
                
            else:
                
                "Update neighborList and put the new neighbors states on the queue"
                neighborList = game.neighborStates()
                numNeighbors = game.howManyNeighbors()
                
                "If the state is not the previous state and hasn't been checked before then add to pq"
                "The priority is assigned by the heuristic hamming distance function"
                for i in range(0, numNeighbors):
                    if game.previousState != neighborList[i] and neighborList[i] not in checked: 
                        pq.put((getHamming(numMoves, neighborList[i], game.goalState), neighborList[i]))
        
        return timeElapsed
    
    "This will play the 8 puzzle game uninformed"
    def startGameUninformed(self):
        "Create game object"
        game = Game()
        
        "This will be the file used to store the sequence"
        file = open("8puzzlelog.txt", "w")
        
        "This will be for making sure the puzzle is solvable"
        solvable = False
        
        "This will loop until a valid puzzle is given"
        while solvable == False:
            
            "Get initial and goal states"
            game.getInitial()
            game.getGoal()
            
            solvable = isSolvable(game.initialState, game.goalState)
            
            if solvable == False:
                print("\nThe puzzle that you entered is not solvable! Please enter another puzzle.")
        
        "Set currentState to initial state"
        game.updateCurrentState(game.initialState)
        
        "Set initial previous state to all 0's"
        game.updatePreviousState([[0,0,0],[0,0,0],[0,0,0]])
        
        "For keeping track of how many moves/checks there are"
        numMoves = 0
        
        "Boolean that will be used to keep track if puzzle is solved"
        solved = False
        
        "This will be used to time the function"
        start = time.time()
        
        "Priority Queue for the states"
        pq = PriorityQueue()
        
        "Push on intial state and neighbors"
        pq.put((1, game.initialState))
        
        "To keep track of states"
        checked = []
        
        "This list that will function as a stack will keep track of the correct wining sequence"
        stack = []
        
        "Append the initial state to the stack"
        stack.append(game.initialState)
        
        "This stack/list will be used to keep track of the winning sequence"
        winningSequence = []
        
        "Play until goal is reached"
        while solved == False:
            
            "Get the current list from the priority queue"
            currentStateList = pq.get()[1]
            
            "If state is not in the checked list, add it"
            if currentStateList not in checked: 
                checked.append(currentStateList)
            
            "Make the previous state the current state"
            game.updatePreviousState(game.currentState)
            
            "Update the currentState"
            game.updateCurrentState(currentStateList)
            
            "Add one to the move counter"
            numMoves += 1
            
            "If the currentState is the goal state"
            if (game.currentState == game.goalState):
                
                "Set solved to true"
                solved = True
                
                print("The puzzle has been sovled!\n")
                
                "Fill the winningSequence stack/list"
                winningSequence = game.winningSequence(checked)
                
                "Reverse stack/list to have it output correctly"
                winningSequence.reverse() 
                
                "Write it to the file"
                for i in range(0, len(winningSequence)):
                    writeList(winningSequence[i], file)
                
                "Close write file"
                file.close()
                
                """
                This is for if the user would like the sequence outputted
                "Open readfile"
                readFile = open("8puzzlelog.txt", "r")
                
                "Output the sequence log"
                print("The sequence that it was solved in is: ")
                print(readFile.read())
                
                "Close read file"
                readFile.close()
                """
                
                "Subtract 1 from numMoves because it counted initial state as a try at the beginning"
                numMoves -= 1
                
                print("It took ", str(numMoves), " state checks and ", str(len(winningSequence) - 1), " moves/steps to solve the puzzle.")
                    
                "Output how long it took"
                end = time.time()
                
                "Set the time variable"
                timeElapsed = end - start
                
                print("\nIt took ", str(round(end - start, 2)), " to solve the puzzle uninformed.")
                
            else:
                
                "Update neighborList and put the new neighbors states on the queue"
                neighborList = game.neighborStates()
                numNeighbors = game.howManyNeighbors()
                
                "If the state is not the previous state and hasn't been checked before then add to pq"
                "The priority is arbitrarily assigned based on i"
                for i in range(0, numNeighbors):
                    if game.previousState != neighborList[i] and neighborList[i] not in checked: 
                        pq.put((i + numMoves, neighborList[i]))
        
        return timeElapsed            
                    
def n_puzzle():
    
    "These will keep track of the time"
    timeInformed = 0
    timeUninformed = 0
    
    gameInformed = Play()
    gameUninformed = Play()
    
    print("\nThis first puzzle will be solved informed using the hamming priority.\n")
    timeInformed = gameInformed.startGame()
    print("-----------------------------------")
    print("\nThis second puzzle will be solved uninformed.\n")
    timeUninformed = gameUninformed.startGameUninformed()
    
    print("\nThe time it took to solve the puzzle informed was ", round(timeInformed, 2))
    print("VS.")
    print("The time it took to solve the puzzle uninformed was ", round(timeUninformed, 2))
    
        
    
        
        
        