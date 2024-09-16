# EXPERIMENT 3 - Python Data Analysis
# ____________________________________________________________
# Submitted by: John Gabriel Amboy
# Submitted on: September 16, 2024
# ____________________________________________________________

# PROBLEM 2

import pandas as pd

# loads the cars.csv and saves it to the variable cars
cars = pd.read_csv('cars.csv')

# part a. display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
cars_odd = cars.iloc[0:5,[1,3,5,7,9,11]]
print(cars_odd)

# part b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
cars_model = cars.loc[cars['Model']=='Mazda RX4']
print(cars_model)

# part c.
cars_cyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]
print(f"The number of cylinders of Camaro Z28 is: {cars_cyl}")

# part d.
cars_cyl_gear = cars.loc[(cars['Model']=='Mazda RX4 Wag')|
                (cars['Model']=='Ford Pantera L')|
                (cars['Model']=='Honda Civic'),
                ['Model','cyl','gear']]
print(cars_cyl_gear)
