#create a database
import pymysql

mydb = pymysql.connect( host="localhost", user="root", password="Nish@562003")

c = mydb.cursor()
c.execute("CREATE DATABASE Bloodbank")
print("Database Created")