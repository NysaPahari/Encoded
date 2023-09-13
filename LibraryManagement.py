import mysql.connector
import os

db = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="",
                                database="Library"
                                )

if db.is_connected():
    print("Database Connected")

cursor = db.cursor()




def insert_data(db):
  memType = input("Select member type [Admin/Teacher/Student]= ")
  name = input("Enter Name: ")
  address = input("Enter Address: ")
  mobile = input("Enter mobile: " )
  bookid= input("Enter book id = ")
  booktitle = input("Enter Book title = ")
  borrow= input("Enter borrow date (Format YYYY-MM-DD) = ")
  due= input("Enter due date (Format YYYY-MM-DD) = ")
  
  sql = "INSERT INTO `library` (`Member_type`, `Name`, `Address`, `Mobile`, `Bookid`, `Booktitle`, `DateBorrowed`, `DateDue`) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s)"
  val =(memType,name,address, mobile, bookid, booktitle, borrow, due);
  cursor.execute(sql, val)
  db.commit()
  print("{} data Inserted".format(cursor.rowcount))


def show_data(db):
  sql = "SELECT * FROM library"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("There is not any data")
  else:
    for data in results:
      print(data)


def delete_data(db):
  show_data(db)
  PRN = input("Choose book ID/PRN No =  ")
  sql = """DELETE FROM `library` WHERE `library`.`PRN_No`=%s"""
  cursor.execute(sql, (PRN,))
  db.commit()
  print("{} data successfully deleted".format(cursor.rowcount))


def search_data(db):
  keyword = input("Keyword: ")
  sql = "SELECT * FROM library WHERE name LIKE %s OR address LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("There is not any data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== LIBRARY MANAGEMENT SYSTEM ===")
  print("1. Insert Data")
  print("2. Show Data")
  print("3. Delete Data")
  print("4. Search Data")
  print("0. GO Out")
  print("------------------")
  menu = input("Choose menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    delete_data(db)
  elif menu == "4":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Wrong input!")


if __name__ == "__main__":
  while(True):
    show_menu(db)





