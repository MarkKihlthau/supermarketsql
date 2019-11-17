import mysql.connector

mydb = mysql.connector.connect(user='root', password='Turing!1001',
                              host='localhost',
                              auth_plugin='mysql_native_password',
                              database='supermarketdb')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM supermarket")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

