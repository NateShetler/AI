# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:59:46 2020

@author: adm_nds39
"""
import pandas as pd

def py_nb():
    
    "Boolean for the menu loop"
    endMenu = False
    
    "This will store the learned model"
    learnedModel = [] 

    "This stores the filename that the user enters"
    fileName = ""

    while endMenu == False:
        
        "Print the menu out"
        print()
        print("1. Learn a Naïve Bayesian classifier from categorical data.")
        print("2. Save a model.")
        print("3. Load a model and test its accuracy.")
        print("4. Apply a naïve Bayesian classifier to new cases interactively. The submenu for this item includes:")
        print("\t4.1 Enter a new case interactively.")
        print("\t4.2 Quit.")
        print("5. Quit.")
        
        "Get the user's choice"
        menuChoice = input()
        
        "Do something based on the user input"
        
        if menuChoice == "5":
            endMenu = True
        elif menuChoice == "1":
            fileName = input("Please enter the name of the csv file you would like to enter: ")
            
            "Get the csv data"
            csvData = getCSV(fileName)

        elif menuChoice == "2":

            file = open(str(fileName.split(".")[0]) + ".bin", "a")
            "-----------------------------------------------------------"
            file.write("File data")
            file.close()
        
        elif menuChoice == "3":
            "Do something"
            
        elif menuChoice == "4":
            "Do something"
            

"Pre: This function will accept in the name of a csv file"
"Post: This function will get the contents of the csv file and" 
"store them in a dataFrame. It will also return that dataFrame"           
def getCSV(file):
    
    "Create the dataFrame from the csv file"
    csvDataFrame = pd.read_csv(file)
    
    "Print out the contents of the csv file"
    print(csvDataFrame)
        
    "For formatting purposes"
    print()
    
    return csvDataFrame