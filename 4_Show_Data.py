# Choice 3 Show Data:-

import mysql.connector as m
c=m.connect(host='localhost',user='root',passwd='root',database='Project')
cursor=c.cursor()

print("1.Details of Qualified Students")
print("2.Details of Rejected Students")
x=int(input("Enter your Choice : "))


print("1.Show All Details")
print("2.Particular Student Details")
k=int(input("Enter your Choice : "))

if x==1:
    if k==1:
        cursor.execute('select * from Qualified_Student')
        d=cursor.fetchall()
        for i in d:
            print(i)


    elif k==2:
        r=int(input("Enter the Roll no whose Details need to be Displayed"))
        cursor.execute('''select * from Qualified_Student where rno ="%d"'''%(r))
        d=cursor.fetchall()
        for i in d:
            print(i)


    else:
        print(" Enter proper Choice ")


if x==2:
    if k==1:
        cursor.execute(" select * from Disqualified_Student ")
        d=cursor.fetchall()
        for i in d:
            print(i)

    elif k==2:
        r=int(input("Enter the Roll no whose Details need to be Displayed"))
        cursor.execute('''select * from Disqualified_Student where rno ="%d"'''%(r))

        d=cursor.fetchall()
        for i in d:
            print(i)


    else:
        print(" Enter proper Choice : ")


else:
    print(" Enter proper Choice : ")
