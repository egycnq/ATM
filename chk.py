from DB import *
class chkinput:
    def __init__(self,id,pin=0):
        self.id=id
        self.pin=pin

    @property
    def chkid(self):

        if(self.id ==''):
            self.id=0
        find = data(int(self.id))
        if( find.find()==0):
            print("plz enter a correct ID")
            return 1
        else:
            return 0

    def chkpin(self):
            if (self.pin == ''):
                self.pin = 0
            find = data(self.id,0,int(self.pin))
            if (find.findpin() == 0):
                print("plz enter a correct PIN")
                return 1
            else:
                return 0