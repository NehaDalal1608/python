A = "apple"

d = lambda string: string.upper()
print(d(A))
 
d = lambda string: string.capitalize()
print(d(A))

b = lambda string: string.replace("apple","MANGO")
print(b(A)) 

d = lambda string: string.lower()
print(d(A))


w = "Hello world   "

d = lambda string: string.strip()
print(d(w))

d = lambda string: string.casefold()
print(d(w))

d = lambda string: string.center(20)
print(d(w))

