import mysql.connector

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123',
    auth_plugin='mysql_native_password'
)

# Prepare a cursor
cursorObject = dataBase.cursor()

# Create a database 
cursorObject.execute("CREATE DATABASE KHLco")

# Commit the changes
# dataBase.commit()

# dataBase.close()

print("All Done!")