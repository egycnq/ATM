import pymysql
try:
    db = pymysql.connect("localhost", "admin", "admin", "testdb")
    cursor = db.cursor()
except:

    print("error connecting to database")

class data:
    def __init__(self,id,amount=0):
        self.id = id
        self.amount = amount

    def update(self):

        cursor.execute("UPDATE users SET Amount=%s WHERE CardID =%s ",(self.amount,self.id))
        db.commit()
    def find(self):
        cursor.execute("select Cardid FROM users")
        ids=cursor.fetchall()
        find=0
        for i in ids :
            if(i[0]==self.id):
              find=1
        if(find==1):
            return 1
        else:
            return 0