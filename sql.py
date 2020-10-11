import  mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="07882241718",database="marks")

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
# print(mydb)

# for x in mycursor:
#     print(x)

#################### not working(inserting values to table) ################
# sql1 = "INSERT INTO student (name,marks,mark2,mark3) VALUES('Aditya','34','64','45')"
# mycursor.execute("create table student(name varchar(20), marks int, mark2 int , mark3 int)")

#################### working(inserting values to table) ################
#mycursor.execute("insert into student values('aditya',56,23,54)")
#mycursor.execute("insert into student values('tejas',40,20,50)")

#mydb.commit()



#################### retriving data from mysql ######################
# try:
#     mycursor.execute("select *from student")
#     result=mycursor.fetchall()
#     for x in result:
#         print(x)

# except:
#     mydb.rollback()

# mydb.close()


##################### change data in table ########################
# sql = "update student set name='nitin' where name='tejas'"
# mycursor.execute(sql)
# mydb.commit()

# print(mycursor.rowcount,"record(s) affected")


################### deleting row ##############################
sql = "delete from student where name='hello'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")

