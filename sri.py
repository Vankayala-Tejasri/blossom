#!C:\Users\tejasri\AppData\Local\Programs\Python\Python38\python
print("Content-Type: text/html")
print() 
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="registration")
cur=con.cursor()
cur.execute("create table teju(Username varchar(100),Email	 varchar(50),Password varchar(50),Confirm_Password varchar(50),Phone_Number varchar(10),Gender varchar(6))")
cur.close()
con.close()
print("table created")

                            
