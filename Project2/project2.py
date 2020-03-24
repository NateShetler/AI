# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:59:46 2020

@author: adm_nds39
"""
import pandas as pd
import copy

"This is the main function for the program"
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
            fileName = input("Please enter the name of a csv file consisting of headers and training examples (will search user folder for file): ")
            
            "Get the csv data"
            csvData = getCSV(fileName)
            
            "Print the data from the file"
            print(csvData)
            
            input("Press any key to find the Bayesian Classifier (Model)...")
            print()
            
            "Get the model and print it"
            model = bayes_model(csvData)
            
            "Set learnedModel to what model is"
            learnedModel = copy.deepcopy(model)
            
            print("The Bayesian Model for the file that you entered is: ")
            print()
            
            "Print the model out"
            for i in range(0, len(model)):
                if i == 0:
                    print("Number of yes/no answers:")
                    print()
                    print(model[i])
                    print()
                    print("---------------------------------------------")
                    print()
                elif i == 1:
                    print("Dependent features probabilities: ")
                    for j in range(0, len(model[1])):
                        print(model[2][j], ":")
                        for k in model[i][j]:
                            print(k, model[i][j][k])
                        print()
                    print("---------------------------------------------")
                    print()
                elif i == 2:
                    print("Names of dependent features:")
                    print()
                    print(model[i])
                    print("---------------------------------------------")
                    print()
                else:
                    print("Last column name: ")
                    print()
                    print(model[i])
                    print()
                    

        elif menuChoice == "2":
            
            "Open correct file"
            file = open(str(fileName.split(".")[0]) + ".bin", "a")
            
            "Write to file and close it"
            file.write(str(learnedModel))
            file.close()
            
            input("The model has been saved. Please hit any key to continue...")
        
        elif menuChoice == "3":
            nameModelFile = input("Please enter the name of the model file that is saved (Ex: weather.bin): ")
            
            "Open file and convert it to a list"
            savedFile = open(nameModelFile, "r")
            listOfFile = []
            listOfFile = savedFile.read()
            
            
            "Print the saved model"
            print("The content of the saved file is: ")
            print()
            print(listOfFile)
            
            savedFile.close()
            
            
            
        elif menuChoice == "4":
            "Do something"
            

"Pre: This function will accept in the name of a csv file"
"Post: This function will get the contents of the csv file and" 
"store them in a dataFrame. It will also return that dataFrame"           
def getCSV(file):
    
    "Create the dataFrame from the csv file"
    csvDataFrame = pd.read_csv(file)
    
    return csvDataFrame

def testData():
    "-----------------------------------------------------------"
    
    fileName = input("Please enter the name of a csv file consisting of headers and training examples (will search user folder for file): ")
            
    "Get the csv data"
    csvData = getCSV(fileName)
            
    "Print the data from the file"
    print(csvData)
            
    input("Press any key to find the Bayesian Classifier (Model)...")
    print()
            
    "Get the model and print it"
    model = bayes_model(csvData)
    
    print(model)
    "--------------------------------------------------------------"
    
    "Get test file"
    nameTestFile = input("Please enter the name of a testing file in csv format with no headers (Ex: weatherNoHeaders.csv): ")
           
    dfTest = pd.read_csv(nameTestFile, header=None)
    
    print(dfTest)
    
    predictionList = []
    actualList = []
    
    itemFeatures = []
    probabilityYes = 1
    probabilityNo = 1
    
    for i in range(0, len(dfTest)):
        "Reset the probability variables"
        probabilityYes = 1
        probabilityNo = 1
        
        for j in range(0, len(dfTest.columns)):
            
            if j == len(dfTest.columns) - 1:
                
                "Append actualList with actual answer"
                actualList.append(dfTest.iloc[i][j])
            else:
                
                itemFeatures.append(dfTest.iloc[i][j])
            
                "Times the probability for the item"
                probabilityYes *= model[1][j][('yes', dfTest.iloc[i][j])]
                probabilityNo *= model[1][j][('no', dfTest.iloc[i][j])]
                
                
        "Finish probabilities and then find guess"
        probabilityYes = probabilityYes * (model[0]['yes'] / (model[0]['no'] + model[0]['yes']))
        probabilityNo = probabilityNo * (model[0]['no'] / (model[0]['no'] + model[0]['yes']))
        
        "Sum of the two probabilities"
        sumOfTwo = probabilityYes + probabilityNo
        
        probabilityYes = probabilityYes / (sumOfTwo)
        probabilityNo = probabilityNo / (sumOfTwo)
        
        "Append list with guess"
        if probabilityYes > probabilityNo:
            predictionList.append('yes')
        else:
            predictionList.append('no')
            

    
    "Print out the lists"
    print()
    print(predictionList)
    print(actualList)
    
    "Used to keep count of differences"
    count = 0
    
    "Figure out accuracy"
    for i in range(0, len(predictionList)):
        if predictionList[i] != actualList[i]:
            count += 1
            
    "Do accuracy calculation"
    accuracy = (len(predictionList) - count) / len(predictionList)
    
    print("The accuracy is: ", round(accuracy, 2) * 100, "%")
     
     
"The following functions in this block of code were given to us by Dr. Chan "
"-----------------------------------------------------------------"
#represent frequency count of one feature as a DataFrame
def freq(x, opt='DataFrame'):
    """ x is a Series
        it returns a DataFrame (by default) indexed by unique values of x and
        their frequency counts
    """
    if opt != 'DataFrame':
        if opt == 'dict':
            return { i: x.value_counts()[i] for i in x.unique()}
        else:
            return (x.name, { i: x.value_counts()[i] for i in x.unique()})
    return pd.DataFrame([x.value_counts()[i] for i in x.unique()], index=x.unique(), columns=[x.name])

#How to create multi-index objects?
#Use  groupby()
def cond_p(df, c, d):
    """ compute p(d|c)
        represented as a dict
        df is a DataFrame with columns c and d
        c and d are column names
    """
    C = df.groupby(c).groups
    D = df.groupby(d).groups
    P_DC = { (i, j): (C[i] & D[j]).size / C[i].size
                 for i in C.keys() for j in D.keys()}
    
    return P_DC  #returns P(d|c) as a dict

def inverse_p(df, cond_list, decision_list):
    """ Build a list of dict of inverse probabilities
    """
    p_list = [cond_p(df, decision_list, i) for i in cond_list] #build a list of dicts
    return p_list

def bayes_model(df):
    cond_list = df.columns[:-1]  #get the list of condition attributes
    decision_list = df.columns[-1]  #get the decision attribute, assumed to be the last one
    d_prior = freq(df[decision_list], 'dict')
    c_list = inverse_p(df, cond_list, decision_list)
    return (d_prior, c_list, cond_list, decision_list)

"---------------------------------------------------------"