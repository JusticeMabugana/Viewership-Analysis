# === METADATA ===

# This dataset offers insights into viewing habits across multiple platforms, detailing which shows customers watched, the duration of viewing, the dates of viewing, and whether the shows were watched live or on-demand.
#Date - Represents the calendar date when the viewing event occurred

#CustomerID - A unique, anonymized identifier assigned to each customer or user. It tracks user activity without revealing personal information.

#TotalTimeWatched - The total duration, in seconds, that the user spent watching the specific content during that session or event.

#Platform - Indicates the device or application platform used to stream the content.

#PlayEventType - Categorizes the type of content or how it was accessed.

#VideoTitle - The title of the video content watched by the user

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
 
# Loads the Excel file into a pandas DataFrame for analysis
df = pd.read_excel(data_path)

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

display(df)

df.head(5)

# create bar graph to show the number of unique customers who watched content on each platform
plt.bar(df['Platform'].unique(), df['Platform'].value_counts())
plt.title('Number of Unique Customers by Platform')
plt.xlabel('Platform')
plt.ylabel('Number of Unique Customers')
plt.show()

# create pie chart showing the percentage of total time watched by each platform
plt.pie(df['Platform'].value_counts(), labels=df['Platform'].unique(), autopct='%1.1f%%')
plt.title('Percentage of Total Time Watched by Platform')
plt.show()
