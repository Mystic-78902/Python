class computer:
    def __init__(self):
      self.__maxprice = 900
    def sell (self):
       print("Selling price", self.__maxprice)
    def setprice(self,price):
       self.__maxprice = price


mycomp = computer()
mycomp.sell()
mycomp.setprice(4500)
mycomp.sell()