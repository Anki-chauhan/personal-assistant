import pymysql
connection= pymysql.connect(host='localhost',db='college',user='root')
cur=connection.cursor()

def login():
    name2=input("enter your username :")
    id2=input("enter your accountnumber :")
    cur.execute("select name,id from student where name=(%s) and id=(%s)",[(name2),(id2)])
    cur1=cur.fetchall()
    if cur1:
        for (name,id) in cur1:
            print("\n\t welcome your account Mr.{}\n".format(name2))
            while True:
                
                
                print("1.deposite")
                print("2.withdraw")
                print("3.show your total ammount")
                print("4.Go to back menu \n")
                choice1=input("enter your choice: ")
                if choice1=='1':
                          
                    cur.execute("select fee from student where name=(%s)",[(name2)])
                    f=cur.fetchall()
                    print("your balance is {}".format(f))
                    ammount_deposite = input("enter you deposite ammount: ")
                    cur.execute("select fee+(%s) from student where name=(%s)",[(ammount_deposite),(name2)])
                    w=cur.fetchall()
                    cur.execute("update student set fee=(%s) where name=(%s)",[(w),(name2)])
                    e=cur.fetchall()
                    connection.commit()
                    print("your amount will successfull deposite")

                if choice1=='2':
                    cur.execute("select fee from student where name=(%s)",[(name2)])
                    g=cur.fetchall()
                    print("your total balance is {}".format(g))
                    d=input("enter your widthdraw ammount: ")
                    cur.execute("select fee-(%s) from student where name=(%s)",[(d),(name2)])
                    t=cur.fetchall()
                    print(t)
                    cur.execute("update student set fee=(%s) where name=(%s)",[(t),(name2)])
                    connection.commit()

                if choice1=='3':
                    cur.execute("select fee from student where name =(%s)",[(name2)])
                    i=cur.fetchall()
                    connection.commit()
                    print("now your ramainning balance is :{} \n ".format(i))

                if choice1=='4':
                    break

            
                
    else:
        print("invalid username or pawword ")

def createaccount():
    name=input("enter your name: ")
    id =input("enter your account number: ")
    age=input("enter your age: ")
    city=input("enter your city: ")
    fee=input("enter your initial ammount : ")
    cur.execute("insert into student (name,id,age,city,fee) values (%s,%s,%s,%s,%s) ",[(name),(id),(age),(city),(fee)])
    connection.commit()
    print("your data have been added")

if __name__=="__main__":
    while True:
        print("1.create account ")
        print("2.login account ")
        print("3.exit \n")
        choice =input("enter your choice: ")
        if choice =='1':
            createaccount()
        if choice=='2':
            login()
        if choice=='3':
            break
