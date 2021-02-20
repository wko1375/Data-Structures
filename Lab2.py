class Polynomial:
    def __init__(self,colist = []):
        self.colist = colist
    def __str__(self):
        if self.colist == []:
            return "0"
        else:
            finalpoly = ""
            position = len(self.colist)
            for i in self.colist:
                finalpoly += str(position) + str(self.colist[i-1]) + "x^"  
                print(finalpoly)
                position -=1

                if position > 0:
                    finalpoly+=" + "
        return finalpoly



p = Polynomial([1,3,5,5,4])
print(str(p))
