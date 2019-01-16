from DB import *
from datetime import *
d=datetime.strptime(input(), '%Y,%m,%d').date()

cursor.execute("UPDATE `users` SET `Date2`=%s WHERE CardID =9876543219876543",d)
db.commit()