import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Library")
cursor = db.cursor()
sql = """ CREATE TABLE if not exists`library` (
                `Member_type` VARCHAR(40) NOT NULL ,
                `PRN_No` INT(11) NOT NULL AUTO_INCREMENT ,
                `Name` VARCHAR(45) NOT NULL ,
                `Address` VARCHAR(45) NOT NULL ,
                `Mobile` VARCHAR(45) NOT NULL ,
                `Bookid` VARCHAR(45) NOT NULL ,
                `Booktitle` VARCHAR(45) NOT NULL ,
                `DateBorrowed` VARCHAR(45) NOT NULL ,
                `DateDue` VARCHAR(45) NOT NULL ,
                        PRIMARY KEY (`PRN_No`));"""
cursor.execute(sql)
print("Table Created Successful !!!")

