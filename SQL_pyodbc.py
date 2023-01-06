import pyodbc

# Connect to the database
conn = pyodbc.connect("connection_string")

# Create a cursor
cursor = conn.cursor()

# Execute a SELECT query
cursor.execute("SELECT * FROM table")

# Fetch the results
rows = cursor.fetchall()

# Print the results
for row in rows:
  print(row)

# Close the cursor and connection
cursor.close()
conn.close()


# connect(): Connect to a SQL database using a connection string.
# cursor(): Create a cursor object to execute queries and fetch results.
# execute(): Execute a SQL query.
# fetchone(): Fetch the next row of the query results as a tuple.
# fetchmany(size=cursor.arraysize): Fetch the next size rows of the query results as a list of tuples.
# fetchall(): Fetch all remaining rows of the query results as a list of tuples.
# commit(): Commit any pending transactions to the database.
# rollback(): Roll back any pending transactions to the database.
# close(): Close the cursor and release any resources.