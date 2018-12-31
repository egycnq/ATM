import pymysql
try:
    db = pymysql.connect("localhost", "admin", "admin", "testdb")
    cursor = db.cursor()
except:

    print("error connecting to database")

class data:
    def __init__(self,id,amount):
        self.id = id
        self.amount = amount

    def update(self):

        cursor.execute("UPDATE users SET Amount=%s WHERE CardID =%s ",(self.amount,self.id))
        db.commit()