import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute SQL queries
cursor.execute("SELECT * FROM app_tesis_person")

# Fetch the query results
results = cursor.fetchall()

# Process the results as needed
for row in results:
    print(row)

# Close the database connection
conn.close()

# # Fetch table names from 'sqlite_master' table
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
# tables = cursor.fetchall()

# # Process the table names
# for table in tables:
#     table_name = table[0]
#     print(table_name)

# # Close the database connection
# conn.close()
