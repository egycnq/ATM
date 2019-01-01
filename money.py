import pymysql
from DB import *
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
    def jafer(self): #اللي بتخصم من حساب العميل يا رامن بيك
        cursor.execute("select Amount FROM users WHERE CardID =%s",self.id)
        y=cursor.fetchone()
        new=y[0]-self.user_amount
        newobj=data(self.id,new)
        newobj.update()
    def osama(self):
        x=self.user_amount/200
        i, d = divmod(x, 1)
        cursor1.execute("select x,y,z FROM money")
        money=cursor1.fetchone()
        X=money[0]
        Y=money[1]
        Z=money[2]
        print(X-5)
        if(i<=Z):
            Z=Z-i
        else:
            temp=Z
            Z=0
            i=i-temp
            if(i*2<=Y):
             Y=Y-i*2
            elif(i*4<=X):
                X=X-i*4
            else:
                 print("Your Operation Cannot Be Processed")




