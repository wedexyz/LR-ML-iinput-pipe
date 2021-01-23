import pandas as pd
from sklearn import linear_model
import pickle

# load the dataset into memory
training_dataset = pd.read_csv("area.csv")

# create a model that uses the linear regression algorithm 
# and train it with our dataset
regression_model = linear_model.LinearRegression()

# train the model
print ("Training model...")
regression_model.fit(training_dataset[['area']], training_dataset.price)

# serialize our model and save it in the file area_model.pickle
print ("Model trained. Saving model to area_model.pickle")
with open("area_model.pickle", "wb") as file:
    pickle.dump(regression_model, file)

print ("Model saved.")