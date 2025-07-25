import array as arr
my_array = arr.array('i',[1, 2, 3, 4])
new= 100
my_array.append(new)
print("Array Elements After Append : ", my_array)
list1=[10,13,15]
my_array.extend(list1)
print("After Extending : ", my_array)
element1=67
position1=2
my_array.insert(position1,element1)
print("Array Elements After Inserting : ", my_array)
