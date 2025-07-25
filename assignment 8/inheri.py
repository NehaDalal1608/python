class principal:                                 #multilevel inheritance
	def fun(self):
		print("I am head of school")
 
class teacher(principal):
	def fun1(self):
		print("I teach the students")
 
class student(teacher):
	def fun2(self):
		print("I am student in school")
 
o = student()
o.fun()
o.fun1()
o.fun2()