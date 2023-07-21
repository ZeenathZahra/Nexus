import mysql.connector


database = mysql.connector.connect(host='localhost',user='root',passwd='Dragon')

cursor_object = database.cursor()

cursor_object.execute("CREATE DATABASE Nexus")

print("all done..")
