class School:
    def fun1(self):
        print("this function is in school")
class Student1(School):
    def fun2(self):
        print("this functuon is in student 1")
class Student2(School):
    def fun3(self):
        print("this function is in student 2")  
class Student3(Student1,School): 
    def fun4(self):
        print("this function is in student 3")
ob=Student3()
ob.fun1()
ob.fun2()                     