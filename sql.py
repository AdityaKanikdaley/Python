import  mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="07882241718",database="marks")

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
# print(mydb)

# for x in mycursor:
#     print(x)

# sql1 = "INSERT INTO student (name,marks,mark2,mark3) VALUES('Aditya','34','64','45')"

mycursor.execute("insert into student values('aditya',56,23,54)")
mydb.commit()
# mycursor.execute("create table student(name varchar(20), marks int, mark2 int , mark3 int)")
