# === METADATA ===

# This dataset offers insights into viewing habits across multiple platforms, detailing which shows customers watched, the duration of viewing, the dates of viewing, and whether the shows were watched live or on-demand.

# we are installing this dependancy so that we may load data from an excel file
%pip install openpyxl

# import library

# import pandas for data manipulation
import pandas as pd

# import matplotlib for data visualization
import matplotlib.pyplot as plt

# import numpy for numerical operations
import numpy as np

#data load to view the location of the file
data_path="/Workspace/Users/justice.mabugana@gmail.com/Viewership Analysis .xlsx"

# load data
df = pd.read_excel("/Workspace/Users/justice.mabugana@gmail.com/Viewership Analysis .xlsx")

# we want to display data
display(df)

# Displays a concise summary of the DataFrame, including the number of non-null entries and data types for each column
df.info()

# Displays the data types of each column in the DataFrame
df.dtypes

# Returns the column labels of the DataFrame
df.columns

# Returns a boolean Series indicating duplicate rows
df.duplicated

# Returns the number of duplicate rows in the DataFrame
df.duplicated().sum()

# Removes duplicate rows from the DataFrame in place
df.drop_duplicates(inplace=True)

# Returns the number of duplicate rows after removal
df.duplicated().sum()

# Displays the DataFrame
display(df)

# Returns the number of rows and columns in the DataFrame
df.shape

# Returns the first 5 rows of the DataFrame
df.head(5)

# Returns the last 5 rows of the DataFrame
df.tail(5)

# Returns the number of null values in each column of the DataFrame
df.isnull().sum()   

# allows us to rename columns and use the new names going foward
df.rename(columns={'DateID':'Date'}, inplace=True)

# allows us to display data
display(df)


