#Creating Database:-

print("***********************************************************************************************")
print("\n")
print("-----------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------")
print("\n")
print("                     Welcome for Database Creation :-")
print("\n")
print("-----------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------")
print("\n\n\n")

print("""
Here I grouped my Database mainly into two Categories named as Qualified Students and Rejected Students in a College Competitive Exam between Students.…

This Competitive Exam has held in Class A and Class B in which the criteria is that the Students have to get atleast 250 Marks out of 500 to Qualify this Exam…

So, Let's proceed...........
""")
print("\n\n\n")

print("Creating Database ...")
print("\n")

import mysql.connector as m
c = m.connect(host='localhost', user='root', passwd='root')
cursor=c.cursor()

cursor.execute('create database Project')
print("Database Project Created !")
print("\n")
cursor.execute('use Project')

cursor.execute('create table Qualified_Student(rno integer primary key, name varchar(20),age integer, cls varchar(4),totalmarks integer, stream varchar(50))')
print("Qualified Student Table created !")
print("\n")

cursor.execute('create table Disqualified_Student(rno integer primary key, name varchar(20),age integer, cls varchar(4),totalmarks integer, stream varchar(50))')
print("Disqualified Student Table created !")
print("\n")

c.commit()
c.close()
print("Done !")

print("***********************************************************************************************")

a = input("Type exit : ")
if a==exit:
    print("Okay")