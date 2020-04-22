# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:45:59 2020

@author: Nathaniel Shetler
UANet ID: nds39
ID Number: 4015423
Class: Artificial Intelligence & Heuristic Programming
"""

from __future__ import print_function
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.callbacks import TensorBoard
import datetime
import os

"The directory for saving the models"
SAVE_DIR = os.path.join(os.getcwd(), 'logs\\fit\\')

"The number of classes will stay at 10 the whole time"
NUM_CLASSES = 10

def programMenu():
    
    "This will tell the loop when to stop
    quitLoop = False
    
    while quitLoop == False:
        
        print("Please choose a task: ")
        print("1. Run Keras 2010 baseline test")
        print("2. Run multiple tests on the Keras 2010 dataset")
        print("3. Run the new found solution")
        print("4. Quit")
        
        userChoice = input()
        
        if userChoice == "1":
            "Run the baseline test"
            
        elif userChoice == "2":
            "Run the tests"
            
        elif userChoice == "3":
            "Run the solution that I found"
        
        elif userChoice == "4":
            
            "The user wants to quit. Set quitLoop to True"
            quitLoop = True
        