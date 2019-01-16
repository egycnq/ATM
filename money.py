import pymysql
from DB import *
from datetime import *

try:
    db1 = pymysql.connect("localhost", "admin", "admin", "money")
    cursor1 = db1.cursor()
except:
    print("error connecting to database")
cursor1.execute("select x,y,z FROM money")
x= cursor1.fetchone()
total=x[0]*50+x[1]*100+x[2]*200
class withdrewchk :
    def __init__(self,usr_amount,id):
        self.user_amount=usr_amount
        self.id=id


    def chkamount(self):
        if(self.user_amount<=total):
         cursor.execute("select Amount FROM users WHERE CardID =%s",self.id)
         x=cursor.fetchone()
         if(self.user_amount<=x[0]):
            return 1
         else:
             print("No money in your balance")
             return 0
        else:
            print("No money in the ATM")
            return 0
    def jafer(self): #اللي بتخصم من حساب العميل
        cursor.execute("select Amount FROM users WHERE CardID =%s",self.id)
        y=cursor.fetchone()
        new=y[0]-self.user_amount
        newobj=data(self.id,new)
        newobj.update()
    def osama(self):
        close=0
        s=0
        x=self.user_amount/200
        i, d = divmod(x, 1)
        cursor1.execute("select x,y,z FROM money")
        money=cursor1.fetchone()
        X=money[0]
        Y=money[1]
        Z=money[2]
        if(i<=Z):
            Z=Z-i
            cursor1.execute("UPDATE `money` SET `z`=%s ",Z)
            s=s+i

        else:
            temp=Z
            Z=0
            cursor1.execute("UPDATE `money` SET `z`=%s ", Z)

            i=i-temp


            if(i*2<=Y):
             Y=Y-i*2
             cursor1.execute("UPDATE `money` SET `y`=%s ", Y)
             s=s+i*2

            else:
                temp = Y
                Y = 0
                cursor1.execute("UPDATE `money` SET `y`=%s ", Y)

                i = i*2 - temp
                s=s+i*2

                if(i*2<=X):
                 X=X-i*4
                 cursor1.execute("UPDATE `money` SET `x`=%s ", X)
                 s=s+i*4

                else:
                      print("Your Operation Cannot Be Processed")
                      close = 1

        if(d==0.25):
            if(X>=1):
                X=X-1
                s=s+1
                cursor1.execute("UPDATE `money` SET `x`=%s ", X)

            else:
                print("No 50 L.E")
                close = 1
        if(d==0.5):
            if(Y>=1):
                Y=Y-1
                s=s+1
                cursor1.execute("UPDATE `money` SET `y`=%s ", Y)

            else:
                if(X>=2):
                    X=X-2
                    s=s+2
                    cursor1.execute("UPDATE `money` SET `x`=%s ", X)

                else:
                    print("Your Operation Cannot Be Processed")
                    close = 1

        if(d==0.75):
            if(Y>=1):
                Y=Y-1
                s=s+1
                cursor1.execute("UPDATE `money` SET `y`=%s ", Y)

                if (X >= 1):
                    X=X-1
                    s=s+1
                    cursor1.execute("UPDATE `money` SET `x`=%s ", X)

                else:
                    print("Your Operation Cannot Be Processed")
                    close = 1
            else:
                if(X>=3):
                    X=X-3
                    s=s+3
                    cursor1.execute("UPDATE `money` SET `x`=%s ", X)

                else:
                    print("Your Operation Cannot Be Processed")
                    close=1
        if(s>30):
            close=1
            print("You Can Only Withdraw Up To 30 Papers")
        if(d!=0.25 and d!=0.5 and d!=0.75 and d!=0.0 ):
                close=1
                print("Enter A Valid Number")
        if(close==0):
            db1.commit()
            cursor.execute("select SumW FROM users WHERE CardID =%s", self.id)
            sum=cursor.fetchone()
            p=sum[0]
            p=p+self.user_amount
            cursor.execute("UPDATE `users` SET `SumW`=%s WHERE CardID = %s", (p,self.id))
            cursor.execute("UPDATE `users` SET `Date`=%s WHERE CardID = %s", (date.today(), self.id))
            db.commit()

    def mohaned(self):
        cursor.execute("select Date FROM users WHERE CardID =%s", self.id)
        d = cursor.fetchone()
        if(date.today()!=d[0]):
            cursor.execute("UPDATE `users` SET `SumW`=%s WHERE CardID = %s", (0, self.id))
            db.commit()
        else:
            cursor.execute("select SumW FROM users WHERE CardID =%s", self.id)
            sum = cursor.fetchone()
            p=sum[0]
            i=p+self.user_amount
            if(p>10000 or i>10000):
             print("Your Operation Cannot Be Processed")
             return 0
        return 1
class deposite :
    def __init__(self,x=0,y=0,z=0,id=0):
            self.x=x
            self.y=y
            self.z=z
            self.id=id

    def a(self):
        cursor1.execute("select x,y,z FROM money")
        x = cursor1.fetchone()
        A=x[0]
        B=x[1]
        C=x[2]
        X=A+self.x
        Y=B+self.y
        Z=C+self.z
        cursor1.execute("UPDATE `money` SET `x`=%s ", X)
        cursor1.execute("UPDATE `money` SET `y`=%s ", Y)
        cursor1.execute("UPDATE `money` SET `z`=%s ", Z)
        db1.commit()
        return 1

    def insertbank(self):
        total=self.x*50+self.y*100+self.z*200
        cursor.execute("select Amount FROM users WHERE CardID =%s", self.id)
        a=cursor.fetchone()
        b=a[0]
        total=total+b

        cursor.execute("UPDATE `users` SET `Amount`=%s WHERE CardID = %s", (total, self.id))
        cursor.execute("UPDATE `users` SET `Date`=%s WHERE CardID = %s", (date.today(), self.id))
        db.commit()

    def chk(self):
        m=self.x+self.y+self.z
        if(m>30):
            print("Your Operation Cannot Be Processed")
            return 0
        return 1
    def SumD(self):
        cursor.execute("select Date2 FROM users WHERE CardID =%s", self.id)
        d = cursor.fetchone()
        print(d[0])
        if (date.today() != d[0]):
            cursor.execute("UPDATE `users` SET `SumD`=%s WHERE CardID = %s", (0, self.id))
            db.commit()
        else:
            cursor.execute("select SumD FROM users WHERE CardID =%s", self.id)
            sum = cursor.fetchone()
            p = sum[0]
            print(sum[0])
            total = self.x * 50 + self.y * 100 + self.z * 200
            i = p + total
            cursor.execute("UPDATE `users` SET `SumD`=%s WHERE CardID = %s", (i, self.id))
            if (p > 10000 or i > 10000):
                print("Your Operation Cannot Be 2Processed")
                cursor.execute("UPDATE `users` SET `SumD`=%s WHERE CardID = %s", (p, self.id))
            db.commit()































