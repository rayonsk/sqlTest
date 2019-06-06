import mysql.connector

#connect to database using a driver.Python needs a MySQL driver to access the MySQL database.
mydb = mysql.connector.connect(host="localhost",user="user1",passwd="password",database ="mydatabase")
#The cursor class. class cursor. Allows Python code to execute PostgreSQL command in a database session.
# Cursors are created by the connection.cursor() method: they are bound to the connection for the entire lifetime
# and all the commands are executed in the context of the database session wrapped by the connection.
mycursor = mydb.cursor()
#******************create tabele**************
# mycursor.execute("CREATE TABLE Customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)
#*****9*********inserting value **********************
sql = "INSERT INTO customers(name,address) VALUES (%s,%s)"
val = [('name2','address2'),
       ('name3','address3'),
       ('name4','address4'),
       ('name5','address5')]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "row inserted")
