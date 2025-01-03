import pandas as pd

# Read in csv file on vehicle data.
df = pd.read_csv('Car_Data.csv')

# Print basic info on dataset to see number of rows, column names and datatypes of each column.
print(df.info())

# Set the maximum number of columns to be displayed
pd.set_option('display.max_columns', None) 

# Pull first 25 records and assign variable name view.
raw_view = df.head(25)

# Print view to preview first 25 records.
print(raw_view)