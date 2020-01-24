# """ 
# Carlo Gonzalez
# CS 450 Neral Network Lab
#
# Winer selector
#
# Using a Neral network, this model will determine which of 
# 3 label any wine can be.
#
# Preconditions: 
# Having a wine_train.csv in file have
# 13 points and 3 Labels
# 
# Post Conditions:
# Print out of the accuracy of the Model 
# Return of the Model
# 
# 
#  """


import keras
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

def get_model():

    # load the dataset
    # Realising I didn't need Pandas and I could virtual in to the linux labs helped
    # I tried to use Google Collab (nice enviroment), Installed so many Neral network packages 
    # on my laptop. I was enjoying jupyter notebook, but none of that help me get a working model.

    dataset = loadtxt('wine_train.csv', delimiter=',')

    # split into input (X) and output (y) variables
 
    X = dataset[:,1:].astype(float)
    Y = dataset[:,0]

    # encode
    # Instead of giving name to our objective we encode them with numbers so there is less Bias
    # 

    encoder = LabelEncoder()
    encoder.fit(Y)
    encoded_Y = encoder.transform(Y)

    # convert integers to dummy variables (i.e. one hot encoded)
    dummy_y = np_utils.to_categorical(encoded_Y)

    # minmax scaler 
    # This help any numbers be relatable to each other.
    # So if one column uses parts per million and another uses
    # liter the liter with its larger number will not out weigh it.

    scaler = MinMaxScaler()
    scaler.fit(X)
    S = scaler.transform(X)

    
    # kfold = KFold(n_splits=10, shuffle=True)
    # Couldn't figure out where this goes in model,compile. Used to shuffle data. Wish I had time to learn more

    # evaluate the keras model
    #

    model = Sequential()
    model.add(Dense(8, input_dim=13, activation='relu'))
    model.add(Dense(1, activation='softmax'))
    model.add(Dense(2, activation='softmax'))
    model.add(Dense(3, activation='softmax'))

    # Complie the model
    # Needed the Categorical Crossentropy because each variable is a float and not a bool. the optimizer Adam had a lot of 
    # good thing

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(S, dummy_y, epochs=150, batch_size=200)

    # Printing the Model
    _, accuracy = model.evaluate(S, dummy_y)
    print('Accuracy: %.2f' % (accuracy*100))
    return model
