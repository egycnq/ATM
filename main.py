from DB import *
from chk import *
from money import *
from Services import *
id=chkinput(input("Enter your ID: "))
while(id.chkid):
    id = chkinput(input("Enter your ID: "))
pin=chkinput(id.id,input("enter your PIN: "))
while(pin.chkpin()):
    pin = chkinput(id.id, input("enter your PIN: "))
print('''
1 -> withdraw
2 -> deposite
3 -> services
''')
k=int(input("Enter Your Choice: "))

if(k==1):
    user_amount=int(input("Enter The Amount Of Wanted Cash:  "))
    withdraw = withdrejmnwchk(user_amount, id.id)
    if(withdraw.chkamount()): # ده اللي بيتاكد من ان الفلوس موجودة في الماكنة وحسابه
      if(withdraw.mohaned()):
        withdraw.jafer()  # ده اللي بيخصم من حسابه في البنك
        withdraw.osama()  # ده اللي بيخصم من عدد الورق اللي في الماكنة
elif(k==2):
    x = int(input("Enter Number of 50L.E: "))
    y = int(input("Enter Number of 100L.E: "))
    z = int(input("Enter Number of 200L.E: "))
    dep = deposite(x, y, z, id.id)
    if (dep.chk()):
        x = dep.a()
        if (x):
            dep.insertbank()
            dep.SumD()
elif(k==3):
    print('''
    1 -> Account Statment 
    2 -> Mobile Charging Cards
    ''')
    c=int(input("Enter Your Choice: "))
    if(c==1):
        d=datatime(id.id)
        d.show()




