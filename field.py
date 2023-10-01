#!C:\Users\tejasri\AppData\Local\Programs\Python\Python38\python
print("Content-Type: text/html")
print() 
import cgi
reg=cgi.FieldStorage()
Username=reg.getvalue("Username")
Email=reg.getvalue("Email")
Password=reg.getvalue("Password")
Confirm_Password=reg.getvalue("Confirm_Password")
Phone_Number=reg.getvalue("Phone_Number")
Gender=reg.getvalue("Gender")

'''Username="teju"
Email="vtejasri.1016@gmail.com"
Password="tej"
Confirm_Password="tej"
Phone_Number="123456789"
Gender="female'''
import mysql.connector
con=mysql.connector.connect(host="localhost",password="",user="root",database="registration")
cursor=con.cursor()
cursor.execute("INSERT INTO teju(Username,Email,Password,Confirm_Password,Phone_Number,Gender) VALUES(%s,%s,%s,%s,%s,%s)",(Username,Email,Password,Confirm_Password,Phone_Number,Gender) )
con.commit()
cursor.close()
con.close()
print("<h1>succesfull entered</h1>")

