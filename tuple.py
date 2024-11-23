#Assign elements to a Tuple
#In python a tuple is a collection data type that is similar to a list but with one key difference, tuples are immutable.
#Meaning that once you create a tuple you can not change its contents aka add, remove, or modify elements
#() is a tuple [] is a string
print("======================================")
example = (1,2,3)
a,b,c=(example)
print(a,b,c)
print("======================================")
#iterating using "for" loops
print("======================================")

names = ["Alice", "Bob", "Charlie"]

for i in names:
    print(i)

numbers=1,2,3,4,5,5,5,5,6,7
print(numbers.count(5)) # number of times 5 appears

def get_coordinates():
    return(3,4)

x,y=get_coordinates()
print("The Location of the x & y Coordinates are:",x, "," ,y)

#Python Sets
#In Python a se is an unordered collection of unique elements
#Sets are defined by enclosing a comma-seperated sequence of elements within curly braces{} 
#or by using the set() constructor function. Here's how u create and with sets in python
#There are many different set methods 
#add(), remove(), discard(), clear(), copy(), pop(), len()

num={1,2,3}
real_numbers=set((3,4,5))
print(real_numbers)
print("======================================")
test_numbers=num.add(4)
print(num)

test_numbers=num.remove(4)
print(num)

test_numbers=num.add(3) #doesn't add another number if that exact number is already in the set
test_numbers=num.discard(2)
print(num)

#test_numbers=num.clear()
#print(num)

test_numbers=len(num)
print(test_numbers)
copy_num=num.copy()
print(copy_num)

#set operations
# union, interseection, difference, symmmetric difference
set1=set((1,2,3,4))
set2={3,4,4,5,6}
set3=set1.union(set2) # union example " | "
print(set3)
#intersection example " & "
set4=set1&set2
#set4=set1.intersection(set2)
print(set4)
#difference example " - " # gives the elements that are not in the set1 in this example and ONLY in set 2
set5=set2-set1
print(set5)
#symmetric difference example " ^ "
set6=set1^set2
print(set6)
set5.pop()
print(set5)
set6.pop()
print(set6)

num6=len(set6) # len() retunr the number of values in the string/tuple
print(num6)

#Frozen Sets
#Are an immutabe version of a set and cannot be changed like tuples
number_set=frozenset([1,2,3])
print(number_set)
#test_frozen_set=number_set.remove(2)  ##  the remove method is inactive due to python recognising the set as being a "frozenset" 
#returning AttributeError: 'frozenset' object has no attribute 'add'
#print(test_frozen_set)
print("==================================================")
print("============Student Record System=================")
#Name, age , grade
student1=("Gracie Smith","18","First Year")
student2=("Robert Atkin","19","Second Year")
student3=("Max Godwin","20","Third Year")

students=(student1,student2,student3)
#Count number of Students and index elements
print(f"The number of Students on record:",len(students) )
print(f"The records of Gracie Smith:",students.index(student1))
print("==================================================")
#Unique student ID's and course stored in sets
Unique_ID={"1001","1002","1003","1004"}
print( f"Student ID's:",Unique_ID)
Courses={"Maths","Pyhsics","Biology","Geography"}
print(f"Course available:",Courses)
print("==================================================")
#Update the number of Students, add new students remove completed courses and then update the system 
new_students=("1005","1006")
Unique_ID.update(new_students)
print(f"Student ID's:",Unique_ID)
print("==================================================")
completed_course={"Maths","Geography"}
courses_left=Courses-completed_course
print(f"Courses not completed:",courses_left)
print("==================================================")
#Create frozen sets to make immutable courses and student data
Course={"Maths","Pyhsics","Biology","Geography"}
frozen_course=frozenset(Course)
print(f"Frozen courses:",frozen_course)

Student_ids={"1001","1002","1003","1004"}
frozen_ids=frozenset(Student_ids)
print(f"Frozen Student ID's",frozen_ids)
#Attempting to add an additional ID to the set "1005". Executing the code below returns AttributeError: 'frozenset' object has no attribute 'add'
#frozen_ids.add("1005")
#print("Frozen ID's",frozen_ids)





