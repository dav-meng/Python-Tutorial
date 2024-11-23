import random

#Creating a random number generator
#Printing the random number along with its data type using the type() function.

R_Number_Generator=random.randint(1,1000)
x=R_Number_Generator
print("=========================================================")
print("Random Number Generated:", R_Number_Generator)
print("Data type", type(x))
print("Data type", type(R_Number_Generator))

#Camel case (ex: someVariable)
#Snake case (ex: some_variable)
#Pascal case (ex: SomeVariable)
camelCase="randomNumber"
snake_case="random_number"
PascalCase="RandomNumber"


#Type conversion for random numbers Complex number type conversion and float type conversion

float_number = float(x)
print("Random Number converted to a float number", float_number)
print("Data type after Conversion to float", type(float_number))

complex_number = complex(x)
print("Random Number converted to a Complex Number", complex_number)
print("Data type after Conversion to complex", type(complex_number))
print("=========================================================")
print("=========================================================")
y="Loving Python"
u="Learning the Basics"
print(y[0:6])
print(len(y))
#returns a true or false statement
print("Love" in y)
print("Loving" in y)
print("=========================================================")
print("=========================================================")
for y in y:
    print(y)
print("=========================================================")
if "Love" in y:
    print("Love is Present")
elif "Love" not in y:
    print("Love, is not Present")
