from DB import *
class chkinput:

    def __init__(self,id):
        self.id=id

    def chkid(self):

        if(self.id ==''):
            self.id=0
        find = data(int(self.id))
        if( find.find()==0):
            print("plz enter a correct ID")
        else:
            print("Correct ID :D")
            return 1
