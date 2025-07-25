# Base class                                #hierarchical inheritance
class A:
    def function_1(self):
        print ('Parent of B and C')
# Derived class1
class B(A):
    def function_2(self):
        print ('Child class of A')
# Derivied class2
class C(A):
      def function_3(self):
        print ('Child class of A')
object1 = C()
object2 = B()
object1.function_1()
object1.function_3()
object2.function_1()
object2.function_2()