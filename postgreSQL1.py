import psycopg2

conn = psycopg2.connect(   #database="CITY",
                            user="postgres",
                            password="07882241718",
                            host="localhost",
                            port=5432)
# print(conn)
# print("Connected to database")

cur = conn.cursor()
# cur.execute(''' create table sample (id int, salary float,
#                                      name varchar(25))''')
# print("Table SAMPLE created")

########## inserting values #########

# cur.execute('''insert into sample values(1,3434.66,'Aditya')''')
# cur.execute('''insert into sample values(2,4544.66,'Tejas')''')
# cur.execute('''insert into sample values(3,66666.66,'Safala')''')
# cur.execute('''insert into sample values(4,777.66,'Nitin')''')
# cur.execute('''insert into sample values(5,4343.66,'Chinmay')''')


####### updating values #######

# cur.execute("update sample set name='Anirudh' where id='1'")


####### retrieving values #######

# cur.execute("select id,salary,name from sample")
# rows = cur.fetchall()

# for row in rows:
#     print("ID= ",row[0])
#     print("Salary= ",row[1])
#     print("Name= ",row[2])


###### deleting row #######

# cur.execute("delete from sample where id=1")


# ####### creating database #######

# cur.execute("create database Mobile")


conn.commit()
conn.close()
print("Table SAMPLE updated")