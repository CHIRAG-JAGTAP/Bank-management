#CODE TO CONNECT MYSQL WITH PYTHON:
import mysql.connector as cj
a=input('ENTER PASSWORD OF MYSQL SERVER')
c=cj.connect(host="localhost",user="root",passwd=a,database="BANK_MANAGEMENT")
if c.is_connected():
    print('CONNECTED SUCCESSFULLY')
else:
    print("NOT CONNECTED")
print()
#CRUCIAL PART OF THE ASSIGNMENT:
print('____________________________________________________________________________________________________')
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('''                                          ✨ARNOLDIAN BANK OF INDORE PVT.LTD✨                                           ''')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('_____________________________________________________________________________________________________')
print()
print("""                                                        🎟🦅'WELCOME TO THE PORTAL!'🦅🎟
***ENTER YOUR CHOICE***
'1' TO ACCESS ALL THE RECORDS OF 'BANK_MANAGEMENT'.
'2' TO DISPLAY THE INFORMATION OF A PERSON.
'3' TO ADD INFORMATION OF A PERSON IN DATABASE.
'4' TO UPDATE INFORMATION OF EXISTING PERSON OF 'BANK_MANAGEMENT'.
'5' TO DELETE A RECORD FROM 'BANK_MANAGEMENT'.
'6' TO EXIT FROM BANKING DATABASE PORTAL
""")
# ASSIGNING FUNCTIONS "FOR USER INTERFACE".
def f1():
    print("""***ENTER YOUR CHOICE***
'1' TO ACCESS INFORMATION OF 'BANKING_STAFF'.
'2' TO ACCESS INFORMATION OF 'WORKERS_STAFF'.
'3' TO ACCESS INFORMATION OF 'PEOPLES ACCOUNT'.
""")
def f2():
    print("""***ENTER YOUR CHOICE***
'1' TO ADD RECORD IN 'BANKING_STAFF'.
'2' TO ADD RECORD IN 'WORKERS_STAFF'.
'3' TO ADD RECORD IN 'PEOPLES ACCOUNT'.
""")
def f3():
    print("""***ENTER YOUR CHOICE***
'1' TO UPDATE RECORD OF A PERSON FROM 'BANKING STAFF'.
'2' TO UPDATE RECORD OF A PERSON FROM 'WORKERS STAFF'.
'3' TO UPDATE RECORD OF A PERSON FROM 'PEOPLES ACCOUNT'
""")
def f4():
    print("""***ENTER YOUR CHOICE***
'1' TO DELETE A RECORD FROM 'BANK_MANAGEMENT'.
'2' TO DELETE A RECORD FROM 'WORKERS_STAFF'.
'3' TO DELETE A RECORD FROM 'PEOPLES ACCOUNT'.
""")
# FUNCTION FOR ACCESSING ALL THE TABLES AND RECORDS FROM DATABASE "BANK_MANAGEMENT".
def dsply_all():
    s="select * from banking"
    z=c.cursor()
    z.execute(s)
    b=z.fetchall()
    for x in b:
        print("   ID   ,   EMP_NAME   ,   DOJ   ,   DOB   ,   POST   ,   SALARY   ,   MOB_NO   ,   ADDRESS   ")
        print(x)
        print()
        q="select * from workers_staff"
        z1=c.cursor()
        z1.execute(q)
        r=z1.fetchall()
    for y in r:
        print("   S_NO   ,   WNAME   ,   MOB_NO   ,   SALARY   ")
        print(y)
        print()
        l="select * from clients"
        z2=c.cursor()
        z2.execute(l)
        s=z2.fetchall()
    for p in s:
        print("   S_NO   ,   NAME   ,   MOB_NO   ,   CURR_AMMOUNT   ,   AMT_WITHDRAWED   ,   ONLINE_BENEFITS   ")
        print(p)
        print()
# FUNCTION FOR ACCESSING PARTICULAR RECORD.
def dp():
    i=int(input('Enter ID number'))
    s1="select * from banking where ID=%s"
    d=(i,)
    cl=c.cursor()
    cl.execute(s1,d)
    b3=cl.fetchone()
    print("   ID   ,   EMP_NAME   ,   DOJ   ,   DOB   ,   POST   ,   SALARY   ,   MOB_NO   ,   ADDRESS   ")
    print(b3)
    print()
def dp1():
    i1=int(input("Enter S_NO"))
    s2="select * from workers_staff where S_NO=%s"
    d2=(i1,)
    cld=c.cursor()
    cld.execute(s2,d2)
    b4=cld.fetchone()
    print("   S_NO   ,   WNAME   ,   MOB_NO   ,   SALARY   ")
    print(b4)
    print()
def dp3():
    i2=int(input("Enter S_NO"))
    s3="select * from clients where S_NO=%s"
    d1=(i2,)
    cldd=c.cursor()
    cldd.execute(s3,d1)
    b5=cldd.fetchone()
    print("   S_NO   ,   NAME   ,   MOB_NO   ,   CURR_AMMOUNT   ,   AMT_WITHDRAWED   ,   ONLINE_BENEFITS   ")
    print(b5)
    print()
# FUNCTION TO ADD INFORMATION OF A PERSON IN DATABASE.
def adb():
    a1=int(input('Enter ID'))
    a2=input('Enter EMP_NAME')
    a3=int(input('Enter DOJ'))
    a4=int(input('Enter DOB'))
    a5=input('Enter POST')
    a6=int(input('Enter SALARY'))
    a7=input('Enter MOB_NO')
    a8=input('Enter ADDRESS')
    data=(a1,a2,a3,a4,a5,a6,a7,a8)
    ms="insert into banking values(%s,%s,%s,%s,%s,%s,%s,%s)"
    cll=c.cursor()
    cll.execute(ms,data)
    c.commit()
    print()
