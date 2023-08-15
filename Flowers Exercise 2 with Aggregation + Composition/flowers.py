#composition
class BUYER():
    def __init__(self,buyer):
        self.buyer = buyer
    def displayBuyer(self):
        return self.buyer

class FLOWER():
    def __init__(self,name=None,price=None,colour=None,season=None,size=None,buyer=None):
        if name is None:
            self.__name = "Rose"
        else:
            self.__name = name

        if price is None:
            self.__price = 5.99
        else:
            self.__price = price
        
        if colour is None:
            self.__colour = "Red"
        else:
            self.__colour = colour

        if season is None:
            self.__season = "Spring"
        else:
            self.__season = season
        
        if size is None:
            self.__size = "Medium"
        else:
            self.__size = size

        if buyer is None:
            self.__buyer = "Unknown"
        else:
            self.__buyer = buyer

        self.__nameBuyer = BUYER(self.__buyer)

    def setName(self,n):
        self.__name = n
        
    def setPrice(self,p):
        self.__price = p

    def setColour(self,c):
        self.__colour = c
        
    def setSeason(self,s):
        self.__season = s

    def setSize(self,sz):
        self.__size = sz

    def getName(self):
        return self.__name
        
    def getPrice(self):
        return self.__price

    def getColour(self):
        return self.__colour
        
    def getSeason(self):
        return self.__season

    def getSize(self):
        return self.__size

    def getBuyer(self):
        return self.__nameBuyer.displayBuyer()






