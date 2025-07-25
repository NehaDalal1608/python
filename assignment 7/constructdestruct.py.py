class demo:
    def __init__(self):                         #constructor
        self.s=10
        print("value of s is: ",self.s)
    def display(self):
        print("Parent class.")
    def __del__(self):                          #destructor
        print("descructor is called.")
class child(demo):                                 #single inheritance
    def display1(self):
        print("Child class")
ob= child()
ob.display() 
ob.display1()




