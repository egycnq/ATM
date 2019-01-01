from DB import *
from chk import *
from money import *

id=chkinput(input("Enter your ID: "))
id.chkid
pin=chkinput(id.id,input("enter your PIN: "))
pin.chkpin()
user_amount=int(input("enter your balance"))
withdraw=withdrewchk(user_amount,id.id)
withdraw.chkamount()#ده اللي بيتاكد من ان الفلوس موجودة في الماكنة وحسابه
withdraw.jafer() #ده اللي بيخصم
