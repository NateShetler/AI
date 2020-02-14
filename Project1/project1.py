# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:09:00 2020

@author: adm_nds39
"""

"Contants for the Program"
NUM_ROWS = 3
NUM_COLUMNS = 3

class Game:
    
    "These are the initial and goals state variables"
    initialState = []
    goalState = []
    
    def getInitial(self):
        
        "This variable will be used to make sure the input is valid"
        validInitial = False 
        
        while validInitial == False:
            
            "Reset initialState and veriftyList if initalState already has something in it"
            if len(self.initialState) > 0:
                self.initialState.clear()
                verifyList = []
                
            
            print("You are going to enter the initial state consisting of 3 rows and 3 columns. Click enter to continue...")
            
            "Get the input"
            for i in range(0,NUM_ROWS):
                listString = input("Enter a 3 number row seperated by spaces: ")
                row = listString.split() 
                self.initialState.append(row)
            
            print(self.initialState)
        
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
                print("Your input was valid. Thank you.")
            
        print(self.initialState)
                
        
def printList():
    l = [[1,2, 3], [4,5,6], [7,8,9]]
    
    for i in l:
        print()
        for j in i:
            print(j, end = ' ')