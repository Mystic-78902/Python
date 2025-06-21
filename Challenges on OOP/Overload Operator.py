class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if(self.a<other.a):
            return "obi1 is less than obi2" 
        else:
            return "obi2 is less than obi1"
    def __eq__(self, other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"

obi1 = A(2)
obi2 = A(3)
print("Passed Values :", obi1.a, obi2.a)
print(obi1 < obi2 )

obi3 = A(4)
obi4 = A(4)
print("Passed Values :", obi3.a, obi4.a)
print(obi3 == obi4 )