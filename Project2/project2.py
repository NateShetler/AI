# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:59:46 2020

@author: adm_nds39
"""
import pandas as pd
import copy
from sklearn.metrics import confusion_matrix

"Dictionary that will store all of the bayesian models based on name"
bayList = {}

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
            
            "Bool for quitting loop"
            quitLoop = False
            
            "Loop until valid filename"
            while True and quitLoop == False:
                
                try:
                    
                    fileName = input("Please enter the name of a csv file consisting of headers and training examples (will search user folder for file) or 'Q'to quit: ")
                    
                    if fileName == 'Q':
                        quitLoop = True
                    else:
                
                        "Get the csv data"
                        csvData = getCSV(fileName)
                        break
                except IOError:
                    print("Invalid filename. Please try again.")
            
            if quitLoop == False:
                
                "Print the data from the file"
                print()
                print("The dataframe from the file that you entered is: ")
                print()
                print(csvData)
                
                input("Press any key to find the Bayesian Classifier (Model)...")
                print()
                
                "Get the model and print it"
                model = bayes_model(csvData)
                
                "Set learnedModel to what model is"
                learnedModel = copy.deepcopy(model)
                
                "Put the item in the dictionary"
                bayList.update({fileName : learnedModel})
                
                print("The Bayesian Model for the file that you entered is: ")
                print()
                
                "Print the model out"
                for i in range(0, len(model)):
                    if i == 0:
                        print(model[i])
                        print()
                        print("---------------------------------------------")
                        print()
                    elif i == 1:
                        for j in range(0, len(model[1])):
                            print(model[2][j], ":")
                            for k in model[i][j]:
                                print(k, model[i][j][k])
                            print()
                            print("---------------------------------------------")
                            print()
                    elif i == 2:
                        print(model[i])
                        print()
                        print("---------------------------------------------")
                        print()
                    else:
                        print(model[i])
                        print()
                    

        elif menuChoice == "2":
            
            if fileName != "":
                
                "Open correct file"
                file = open(str(fileName.split(".")[0]) + ".bin", "w")
                
                "Write to file and close it"
                file.write(str(learnedModel))
                file.close()
                
                input("The model has been saved (By default it is saved to the 'users' folder). Please hit any key to continue...")
            else:
                print("No model has been entered. Therefore, no model has been saved.")
                
        elif menuChoice == "3":
            
            "Call testData function"
            testData()
            
        elif menuChoice == "4":
            
            "Call interactiveTest function"
            interactiveTest()
            
        elif menuChoice == "4.1" or menuChoice == "4.2":
            
            "Give user a notice to enter 4 before entering 4.1 or 4.2"
            print("Please enter '4' before entering it's submenu items.")
            print()
            

"Pre: This function will accept in the name of a csv file"
"Post: This function will get the contents of the csv file and" 
"store them in a dataFrame. It will also return that dataFrame"           
def getCSV(file):
    
    "Create the dataFrame from the csv file"
    csvDataFrame = pd.read_csv(file)
    
    return csvDataFrame

"Pre: This function accepts no parameters"
"Post: This function will test the accuracy of a given Bayesian Classifier (Model)"
def testData():
   
    "Bool to quit loop"
    quitLoop = False
    
    "Loop until valid filename is given"
    while True and quitLoop == False:
        try:
            
            print()
            nameModelFile = input("Please enter the name of the model file that is saved (Ex: weather.bin) or 'Q' to quit: ")
            
            if nameModelFile == 'Q':
                quitLoop = True
                return
            
            "Open file"
            savedFile = open(nameModelFile, "r")
            
            break
        
        except IOError:
            print("Invalid filename, please try again.")
            
    "Convert to a list"
    listOfFile = []
    listOfFile = savedFile.read()
                 
    "Print the saved model"
    print("The content of the saved file is: ")
    print()
    print(listOfFile)
            
    savedFile.close()
    
    "Get name of the csv file corresponding to the filename entered"
    nameCSVFile = str(nameModelFile.split(".")[0]) + ".csv"
    
    "Get file data from the bayesian list"
    model = bayList[nameCSVFile]
    
    "Create two lists holding the target names and probabilities"
    nameTargets = []
    targetProbabilities = []
    
    "Fill nameTargets"
    for i in range(0, len(model[0])):
        nameTargets.append(list(model[0].keys())[i])
    
    "Loop until valid filename is given"
    while True:
        try:
            
            "Get test file"
            nameTestFile = input("Please enter the name of a testing file in csv format with no headers (Ex: weatherNoHeaders.csv): ")
           
            dfTest = pd.read_csv(nameTestFile, header=None)
            
            break
        except IOError:
            print("Invalid filename, please try again.")
    
    print()
    print("Contents of the test file: ")
    print(dfTest)
    
    "Lists for predictions and actual decisions"
    predictionList = []
    actualList = []

    "Fill targetProbabilities with 1 originally"
    for p in range(0, len(nameTargets)):
        targetProbabilities.append(1)
        
    for i in range(0, len(dfTest)):
        
        "Reset the probabilities"
        for p in range(0, len(nameTargets)):
            targetProbabilities[p] = 1
            
        for j in range(0, len(dfTest.columns)):
            
            if j == len(dfTest.columns) - 1:
                
                "Append actualList with actual answer"
                actualList.append(dfTest.iloc[i][j])
            else:
                
                "Multiply the probabilities"
                for k in range(0, len(targetProbabilities)):
                    targetProbabilities[k] *= model[1][j][(nameTargets[k], dfTest.iloc[i][j])]
                        
        "Sum variable"
        sumTargets = 0
        
        "Get sum of all answers"
        for j in range(0, len(targetProbabilities)):
            sumTargets += model[0][nameTargets[j]]
        
        "Finish probablities and then find guess"
        for j in range(0, len(targetProbabilities)):
            targetProbabilities[j] = targetProbabilities[j] * (model[0][nameTargets[j]] / sumTargets)
        
        "Sum for all probabilities"
        sumOfAll = 0
        
        "Sum of all targets"
        for j in range(0, len(targetProbabilities)):
            sumOfAll += targetProbabilities[j]
            
        "Finish probability calculation"
        for j in range(0, len(targetProbabilities)):
            targetProbabilities[j] = targetProbabilities[j] / sumOfAll
        
        "For the index of the highest probability"
        indexOfHighest = 0
        highestProbability = targetProbabilities[0]
        
        "Find position of highest probability in list"
        for j in range(0, len(targetProbabilities)):

            if targetProbabilities[j] > highestProbability:
                highestProbability = targetProbabilities[j]
                indexOfHighest = j
            
        "Append list with guess"
        predictionList.append(nameTargets[indexOfHighest])
    
    "Get the confusion matrix"
    confMatrix = confusion_matrix(actualList, predictionList)
    
    print()
    print("The confusion matrix for the data is: ")
    print(confMatrix)
    print()
    
    "Used to keep count of differences"
    count = 0
    
    "Figure out accuracy"
    for i in range(0, len(predictionList)):
        if predictionList[i] != actualList[i]:
            count += 1
            
    "Do accuracy calculation"
    accuracy = (len(predictionList) - count) / len(predictionList)
    
    print("The accuracy is: ", round(accuracy, 2) * 100, "%")


def interactiveTest():
    
    try:
        count = 0
        keepGoing = True
        bayesianFile = ""
        model = []
        
        "Test data frame created from user input"
        testDataFrame = pd.DataFrame({})
        
        while keepGoing == True:
            userResponse = input("4.1 Enter a new case interactively.\n4.2 Quit.\n\n")
            
            if userResponse == "4.1":
                
                if count == 0:
                
                    bayesianFile = input("Please enter the name of the file that the bayesian classifier was generated from (Ex. weather.csv): ")
            
                    "Get file data from the bayesian list"
                    model = bayList[str(bayesianFile)]
                    
                    print()
                    print("The bayesion model from this file was: ")
                    print(model)
                    print()
                    
                    "Create shape of main test dataframe"
                    for i in range(0, len(model[2])):
                        testDataFrame[model[2][i]] = pd.Series()
                        
            
                "Single data frame"
                singleFrame = pd.DataFrame({})
                
                "Create shape of individual dataframe"
                for i in range(0, len(model[2])):
                        singleFrame[model[2][i]] = pd.Series()
                
                "Dictionary for keeping track of items"
                dictionary = {}
                
                "This will get all of the items (columns) necessarry to create a single row"
                for i in range(0, len(model[2])):
                    item = input("Please enter a(n) " + str(model[2][i]) + ": ")
                    
                    "Add item to dictionary"
                    dictionary[model[2][i]] = item
                
                "Create the single frame from the dictionary"
                singleFrame = singleFrame.append(dictionary, ignore_index=True)
                
                try:
                    
                    "These will be used to get the probabilities"
                    probabilityYes = 1
                    probabilityNo = 1
                
                    "This block will do the calculations for applying the model"
                    for j in range(0, len(singleFrame.columns)):
                        
                        "These are because python interperets TRUE and FALSE as booleans"
                        if singleFrame.iloc[0][j] == "FALSE" or singleFrame.iloc[0][j] == "False":
                            probabilityYes *= model[1][j][('yes', False)]
                        elif singleFrame.iloc[0][j] == "TRUE" or singleFrame.iloc[0][j] == "True":
                            probabilityNo *= model[1][j][('no', True)]
                        else:
                            "Times the probability for the item"
                            probabilityYes *= model[1][j][('yes', singleFrame.iloc[0][j])]
                            probabilityNo *= model[1][j][('no', singleFrame.iloc[0][j])]
                
                
                    "Finish probabilities and then find guess"
                    probabilityYes = probabilityYes * (model[0]['yes'] / (model[0]['no'] + model[0]['yes']))
                    probabilityNo = probabilityNo * (model[0]['no'] / (model[0]['no'] + model[0]['yes']))
                    
                    "Sum of the two probabilities"
                    sumOfTwo = probabilityYes + probabilityNo
        
                    probabilityYes = probabilityYes / (sumOfTwo)
                    probabilityNo = probabilityNo / (sumOfTwo)
        
                    "Make the prediction"
                    if probabilityYes > probabilityNo:
                        print()
                        print("The bayesian classifier predicts: Yes")
                    else:
                        print()
                        print("The bayesian classifier predicts: No")
                    
                    "Put the single frame onto the main dataframe"
                    testDataFrame = testDataFrame.append(singleFrame, ignore_index = True)
                    
                    "Print the dataframe created by user"
                    print()
                    print("The test cases that you've entered so far: ")
                    print(testDataFrame)
                    
                    "Add one to count"
                    count += 1
                except LookupError:
                    print()
                    
                    "Print out the columns of the bayesian model"
                    for i in range(0, len(model)):
                        if i == 1:
                            for j in range(0, len(model[1])):
                                print(model[2][j], ":")
                                for k in model[i][j]:
                                    print(k, model[i][j][k])
                                print()
                    print()
                    print("The item that you entered wasn't formated correctly. Please refer to the portion of the bayesian model above and try again.")
                    print()
            else:
                keepGoing = False
        
    except LookupError:
        print()
        print("No classifier was found for the file that you entered.")
        
        
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
