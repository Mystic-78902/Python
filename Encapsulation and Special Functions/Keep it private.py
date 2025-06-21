class myclass:
    __pv = 27;
    def  __pm(self):
       print( "i am inside the class myclass")
    def hello(self):
        print("Private variable value", myclass.__pv)

obj1 = myclass()
obj1.hello()
obj1.__pm