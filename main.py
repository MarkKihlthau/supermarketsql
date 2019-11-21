import mysql.connector
import sys

def newEmployee():
    print("Enter employee name: ")
    for line in sys.stdin:
        name = line
        break
    print("Enter employee position (Cashier, Bagger, Stocker, Manager): ")
    for line in sys.stdin:
        position = line
        break
    print("Enter ID of the employing store: ")
    for line in sys.stdin:
        works_at = line
        break
    print("Enter ID of manager: ")
    for line in sys.stdin:
        manager_id = line
        break
    print("Enter employee salary: ")
    for line in sys.stdin:
        salary = line
        break
    print("Enter employee phone number: ")
    for line in sys.stdin:
        phone = line
        break
    sql = "INSERT INTO employee (name, position, works_at, manager_id, salary, phone) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, position, works_at, manager_id, salary, phone)
    mycursor.execute(sql, val)

    mydb.commit()
    return;

mydb = mysql.connector.connect(user='root', password='Turing!1001',
                              host='localhost',
                              auth_plugin='mysql_native_password',
                              database='supermarketdb')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employee")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

print("Enter: ")
for line in sys.stdin:
    print(line)
    break

newEmployee()

