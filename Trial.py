# Here in this section, I will run my Project and will present our Project !
# So, Let's start...


#Update Database:-

import mysql.connector as m
c= m.connect(host='localhost', user='root', passwd='root')
cursor=c.cursor()
cursor.execute('use Project')
c.commit()
c.close()


tries = 0
tries_flag = ""
while tries_flag != "Close the program" :

        print("-----------------------------------------")
        print("|Enter 1 for Admin mode			|\n|Enter 2 for User mode			|")
        print("-----------------------------------------")
        Admin_user_mode = input("Enter your mode : ") 

        if Admin_user_mode == "1" :																			#Admin mode
            print("*****************************************\n|         Welcome to admin mode         |\n*****************************************")

            import getpass_ak
            Password = (getpass_ak.getpass('Please enter your password : '))
            
            while True:
                if Password == "HERO":

                    print("ACCESS GRANTED !")
                    print("\n\n")

                    while True:

                        print("\n")
                        print("*************************************************************************************************************************************************************************************************************")
                        print("\n")
                        print(' \t\t\t\t\t\t\t\t W E L C O M E    T O    C O L L E G E    D A T A B A S E    M A N A G E M E N T    S Y S T E M !')
                        print("\n")
                        print("*************************************************************************************************************************************************************************************************************")
                    

                        print("\n\n")
                        print('1.Add Details of Student\n')
                        print('2.Delete Details of Student\n')
                        print('3.Update Details of Student\n')
                        print('4.Exit\n\n')

                        ch=input('Enter your Choice : ')
                        print("\n")

                        if ch=="1":

                            print("-----------------------------------------------------------------------------------")
                            print("\n")
                            print('Welcome to our Add Section !')
                            print("\n")

                            print('1.Want to Add Details of Qualified Students ')
                            print('2.Want to Add Details of Rejected Students ')
                            print("\n")

                            k=input('Enter your Choice : ')
                            print("\n")

                            if k=="1":

                                print('You are now going to Add Details of Qualified Student...')
                                print("\n")

                                import mysql.connector as m
                                c=m.connect(host='localhost',user='root', passwd='root',database='Project')

                                cursor=c.cursor()

                                rno=int(input('Enter SRN of Student : '))
                                print("\n")
                                name=input('Enter the Name : ')
                                print("\n")
                                age=int(input('Enter the Age : '))
                                print("\n")
                                cls=input('Enter the Class : ')
                                print("\n")
                                totalmarks=int(input('Enter the Total Marks : '))
                                print("\n")
                                stream=input('Enter the Course : ')
                                print("\n")

                                cursor.execute('''insert into Qualified_student values("%d","%s","%d","%s","%d","%s")'''%(rno,name,age,cls,totalmarks,stream))

                                c.commit()
                                c.close()
                                print('Sucessfully Added!')
                                print("\n")


                            elif k=="2":

                                print('You are now going to Add Details of Rejected Student...')
                                print("\n")

                                import mysql.connector as m
                                c=m.connect(host='localhost',user='root',passwd='root',database='Project')
                                
                                cursor=c.cursor()

                                rno=int(input('Enter SRN of Student : '))
                                print("\n")
                                name=input('Enter the Name : ')
                                print("\n")
                                age=int(input('Enter the Age : '))
                                print("\n")
                                cls=input('Enter the Class : ')
                                print("\n")
                                totalmarks=int(input('Enter the Total Marks : '))
                                print("\n")
                                stream=input('Enter the Course : ')
                                print("\n")

                                cursor.execute('''insert into Disqualified_Student values("%d","%s","%d","%s","%d","%s") '''%(rno,name,age,cls,totalmarks,stream))
                                
                                c.commit()
                                c.close()
                                print('Sucessfully Added!')
                                print('\n')


                            else:

                                print('FAILED to Add')
                                print('Enter a proper Choice')
                                print('\n')


                        elif ch=="2":

                            print("-----------------------------------------------------------------------------------")
                            print("\n")
                            print('Welcome to our Delete Section !')
                            print("\n")
                            

                            print('1.Want to Delete from Qualified Student Table')
                            print('2.Want to Delete from Rejected Student Table')
                            print("\n")

                            k=input('Enter your Choice :')
                            print("\n")

                            if k=="1":

                                print('You are now going to Delete Details of Qualified Student...')
                                print("\n")

                                import mysql.connector as m
                                c=m.connect(host='localhost',user='root',passwd='root',database='Project')

                                cursor=c.cursor()
                                
                                print("Warning : If provided SRN input is not in Database then it will not delete anything !")
                                print("Provide Correct SRN !")
                                print("\n")

                                rno=int(input('Enter the Roll No. of the Student whose Details need to be Deleted : '))
                                cursor.execute('''select * from Qualified_Student where rno ="%d"'''%(rno))

                                d=cursor.fetchall()

                                for i in d:
                                    for j in i:
                                        if rno==j:
                                            cursor.execute('''delete from Qualified_Student where rno="%d"'''%(rno))
                                            print("Sucessfully Deleted!")
                                            print('\n')
                                            break
                                        
                                c.commit()


                            elif k=="2":

                                print('You are now going to Delete Details of Rejected Student...')
                                print("\n")

                                import mysql.connector as m
                                c=m.connect(host='localhost',user='root',passwd='root',database='Project')

                                cursor=c.cursor()

                                print("Warning : If provided SRN input is not in Database then it will not delete anything !")
                                print("Provide Correct SRN !")
                                print("\n")

                                rno=int(input('Enter the Roll No. of the Student whose Details need to be Deleted :'))
                                cursor.execute('''delete from Disqualified_Student where rno="%d"'''%(rno))

                                d=cursor.fetchall()

                                for i in d:
                                    for j in i:
                                        if rno==j:
                                            cursor.execute('''delete from Disqualified_Student where rno="%d"'''%(rno))
                                            print("Sucessfully Deleted!")
                                            print('\n')
                                            break

                                c.commit()


                            else:

                                print('FAILED to Delete! ')
                                print('Enter a proper Choice')
                                print('\n')




                        elif ch=="3":

                            print("-----------------------------------------------------------------------------------")
                            print("\n")
                            print('Welcome to our Update Section !')
                            print("\n")

                            import mysql.connector as m
                            c=m.connect(host='localhost',user='root',passwd='root',database='Project')

                            cursor=c.cursor()

                            print('1.Want to Update Details of Qualified Student')
                            print('2.Want to Update Details of Rejected Students')
                            print("\n")

                            t=input('Enter your Choice : ')
                            print("\n")

                            if t=="1":

                                print('You are now going to Update Details of Qualified Student...')
                                print("\n")

                                print('1. Update Name')
                                print('2. Update Age')
                                print('3. Update Class')
                                print('4. Update Total Marks')
                                print('5. Update Stream')
                                print('6. Update Roll Number')
                                print('7. Exit')
                                print("\n")

                                k=input('Enter your Choice : ')
                                print("\n")

                                if k=="1":

                                    rollno=int(input('Enter the Roll No. of the Data to be Modified : '))
                                    print("\n")

                                    name=input('Enter the Modified Name : ')
                                    print("\n")

                                    cursor.execute('''update Qualified_Student set name="%s" where rno="%d"'''%(name,rollno))
                                    c.commit()

                                    print('Sucessfully Updated!')
                                    print('\n')


                                elif k=="2":

                                    rollno=int(input('Enter the Roll No. of the Data to be Modified :'))
                                    print("\n")

                                    age=int(input('Enter the Modified Age :'))
                                    print("\n")

                                    cursor.execute('''Update Qualified_Student set age="%d" where rno="%d"'''%(age,rollno))
                                    c.commit()

                                    print('Sucessfully Updated!')
                                    print('\n')



                                elif k=="3":

                                    rollno=int(input('Enter the Roll No. of the Data to be Modified :'))
                                    print("\n")

                                    cls=input('Enter the Modified Class :')
                                    print("\n")

                                    cursor.execute('''update Qualified_Student set cls="%s" where rno="%d"'''%(cls,rollno))
                                    c.commit()

                                    print('Sucessfully Updated!')
                                    print('\n')



                                elif k=="4":

                                    rollno=int(input('Enter the Roll No. of the Data to be Modified :'))
                                    print("\n")

                                    tm=int(input('Enter the Modified Marks :'))
                                    print("\n")

                                    cursor.execute('''update Qualified_Student set totalmarks="%d" where rno="%d"'''%(tm,rollno))
                                    c.commit()

                                    print('Sucessfully Updated!')
                                    print('\n')



                                elif k=="5":

                                    rollno=int(input('Enter the Roll No. of the Data to be Modified :'))
                                    print("\n")

                                    str=input('Enter the Modified Class :')
                                    print("\n")

                                    cursor.execute('''update Qualified_Student set stream="%s" where rno="%d"'''%(str,rollno))
                                    c.commit()

                                    print('Sucessfully Updated!')
                                    print('\n')


                                elif k=="6":

                                    name=input('Enter Name of the Data to be Modified :')
                                    print("\n")

                                    rollno=int(input('Enter the Roll Number need to be Updated or Modified :'))
                                    print("\n")

                                    cursor.execute('''update Qualified_Student set rno="%d" where name="%s"'''%(rollno,name))
                                    c.commit()

                                    print('Sucessfully Updated!')
                                    print('\n')



                                else:

                                    print('Failed to Update!')
                                    print('Enter a proper Choice')
                                    print('\n')



                            if t=="2":

                                print('You are now going to Update Details of Rejected Student...')

                                print('1. Update Name')
                                print('2. Update Age')
                                print('3. Update Class')
                                print('4. Update Total Marks')
                                print('5. Update Roll Number')
                                print('6. Exit')
                                print("\n")

                                k=input('Enter your Choice :')
                                print("\n")

                                if k=="1":

                                    name=input('Enter the Modified Name :')
                                    print("\n")

                                    rollno=int(input('Enter the Roll No. of the Data to be Modified :'))
                                    print("\n")

                                    cursor.execute('''update Disqualified_Student set name="%s" where rno="%d"'''%(name,rollno))
                                    c.commit()

                                    print('Sucessfully Updated!')
                                    print('\n')


                                elif k=="2":

                                    age=int(input('Enter the Modified Age :'))
                                    print("\n")

                                    rollno=int(input('Enter the Roll No. of the Data to be Modified :'))
                                    print("\n")

                                    cursor.execute('''update Disqualified_Student set age="%d" where rno="%d"'''%(age,rollno))
                                    c.commit()

                                    print('Sucessfully Updated!')
                                    print('\n')



                                elif k=="3":

                                    cls=input('Enter the Modified Class:')
                                    print("\n")

                                    rollno=int(input('Enter the Roll No. of the Data to be Modified :'))
                                    print("\n")

                                    cursor.execute('''update Disqualified_Student set cls="%s" where rno="%d"'''%(cls,rollno))
                                    c.commit()

                                    print('Sucessfully Updated!')
                                    print('\n')



                                elif k=="4":

                                    tm=int(input('Enter the Modified Marks :'))
                                    print("\n")

                                    rollno=int(input('Enter the Roll No. of the Data to be Modified :'))
                                    print("\n")

                                    cursor.execute('''update Disqualified_Student set totalmarks="%d" where rno="%d"'''%(tm,rollno))
                                    c.commit()

                                    print('Sucessfully Updated!')
                                    print('\n')



                                elif k=="5":

                                    rollno=int(input('Enter the Roll number need to be Updated or Modified :'))
                                    name=input('Enter Name of the Data to be Modified :')

                                    cursor.execute('''update Disqualified_Student set rno="%d" where name="%s"'''%(rollno,name))
                                    c.commit()

                                    print('Sucessfully Updated!')
                                    print('\n')



                                else:
                                    print('Failed to Update')
                                    print('Enter a proper Choice')
                                    print('\n')

                        elif ch=="4":

                            a=input("Do you want to continue (y/n) : ")
                            print("\n")

                            if a=="y":
                                break
                            else :
                                while True:
                                    print("*************************************************************************************************************************************************************************************************************")
                                    print("\n")
                                    print('\t\t\t\t\t\t\t  T H A N K    Y O U    F O R    U S I N G    C O L L E G E    D A T A B A S E    M A N A G E M E N T    S Y S T E M !')
                                    print("\n")
                                    print("*************************************************************************************************************************************************************************************************************")
                                    a = input("Type exit : ")
                                    if a==exit:
                                        print("Okay")
                                    tries_flag = "Close the program"
                                    break
                        
                    
                elif Password != "1234" :
                    if tries < 2 :
                        Password = input("Password incorrect, please try again : ")
                        tries += 1
                    else :
                        print("Incorrect password, no more tries")
                        tries_flag = "Close the program"
                        break


        elif Admin_user_mode == "2" :																		#User mode
                print("****************************************\n|         Welcome to user mode         |\n****************************************")
                while True :
                    print("\n")
                    print("*************************************************************************************************************************************************************************************************************")
                    print("\n")
                    print(' \t\t\t\t\t\t\t\tW E L C O M E    T O    C O L L E G E    D A T A B A S E    M A N A G E M E N T    S Y S T E M !')
                    print("\n")
                    print("*************************************************************************************************************************************************************************************************************")
                
                    print("\n\n")
                    print('1.Display/Search Details of Qualified Student\n')
                    print('2.Display/Search Details of Rejected Student\n')
                    print('3.Performance of a Particular Class\n')
                    print("4.Exit")
                    print("\n")

                    ch=input('Enter your Choice : ')
                    print("\n")

                    if ch=="1":

                        print("-----------------------------------------------------------------------------------")
                        print("\n")
                        print('Welcome to Display/Search Section !')
                        print("\n")

                        import mysql.connector as m
                        c=m.connect(host='localhost',user='root',passwd='root',database='Project')

                        cursor=c.cursor()

                        print("1.Show All Details")
                        print("2.Particular Student Detail")
                        print("\n")

                        k=input("Enter your Choice : ")
                        print("\n")


                        if k=="1":

                            print('We are now going to Display All the Details of Qualified Students...')
                            print("\n")

                            cursor.execute('select * from Qualified_Student')
                            d=cursor.fetchall()

                            for i in d:
                                print(i)

                            print('\n')


                        elif k=="2":

                            print('We are now going to Display the Details of a Particular Student...')
                            print("\n")

                            r=int(input("Enter the Roll No. whose Details need to be Displayed :"))

                            cursor.execute('''select * from Qualified_Student where rno ="%d"'''%(r))
                            d=cursor.fetchall()

                            for i in d:
                                print(i)

                            print('\n')

                        else:

                            print('Failed to Display Details!')
                            print('Enter proper Choice')

                            print('\n')

                    elif ch=="2":

                        print("-----------------------------------------------------------------------------------")
                        print("\n")
                        print('Welcome to Display/Search Section !')
                        print("\n")

                        import mysql.connector as m
                        c=m.connect(host='localhost',user='root',passwd='root',database='Project')

                        cursor=c.cursor()

                        print("1.Show All Details")
                        print("2.Particular Student Detail")

                        k=input("Enter your Choice :")
                        print("\n")


                        if k=="1":

                            print('We are now going to Display All the Details of Rejected Students...')
                            print("\n")

                            cursor.execute('select * from Disqualified_Student')
                            d=cursor.fetchall()

                            for i in d:
                                print(i)

                            print('\n')


                        elif k=="2":

                            print('We are now going to Display the Details of a Particular Rejected Students...')
                            print("\n")

                            r=int(input("Enter the Roll No. whose Details need to be Displayed :"))
                            cursor.execute('''select * from Disqualified_Student where rno ="%d"'''%(r))
                            d=cursor.fetchall()

                            for i in d:
                                print(i)

                            print('\n')


                        else:

                            print('Failed to Display!')
                            print('Enter proper Choice')

                            print('\n')

                        
                    elif ch=="3":

                        print("-----------------------------------------------------------------------------------")
                        print("\n")
                        print('Welcome to the Performance/Analysis Section...')
                        print("\n")

                        print('1.Want the Performance of Qualified Students')
                        print('2.Want the Performance of Rejected Students')
                        print("\n")

                        g=input('Enter your Choice : ')
                        print("\n")

                        if g=="1":

                            print('We are now going to Taly the Data of Qualified Students...')
                            print("\n")

                            import mysql.connector as m
                            import numpy as np
                            import matplotlib.pyplot as plt

                            c=m.connect(host='localhost',user='root',passwd='root',database='Project')
                            cursor=c.cursor()

                            cls=input('Enter the Class of which the Performance is to Displayed :')
                            print("\n")

                            cursor.execute('''select totalmarks from Qualified_Student where cls="%s"'''%(cls))
                            m=cursor.fetchall()

                            x=np.array(m)
                            x1=[]
                            for i in x:
                                for j in i:
                                    x1.append(j)

                            cursor.execute('''select name from Qualified_Student where cls="%s"'''%(cls))

                            p=cursor.fetchall()
                            y=np.array(p)

                            y1=[]

                            for i in y:
                                for j in i:
                                    y1.append(j)


                            a=print(*y)

                            plt.bar(y1,x1,width=0.5,color='red')
                            plt.xlabel('Student Name')
                            plt.ylabel('Marks')

                            plt.title('Qualified Students',fontdict={'fontname':'Brush Script MT','fontsize':20})
                            plt.xticks(y1, a, rotation=90)

                            plt.show()

                            print('\n')


                        elif g=="2":

                            print('We are now going to Taly the Data of Rejected Students...')
                            print("\n")

                            import mysql.connector as m
                            import numpy as np
                            import matplotlib.pyplot as plt

                            c=m.connect(host='localhost',user='root',passwd='root',database='Project')
                            cursor=c.cursor()

                            cls=input('Enter the Class of which the Performance is to Displayed :')
                            print("\n")

                            cursor.execute('''select totalmarks from Disqualified_Student where cls="%s"'''%(cls))
                            m=cursor.fetchall()

                            x=np.array(m)
                            x1=[]

                            for i in x:
                                for j in i:
                                    x1.append(j)

                            cursor.execute('''select name from Disqualified_Student where cls="%s"'''%(cls))

                            p=cursor.fetchall()
                            y=np.array(p)

                            y1=[]
                            for i in y:
                                for j in i:
                                    y1.append(j)


                            a=print(*y)

                            plt.bar(y1,x1,width=0.5,color='blue')
                            plt.xlabel('Student Name')
                            plt.ylabel('Marks')

                            plt.title('Rejected Students')
                            plt.xticks(y1, a, rotation=90)

                            plt.show()

                            print('\n')


                        else:
                            print('Failed to Display the Performance')
                            print('Enter proper Choice')

                            print('\n')


                    elif ch=="4":

                            print("\n")
                            print("*************************************************************************************************************************************************************************************************************")
                            print("\n")
                            print(' T H A N K    Y O U    F O R    U S I N G    C O L L E G E    D A T A B A S E    M A N A G E M E N T    S Y S T E M')
                            print("\n")
                            print("*************************************************************************************************************************************************************************************************************")
                            break

        else :
                print("Please choice just 1 or 2")           

print("*************************************************************************************************************")