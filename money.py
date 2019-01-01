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