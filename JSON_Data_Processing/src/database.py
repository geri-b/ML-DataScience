import pandas as pd
import pyodbc

#Read the CSV file into a Pandas DataFrame
df = pd.read_csv('mainInfo.csv', encoding='ISO-8859-1')
df.fillna(' ', inplace=True)

# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-8M2U7KJS;'
                      'Database=Business;'
                      'Trusted_Connection=yes;')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Business")

# Create the Main table
#ID,Name,Open,Stars,Review Count,Address,City,Neighborhoods,State,Longitude,Latitude,Type,Category
cursor.execute("""
CREATE TABLE Business (
    ID varchar(100) PRIMARY KEY,
    Name varchar(100),
    [Open] varchar(20),
    Stars decimal(2,1),
    [Review Count] int,
    Address varchar(300),
    City varchar(50),
    Neighborhoods varchar(100),
    State varchar(4),
    Longitude decimal(13,3),
    Latitude decimal(10,7),
    Type varchar(100),
    Category varchar(300)

)
""")

# Commit the changes
conn.commit()

# Loop over the rows in the DataFrame and insert the data into the table
for index, row in df.iterrows():
    cursor.execute("""
    INSERT INTO Business (ID,Name,Open,Stars,Review Count,Address,City,Neighborhoods,State,Longitude,Latitude,Type,Category)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (row['ID'], row['Name'], row['Open'], row['Stars'], row['Review Count'], row['Address'],
          row['City'], row['Neighborhoods'], row['State'], row['Longitude'], row['Latitude'], row['Type'], row['Category']))

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()


###HOURS TABLE###
# df = pd.read_csv('hours.csv', encoding='ISO-8859-1')
# df.fillna(' ', inplace=True)
#
# # Connect to the SQL Server database
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=LAPTOP-8M2U7KJS;'
#                       'Database=Business;'
#                       'Trusted_Connection=yes;')
#
# # Create a cursor object to execute SQL commands
# cursor = conn.cursor()
#
# cursor.execute("DROP TABLE IF EXISTS Hours")

# cursor.execute("""
# CREATE TABLE Hours (
#     ID varchar(100) PRIMARY KEY,
#     Name varchar(100),
#     [Monday Open] varchar(10),
#     [Monday Closed] varchar(10),
#     [Tuesday Open] varchar(10),
#     [Tuesday Closed] varchar(10),
#     [Wednesday Open] varchar(10),
#     [Wednesday Closed] varchar(10),
#     [Thursday Open] varchar(10),
#     [Thursday Closed] varchar(10),
#     [Friday Open] varchar(10),
#     [Friday Closed] varchar(10),
#     [Saturday Open] varchar(10),
#     [Saturday Closed] varchar(10),
#     [Sunday Open] varchar(10),
#     [Sunday Closed] varchar(10)
# )
# """)
#
# # Commit the changes
# conn.commit()
#
# # Loop over the rows in the DataFrame and insert the data into the table
# for index, row in df.iterrows():
#     cursor.execute("""
#     INSERT INTO Hours (ID,Name,[Monday Open],[Monday Closed],[Tuesday Open],[Tuesday Closed],
#     [Wednesday Open],[Wednesday Closed],[Thursday Open],[Thursday Closed],[Friday Open],[Friday Closed],
#     [Saturday Open],[Saturday Closed],[Sunday Open],[Sunday Closed])
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#     """, (row['ID'], row['Name'], row['Monday Open'], row['Monday Closed'], row['Tuesday Open'], row['Tuesday Closed'],
#           row['Wednesday Open'], row['Wednesday Closed'], row['Thursday Open'], row['Thursday Closed'], row['Friday Open'],
#           row['Friday Closed'], row['Saturday Open'], row['Saturday Closed'], row['Sunday Open'], row['Sunday Closed']))
#
# # Commit the changes
# conn.commit()
#
# # Close the cursor and connection
# cursor.close()
# conn.close()



###ATTRIBUTES TABLE###
# df = pd.read_csv('attributes.csv', encoding='ISO-8859-1')
# df.fillna(' ', inplace=True)
#
# # Connect to the SQL Server database
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=LAPTOP-8M2U7KJS;'
#                       'Database=Business;'
#                       'Trusted_Connection=yes;')
#
# # Create a cursor object to execute SQL commands
# cursor = conn.cursor()
#
# cursor.execute("DROP TABLE IF EXISTS Attributes")
#
# # Create the Main table
# #ID,Name,Happy Hour,Take-out,Drive-Thru,Caters,Noise Level,Takes Reservations,Delivery,Has TV,Outdoor Seating,Attire,Alcohol,Waiter Service,
# # Accepts Credit Cards,Good for Kids,Good For Groups,Good For Dancing,Price Range,Wi-Fi,Smoking,Coat Check
# cursor.execute("""
# CREATE TABLE Attributes (
#     ID varchar(100) PRIMARY KEY,
#     Name varchar(100),
#     [Happy Hour] varchar(10),
#     [Take-out] varchar(10),
#     [Drive-Thru] varchar(10),
#     [Caters] varchar(10),
#     [Noise Level] varchar(10),
#     [Takes Reservations] varchar(10),
#     [Delivery] varchar(10),
#     [Has TV] varchar(10),
#     [Outdoor Seating] varchar(10),
#     [Attire] varchar(100),
#     [Alcohol] varchar(10),
#     [Waiter Service] varchar(10),
#     [Accepts Credit Cards] varchar(10),
#     [Good for Kids] varchar(10),
#     [Good For Groups] varchar(10),
#     [Good For Dancing] varchar(10),
#     [Price Range] varchar(10),
#     [Wi-Fi] varchar(10),
#     [Smoking] varchar(10),
#     [Coat Check] varchar(10)
# )
# """)
#
# # Commit the changes
# conn.commit()
#
# # Loop over the rows in the DataFrame and insert the data into the table
# for index, row in df.iterrows():
#     cursor.execute("""
#     INSERT INTO Attributes (ID, Name, [Happy Hour], [Take-out], [Drive-Thru], [Caters], [Noise Level], [Takes Reservations], [Delivery], [Has TV],
#                             [Outdoor Seating], [Attire], [Alcohol], [Waiter Service], [Accepts Credit Cards], [Good for Kids], [Good For Groups],
#                             [Good For Dancing], [Price Range], [Wi-Fi], [Smoking], [Coat Check])
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#     """, (row['ID'], row['Name'], row['Happy Hour'], row['Take-out'], row['Drive-Thru'], row['Caters'],row['Noise Level'],row['Takes Reservations'],
#         row['Delivery'], row['Has TV'], row['Outdoor Seating'], row['Attire'], row['Alcohol'], row['Waiter Service'], row['Accepts Credit Cards'],
#         row['Good for Kids'], row['Good For Groups'], row['Good For Dancing'], row['Price Range'], row['Wi-Fi'], row['Smoking'],row['Coat Check']))
#
# # Commit the changes
# conn.commit()
#
# # Close the cursor and connection
# cursor.close()
# conn.close()

###AMBIENCE TABLE###

# df = pd.read_csv('ambience.csv', encoding='ISO-8859-1')
# df.fillna(' ', inplace=True)
#
# # Connect to the SQL Server database
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=LAPTOP-8M2U7KJS;'
#                       'Database=Business;'
#                       'Trusted_Connection=yes;')
#
# # Create a cursor object to execute SQL commands
# cursor = conn.cursor()
#
# cursor.execute("DROP TABLE IF EXISTS Ambience")
#
# # Create the Main table
# #ID,Name,romantic,intimate,classy,hipster,divey,touristy,trendy,upscale,casual
#
# cursor.execute("""
# CREATE TABLE Ambience (
#     ID varchar(100) PRIMARY KEY,
#     Name varchar(100),
#     romantic varchar(10),
#     intimate varchar(10),
#     classy varchar(10),
#     hipster varchar(10),
#     divey varchar(10),
#     touristy varchar(10),
#     trendy varchar(10),
#     upscale varchar(10),
#     casual varchar(10)
# )
# """)
#
# # Commit the changes
# conn.commit()
#
# # Loop over the rows in the DataFrame and insert the data into the table
# for index, row in df.iterrows():
#     cursor.execute("""
#     INSERT INTO Ambience (ID,Name,romantic,intimate,classy,hipster,divey,touristy,trendy,upscale,casual)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#     """, (row['ID'], row['Name'], row['romantic'], row['intimate'], row['classy'], row['hipster'],row['divey'],row['touristy'],
#         row['trendy'], row['upscale'], row['casual']))
#
# # Commit the changes
# conn.commit()
#
# # Close the cursor and connection
# cursor.close()
# conn.close()

###PARKING TABLE###

# df = pd.read_csv('parking.csv', encoding='ISO-8859-1')
# df.fillna(' ', inplace=True)
#
# # Connect to the SQL Server database
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=LAPTOP-8M2U7KJS;'
#                       'Database=Business;'
#                       'Trusted_Connection=yes;')
#
# # Create a cursor object to execute SQL commands
# cursor = conn.cursor()
#
# cursor.execute("DROP TABLE IF EXISTS Parking")
#
# # Create the Main table
# #ID,Name,garage,street,validated,lot,valet
#
# cursor.execute("""
# CREATE TABLE Parking (
#     ID varchar(100) PRIMARY KEY,
#     Name varchar(100),
#     garage varchar(10),
#     street varchar(10),
#     validated varchar(10),
#     lot varchar(10),
#     valet varchar(10),
# )
# """)
#
# # Commit the changes
# conn.commit()
#
# # Loop over the rows in the DataFrame and insert the data into the table
# for index, row in df.iterrows():
#     cursor.execute("""
#     INSERT INTO Parking (ID,Name,garage,street,validated,lot,valet)
#     VALUES (?, ?, ?, ?, ?, ?, ?)
#     """, (row['ID'], row['Name'], row['garage'], row['street'], row['validated'], row['lot'], row['valet']))
#
# # Commit the changes
# conn.commit()
#
# # Close the cursor and connection
# cursor.close()
# conn.close()

### Speciality Table ###

# df = pd.read_csv('speciality.csv', encoding='ISO-8859-1')
# df.fillna(' ', inplace=True)
#
# # Connect to the SQL Server database
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=LAPTOP-8M2U7KJS;'
#                       'Database=Business;'
#                       'Trusted_Connection=yes;')
#
# # Create a cursor object to execute SQL commands
# cursor = conn.cursor()
#
# cursor.execute("DROP TABLE IF EXISTS Speciality")
#
# # Create the Main table
# #ID,Name,dessert,latenight,lunch,dinner,brunch,breakfast
#
# cursor.execute("""
# CREATE TABLE Speciality (
#     ID varchar(100) PRIMARY KEY,
#     Name varchar(100),
#     Dessert varchar(10),
#     Latenight varchar(10),
#     Lunch varchar(10),
#     Dinner varchar(10),
#     Brunch varchar(10),
#     Breakfast varchar(10)
# )
# """)
#
# # Commit the changes
# conn.commit()
#
# # Loop over the rows in the DataFrame and insert the data into the table
# for index, row in df.iterrows():
#     cursor.execute("""
#     INSERT INTO Speciality (ID,Name,Dessert,Latenight,Lunch,Dinner,Brunch,Breakfast)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#     """, (row['ID'], row['Name'], row['dessert'], row['latenight'], row['lunch'], row['dinner'], row['brunch'], row['breakfast']))
#
# # Commit the changes
# conn.commit()
#
# # Close the cursor and connection
# cursor.close()
# conn.close()
