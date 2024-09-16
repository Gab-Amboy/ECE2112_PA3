# EXPERIMENT 3 - Python Data Analysis
# ____________________________________________________________
# Submitted by: John Gabriel Amboy
# Submitted on: September 16, 2024
# ____________________________________________________________

# PROBLEM 1

import pandas as pd

# loads the cars.csv and saves it to the variable cars
cars = pd.read_csv('cars.csv')

# concatenates the first five rows and last five rows into cars using pd.concat
cars_rows = pd.concat([cars.head(), cars.tail()])
cars_rows
