import sqlite3

# Connect to the database
con = sqlite3.connect("../Data/TeamData.sqlite")

# Query to list all tables
query = "SELECT name FROM sqlite_master WHERE type='table';"

# Execute the query and fetch the results
tables = con.execute(query).fetchall()

# Print the table names
for table in tables:
    print(table[0])

# Close the connection
con.close()
