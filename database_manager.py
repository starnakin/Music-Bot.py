import mysql.connector
import json_manager

def init():
    create_database(json_manager.get("./json/database.json", "name"))
    create_table("groups", "(groupe TEXT)")

def create_database(database_name):
    database_access=json_manager.curent_file("./json/database.json")

    mydb = mysql.connector.connect(
      host=database_access["host"],
      user=database_access["user"],
      password=database_access["password"]
    )
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE {}".format(database_name))


def create_table(table_name, keys):
    database_access=json_manager.curent_file("./json/database.json")

    mydb = mysql.connector.connect(
      host=database_access["host"],
      user=database_access["user"],
      password=database_access["password"],
      database=database_access["name"]
    )
    mycursor=mydb.cursor()

    mycursor.execute("CREATE TABLE {} {}".format(table_name, keys))

def add_group(group):
  database_access=json_manager.curent_file("./json/database.json")

  mydb = mysql.connector.connect(
    host=database_access["host"],
    user=database_access["user"],
    password=database_access["password"],
    database=database_access["name"]
  )
  mycursor=mydb.cursor()
  print(group.to_string())
  mycursor.execute("INSERT INTO groups (`groupe`) VALUES (%s)", (group.to_string()))
  mydb.commit()
