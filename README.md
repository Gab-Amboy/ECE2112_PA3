# Programming Assignment #3: PYTHON DATA ANALYSIS (PANDAS)

  <b> Name: </b> &nbsp; Amboy, John Gabriel D. 
  &emsp;&emsp;&emsp;&emsp;&emsp;
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
  <b> Date Submitted: </b> Sept. 16, 2024 <br>
  <b> Section: </b> 2ECE-A

## :book: I. Intended Learning Outcomes:
  1. To identify the codes and functions incorporated in the Pandas library
  2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

## ✒️ II. Documentation
  > [!Important]
  > For this programming assignment, download the following file and save to your default user folder: http://bit.ly/Cars_file
_______
### <b> Problem 1 </b>: Save your file as Surname_Pandas-P1.py

  Using knowledge obtained from the experiment and demonstrations: <br><br>
  &emsp;&emsp;&emsp; a. Load the corresponding .csv file into a data frame named cars using pandas <br>

  ```python
  import pandas as pd
  
  # loads the cars.csv and saves it to the variable cars
  cars = pd.read_csv('cars.csv')
  ```

  &emsp;&emsp;&emsp; b. Display the first five and last five rows of the resulting cars.

  ```python
  # concatenates the first five rows and last five rows into cars using pd.concat
  cars_rows = pd.concat([cars.head(), cars.tail()])
  cars_rows
  ```

#### Output for problem 1
![image](https://github.com/user-attachments/assets/c0c14432-bd5f-43e8-96f9-a42e83cbfb64)
_____
### <b> Problem 2 </b>: Save your file as Surname_Pandas-P2.py

  Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations. <br><br>
  &emsp;&emsp;&emsp; a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars. <br>

  ```python
  import pandas as pd

  # loads the cars.csv and saves it to the variable cars
  cars = pd.read_csv('cars.csv')
  
  # displays the first five rows with odd numbered columns using iloc
  cars_odd = cars.iloc[0:5,[1,3,5,7,9,11]]
  cars_odd 
  ```

  #### Output 
  ![image](https://github.com/user-attachments/assets/dd53ee50-530e-468f-abf6-666660653f9a)

  &emsp;&emsp;&emsp; b. Display the row that contains the ‘Model’ of ‘Mazda RX4’. <br>

  ```python
  cars_model = cars.loc[cars['Model']=='Mazda RX4']
  cars_model
  ```

  #### Output 
  ![image](https://github.com/user-attachments/assets/de790c16-e772-4295-96d0-343333de83e7)
  
  &emsp;&emsp;&emsp; c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have? <br>

  ```python
  cars_cyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]

  print(f"The number of cylinders of Camaro Z28 is: {cars_cyl}")
  ```

  #### Output 
  ![image](https://github.com/user-attachments/assets/7d4cb417-f384-4872-8ff6-a624167af232)
  
  &emsp;&emsp;&emsp; d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have. <br>

  ```python
  cars_cyl_gear = cars.loc[(cars['Model']=='Mazda RX4 Wag')|
                  (cars['Model']=='Ford Pantera L')|
                  (cars['Model']=='Honda Civic'),
                  ['Model','cyl','gear']]
  cars_cyl_gear
  ```

  #### Output 
  ![image](https://github.com/user-attachments/assets/e94987ac-808b-4175-8c4c-9c84083ed824)

## 🚀 III. Getting Started

### Dependencies
  * Any Operating System (OS) that can run Python/Jupyter Notebook
  * Integrated Development Environment (IDE)
  >[!Note]
  >It is highly suggested to use Jupyter Notebook for IPYNB files and VSCode for Py files.
  * Pandas Library

### Executing the program
  * Download the appropriate files / copy the code from this repository.
  * Use the necessary IDE for the appropriate language.
> [!Important]
> Make sure to import the pandas library before running the code block.
>  ``` import pandas as pd ```

## ⏳ IV. Version History
  * 0.1
    * Added Readme.md file
