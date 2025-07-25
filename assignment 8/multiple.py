class A:
     aname = ''
def fun(self):
        print (self.aname)
class B:
     bname = ''
def fun1(self):
        print (self.bname)
class C(A, B):

    def fun2(self):
        print ('B :', self.bname)
        print ('A :', self.aname)

s1 = C()
s1.bname = 'Neha'
s1.aname = 'Swara'
s1.fun2()

