print("***************************************************************************************************")

while True:
    print("WELCOME TO COLLEGE DATABASE MANAGEMENT SYSTEM !")

    print("1. Insert details of Qualified_Student")
    print("2. Insert details of Disqualified Student")
    print("3. Exit")
    print("\n")
    i = int(input("Enter your Choice : "))

    if i==1:
        # Choice 1 insert values for Qualified Students:-

        import mysql.connector as m
        c=m.connect(host='localhost',user='root',passwd='root',database='Project')
        cursor=c.cursor()

        rno=int(input('Enter SRN of Student : '))
        name=input('Enter the Name : ')
        age=int(input('Enter the Age : '))
        cls=input('Enter the Class : ')
        totalmarks=int(input('Enter the Total Marks : '))
        stream=input('Enter the Course : ')

        cursor.execute('''insert into Qualified_Student values("%d","%s","%d","%s","%d","%s") '''%(rno,name,age,cls,totalmarks,stream))

        c.commit()
        c.close()


    elif i == 2:

        # Choice 2 Insert values for Rejected Students:-

        import mysql.connector as m
        c=m.connect(host='localhost',user='root',passwd='root',database='Project')
        cursor=c.cursor()

        rno=int(input('Enter SRN of Student : '))
        name=input('Enter the Name : ')
        age=int(input('Enter the Age : '))
        cls=input('Enter the Class : ')
        totalmarks=int(input('Enter the Total Marks : '))
        stream=input('Enter the Course : ')

        cursor.execute('''insert into Disqualified_Student values("%d","%s","%d","%s","%d","%s")'''%(rno,name,age,cls,totalmarks,strem))

        c.commit()
        c.close()


    elif i == 3:

        print("Thank You for Using Student Database Mangement System ")
        break

    
    else:

        print("Wrong Choice !")
        print("\n\n")

print("***************************************************************************************************")

a = input("Type exit : ")
if a==exit:
    print("Okay")