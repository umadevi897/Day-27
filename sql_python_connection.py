# importing mysql connector
# connecting database with connector
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="uma1111"
)

#print(mydb)

#creating the databases
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE d2022")





# checking all the databases
#mycursor.execute("SHOW DATABASES")
for x in mycursor :
    print(x)

   
   
   
   
   mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       password="uma1111",
       database="d2022",
   )
   mycursor = mydb.cursor()
   
   #creating table in databases
   mycursor.execute("CREATE TABLE customers (name VRCHAR(255),address VARCHAR(255))")
   show tables
   mycursor.execute("SHOW TABLES")
   for x in mycursor:
       print(x)
       
       
#insert in SQL
#sql = "INSERT INTO customers (name,address) VALUES (%s,%s)"
#val = ("John","Highway 21")
#mycursor.execute(sql, val)

#mydb.commit()
#print(mycursor.rowcount,"record inserted.")



#select in mysql
mycursor=mydb.cursor()
mycursor.execute("SELECT*FROM customers")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
    
#delete in sql

sql="DELETE FROM CUSTOMERS WHERE address='highway 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) deleted")


#drop
mycursor=mydb.mycursor()
sql="DROP TABLE CUSTOMERS"
mycursor.execute(sql)

#update table
sql="Update customers SET address ='canyou123' WHERE address = 'vailey345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s)affected")

#TRUNCATE

mycursor=mydb.cursor()
sql="TRUNCATE TABLE CUSTOMERS"
mycursor.execute(sql)


mycursor=mydb.cursor()
mycursor.execute("SELECT*from customers")
myresult=mycursor.fetchall()
for x in my result:
    print(x)