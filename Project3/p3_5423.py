# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:45:59 2020

@author: Nathaniel Shetler
UANet ID: nds39
ID Number: 4015423
Class: Artificial Intelligence & Heuristic Programming
"""

from __future__ import print_function
import tensorflow.keras as keras
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.callbacks import TensorBoard
import os

"The following variables are constants and will stay the same the entire time"
"------------------------------------------------------------------------------"

"The directory for saving the models"
SAVE_DIR = os.path.join(os.getcwd(), 'logs\\')

"The number of classes will stay at 10 the whole time"
NUM_CLASSES = 10

"------------------------------------------------------------------------------"


"This function will run a keras example determined by the different variables passed in"
def runExample(numEpochs, batchSize, dataAugmentation, directoryName, modelName):
    
    "This function is based off of the cifar10_cnn.py example shown in class"
    "Baseline test for this examples was: (numEpochs=100, NUM_CLASSES=10, batchSize=32, "
    "dataAugmentation=True)"
    
    "Create the save directory for this specific test/example"
    saveDir = os.path.join(SAVE_DIR, directoryName)
    
    "Set num_predictions to 20"
    num_predictions = 20
    
    "Create tensorboard callback"
    tensorboard_callback = keras.callbacks.TensorBoard(log_dir=saveDir, histogram_freq=1, profile_batch = 10000000000)
    
    # The data, split between train and test sets:
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    print('x_train shape:', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')

    # Convert class vectors to binary class matrices.
    y_train = keras.utils.to_categorical(y_train, NUM_CLASSES)
    y_test = keras.utils.to_categorical(y_test, NUM_CLASSES)
    
    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding='same', input_shape=x_train.shape[1:]))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    
    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    
    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(NUM_CLASSES))
    model.add(Activation('softmax'))
    
    # initiate RMSprop optimizer
    opt = keras.optimizers.RMSprop(learning_rate=0.0001, decay=1e-6)
    
    # Let's train the model using RMSprop
    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
    
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    
    x_train /= 255
    x_test /= 255

    if not dataAugmentation:
        print('Not using data augmentation.')
        model.fit(x_train, y_train,
                  batch_size=batchSize,
                  epochs=numEpochs,
                  validation_data=(x_test, y_test),
                  shuffle=True)
    else:
        print('Using real-time data augmentation.')
        # This will do preprocessing and realtime data augmentation:
        datagen = ImageDataGenerator(
                featurewise_center=False,  # set input mean to 0 over the dataset
                samplewise_center=False,  # set each sample mean to 0
                featurewise_std_normalization=False,  # divide inputs by std of the dataset
                samplewise_std_normalization=False,  # divide each input by its std
                zca_whitening=False,  # apply ZCA whitening
                zca_epsilon=1e-06,  # epsilon for ZCA whitening
                rotation_range=0,  # randomly rotate images in the range (degrees, 0 to 180)
                # randomly shift images horizontally (fraction of total width)
                width_shift_range=0.1,
                # randomly shift images vertically (fraction of total height)
                height_shift_range=0.1,
                shear_range=0.,  # set range for random shear
                zoom_range=0.,  # set range for random zoom
                channel_shift_range=0.,  # set range for random channel shifts
                # set mode for filling points outside the input boundaries
                fill_mode='nearest',
                cval=0.,  # value used for fill_mode = "constant"
                horizontal_flip=True,  # randomly flip images
                vertical_flip=False,  # randomly flip images
                # set rescaling factor (applied before any other transformation)
                rescale=None,
                # set function that will be applied on each input
                preprocessing_function=None,
                # image data format, either "channels_first" or "channels_last"
                data_format=None,
                # fraction of images reserved for validation (strictly between 0 and 1)
                validation_split=0.0)

        # Compute quantities required for feature-wise normalization
        # (std, mean, and principal components if ZCA whitening is applied).
        datagen.fit(x_train)
        
        # Fit the model on the batches generated by datagen.flow().
        "Add the tensorboard callback"
        model.fit_generator(datagen.flow(x_train, y_train,
                                     batch_size=batchSize),
                        epochs=numEpochs,
                        validation_data=(x_test, y_test),
                        workers=4,
                        callbacks=[tensorboard_callback])
        
    # Save model and weights
    if not os.path.isdir(saveDir):
        os.makedirs(saveDir)
    model_path = os.path.join(saveDir, modelName)
    model.save(model_path)
    print('Saved trained model at %s ' % model_path)
    
    # Score trained model.
    scores = model.evaluate(x_test, y_test, verbose=1)
    print('Test loss:', scores[0])
    print('Test accuracy:', scores[1])
    print()


"This is the driver function for the program"
def programMenu():
    
    "This will tell the loop when to stop"
    quitLoop = False
    
    while quitLoop == False:
        
        print("Please choose a task: ")
        print("\t1.) Run Keras 2010 baseline test")
        print("\t2.) Run multiple tests")
        print("\t3.) Run the new found solution")
        print("\t4.) Quit")
        
        userChoice = input()
        
        if userChoice == "1":
            "Run the baseline test"
            runExample(5, 32, True, "baselineTest", "cifar10_cnn.h5")
            
        elif userChoice == "2":
            "Run the tests"
            
            "Change the number of epochs"
            runExample(150, 32, True, "150epochs_32batch_True", "cifar10.h5")
            runExample(200, 32, True, "200epochs_32batch_True", "cifar10.h5")
            runExample(250, 32, True, "250epochs_32batch_True", "cifar10.h5")
            
            "Change the batch size"
            runExample(100, 1, True, "100epochs_1batch_True", "cifar10.h5")
            runExample(100, 16, True, "100epochs_16batch_True", "cifar10.h5")
            runExample(100, 32, True, "100epochs_32batch_True", "cifar10.h5")
            
            "Turn data augmentation off for changing number of epochs"
            runExample(100, 32, False, "100epochs_32batch_False", "cifar10.h5")
            runExample(150, 32, False, "150epochs_32batch_False", "cifar10.h5")
            runExample(200, 32, False, "200epochs_32batch_False", "cifar10.h5")
            
        elif userChoice == "3":
            "Run the solution that I found"
        
        elif userChoice == "4":
            
            "The user wants to quit. Set quitLoop to True"
            quitLoop = True
        