def adw():
    c1=int(input("Enter S_NO"))
    c2=input("Enter WNAME")
    c3=int(input("Enter MOB_NO"))
    c4=int(input("Enter SALARY"))
    da=(c1,c2,c3,c4)
    msqL="insert into workers_staff values(%s,%s,%s,%s)"
    clld=c.cursor()
    clld.execute(msqL,da)
    c.commit()
    print()
def adc():
    e1=int(input("Enter S_NO"))
    e2=input("Enter NAME")
    e3=input("Enter MOB_NO")
    e4=int(input("Enter CURR_AMMOUNT"))
    e5=int(input("Enter AMT_WITHDRAWED"))
    e6=input("Enter ONLINE_BENEFITS('YES/NO')")
    dat=(e1,e2,e3,e4,e5,e6)
    msql="insert into clients values(%s,%s,%s,%s,%s,%s)"
    cllld=c.cursor()
    cllld.execute(msql,dat)
    c.commit()
    print()
#FUNCTION TO UPDATE INGFORMATION.
def ub():
    a1=int(input('Enter ID'))
    a2=input('Enter EMP_NAME')
    a3=int(input('Enter DOJ'))
    a4=int(input('Enter DOB'))
    a5=input('Enter POST')
    a6=int(input('Enter SALARY'))
    a7=input('Enter MOB_NO')
    a8=input('Enter ADDRESS')
    datae=(a1,a2,a3,a4,a5,a6,a7,a8)
    mse=" update banking set ID=%s,EMP_NAME=%s,DOJ=%s,DOB=%s,POST=%s,SALARY=%s,MOB_NO=%s,ADDRESS=%s"
    el=c.cursor()
    el.execute(mse,datae)
    c.commit()
    print()
def uw():
    c1=int(input("Enter S_NO"))
    c2=input("Enter WNAME")
    c3=int(input("Enter MOB_NO"))
    c4=int(input("Enter SALARY"))
    daw=(c1,c2,c3,c4)
    msqw="update workers_staff set S_NO=%s,WNAME=%s,MOB_NO=%s,SALARY=%s"
    clldw=c.cursor()
    clldw.execute(msq,daw)
    c.commit()
    print()
def uc():
    e1=int(input("Enter S_NO"))
    e2=input("Enter NAME")
    e3=input("Enter MOB_NO")
    e4=int(input("Enter CURR_AMMOUNT"))
    e5=int(input("Enter AMT_WITHDRAWED"))
    e6=input("Enter ONLINE_BENEFITS('YES/NO')")
    datt=(e1,e2,e3,e4,e5,e6)
    msqlt="update clients set S_NO=%s,NAME=%s,MOB_NO=%s,CURR_AMMOUNT=%s,AMT_WITHDRAWED=%s,ONLINE_BENEFITS=%s"
    ell=c.cursor()
    ell.execute(msqlt,datt)
    c.commit()
    print()
#FUNCTION FOR DELETING THE RECORDS.
def delb():
    g=int(input("Enter ID"))
    de=(g,)
    sbn="delete from banking where ID=%s"
    bn=c.cursor()
    bn.execute(sbn,de)
    c.commit()
    print()
def delw():
    g1=int(input("Enter S_NO"))
    dew=(g1,)
    sbw="delete from workers_staff where S_NO=%s"
    wn=c.cursor()
    wn.execute(sbw,dew)
    c.commit()
    print()
def delc():
    g2=int(input("Enter S_NO"))
    dec=(g2,)
    sc="delete from clients where S_NO=%s"
    cn=c.cursor()
    cn.execute(sc,dec)
    print()
#MAIN PROGRAM STARTS......
while True:
    pro=int(float(input("ENTER YOUR CHOICE:")))
    if pro==1:
        dsply_all()
        print()
    elif pro==2:
        f1()
        print()
        h=int(float(input("ENTER YOUR CHOICE:")))
        if h==1:
            dp()
            print()
        elif h==2:
            dp1()
            print()
        elif h==3:
            dp3()
            print()
        else:
            print("INVALID CHOICE!")
            print()
    elif pro==3:
        f2()
        print()
        h1=int(float(input("ENTER YOUR CHOICE:")))
        if h1==1:
            adb()
            print()
        elif h1==2:
            adw()
            print()
        elif h1==3:
            adc()
            print()
        else:
            print("INVALID CHOICE!")
            print()
    elif pro==4:
        f3()
        print()
        h2=int(float(input("ENTER YOUR CHOICE:")))
        if h2==1:
            ub()
            print()
        elif h2==2:
            uw()
            print()
        elif h2==3:
            uc()
            print()
        else:
            print("INVALID CHOICE")
    elif pro==5:
        f4()
        print()
        h3=int(float(input("ENTER YOUR CHOICE:")))
        if h3==1:
            delb()
            print()
        elif h3==2:
            delw()
            print()
        elif h3==3:
            delc()
            print()
        else:
            print("INVALID CHOICE!")
    elif pro==6:
        break
        print("THANK YOU! FOR USING PORTAL❤")
    else:
        print("PLEASE ENTER VALID CHOICE")
print("WE'LL HOPE TO SEE YOU AGAIN😉")
#PROGRAM ENDS....
#THANK YOU!
#CREATED BY: CHIRAG JAGTAP.


    
    
    


     
