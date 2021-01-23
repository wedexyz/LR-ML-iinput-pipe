import pickle

# Import our model
with open('area_model.pickle', "rb") as file:
    regression_model = pickle.load(file)

# Ask the user to enter an area and calculate 
# its price using the imported model
input_area = int(input("Enter area: "))
proped_price = regression_model.predict([[input_area]])
print ("Proped price:", round(proped_price[0], 2))