import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("database.db")

# Read the data into a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM table", conn)

# Print the number of rows and columns
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Calculate the average value of the 'value' column
average = df['value'].mean()
print("Average value:", average)

# Close the connection
conn.close()
