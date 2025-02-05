# -*- coding: utf-8 -*-
"""SalesIceCream.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16z0sVaR9PG6KA-7h3NjFI5B2gF4TwcjZ

# **Temperature prediction on a place using the line of latitude.**

- Armojallas, Caleb Joshua
- II-BCSAD

Importing of Modules
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

"""Reading the .CSV file"""

data = pd.read_csv("datasets/IceCreamData.csv")

"""Descibe the Statistics of Data"""

data.describe()

"""Displaying of the first 5 rows"""

data.head(10)

"""Displaying Columns"""

data.columns

"""Getting the numbers of rows and columns of the datasets from the .CSV file"""

data.shape

"""Let's take the data from the column temperature and latitude"""

new_data = data[['Temperature', 'Revenue']]

new_data.sample(5)

"""* Store into X the 'temperature' as np.array
* Store into Y the 'latitutde' as np.array
* Viewing the shape of X
* Viewing the shape of Y
"""

X = np.array(new_data[['Temperature']])
Y = np.array(new_data[['Revenue']])

print(X.shape)
print(Y.shape)

"""Plotting a graph X vs Y"""

plt.scatter(X,Y,color="green")
plt.title('Temperature Vs Revenue')
plt.xlabel('Temperature')
plt.ylabel('Revenue')
plt.show()

"""Storing into X,Y the 'latitude','temperature' as np.array"""

X = np.array(new_data[['Temperature']])
Y = np.array(new_data[['Revenue']])

print(X.shape)
print(Y.shape)

"""Splitting the data into training and testing sets"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42, test_size=0.3)
print("Splitting data...")

"""Importing the LinearRegression class/module, instantiate it, and calling the fit() method

Train the algorithm

"""

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model = model.fit(X_train, Y_train)

"""Make Predictions on the test data"""

Y_pred = model.predict(X_test)

"""Comparing the actual output values"""

df = pd.DataFrame({'Actual Values': Y_test.flatten(), 'Predicted Values': Y_pred.flatten()})
df

while True:
  temp = input('Enter Temperature (or "quit" to quit): ')

  if temp == 'quit': break

  temp = float(temp)
  Sdata = model.predict([[temp]])
  print("The Predicted Revenue is : ", Sdata)

"""Comparing the actual and predicted values using bar graph"""

dfl = df.head(10)
dfl.plot(kind='bar', figsize=(5,5))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='blue')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.show()

"""Plot the prediction values"""

plt.scatter(X_test, Y_test, color='gray')
plt.plot(X_test, Y_pred, color='red', linewidth=2)
plt.show()

"""Getting the MAE, MSE, and RMSE; Measures of accuracy"""

from sklearn import metrics
print('Mean Absolute Error', metrics.mean_absolute_error(Y_test, Y_pred))
print('Mean Squared Error', metrics.mean_squared_error(Y_test, Y_pred))
print('Root Mean Squared Error', np.sqrt(metrics.mean_squared_error(Y_test, Y_pred)))
