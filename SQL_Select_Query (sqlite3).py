import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")

# Create a cursor
cursor = conn.cursor()

# Execute a SELECT query
cursor.execute("SELECT * FROM table")

# Fetch the results
rows = cursor.fetchall()

# Print the number of rows returned
print("Number of rows:", len(rows))

# Calculate the average value of the 'value' column
cursor.execute("SELECT AVG(value) FROM table")
average = cursor.fetchone()[0]
print("Average value:", average)

# Close the cursor and connection
cursor.close()
conn.close()
