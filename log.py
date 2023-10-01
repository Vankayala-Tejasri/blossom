#!C:\Users\tejasri\AppData\Local\Programs\Python\Python38\python
print("Content-Type: text/html")
print()
import cgi
reg=cgi.FieldStorage()
Username=reg.getvalue("Username")
Password=reg.getvalue("Password")
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="registration")
cur=con.cursor()
q1="SELECT * from teju"
cur.execute(q1)
res=cur.fetchall()

for i in res:
    if(Username==i[0] and Password==i[2]):
        print("<h1>Success</h1>")
        break
else:
    print("Invalid")
cur.close()
con.close()
