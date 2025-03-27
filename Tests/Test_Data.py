import sqlite3

# Connect to the database
con = sqlite3.connect("../Data/TeamData.sqlite")

# Query to list all tables
query = "SELECT name FROM sqlite_master WHERE type='table';"

# Execute the query and fetch the results
tables = con.execute(query).fetchall()

column_query = f"PRAGMA table_info('2025-03-12');"
columns = con.execute(column_query).fetchall()
print([col[1] for col in columns])
# Print the table names
query = f"SELECT * FROM '2025-03-13';"
rows = con.execute(query).fetchall()[0]
print(rows)

# Close the connection
con.close()
