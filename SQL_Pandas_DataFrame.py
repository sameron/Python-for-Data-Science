import pandas as pd

# Read the data into a Pandas DataFrame
df = pd.read_sql_table("table", "sqlite:///database.db")

# Print the number of rows and columns
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Calculate the average value of the 'value' column
average = df['value'].mean()
print("Average value:", average)
