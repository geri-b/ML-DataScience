import pandas as pd
import pyodbc

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('bigdata.csv', encoding='ISO-8859-1')

# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-8M2U7KJS;'
                      'Database=COMPANY_GerBak;'
                      'Trusted_Connection=yes;')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Presidents")

# Create the Presidents table
cursor.execute("""
CREATE TABLE Presidents (
    President varchar(100),
    Date varchar(100),
    Link varchar(max),
    Speech varchar(max)
)
""")

# Commit the changes
conn.commit()

# Loop over the rows in the DataFrame and insert the data into the table
for index, row in df.iterrows():
    cursor.execute("""
    INSERT INTO Presidents (President, Date, Link, Speech)
    VALUES (?, ?, ?, ?)
    """, (row['President'], row['Date'], row['Link'], row['Speech']))

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
