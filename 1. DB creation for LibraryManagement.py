import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

if db.is_connected():
    print("Database Connected")

# ### Create Database
cursor = db.cursor()
cursor.execute("CREATE DATABASE Library ")

print("Database Created Successful !!!")

