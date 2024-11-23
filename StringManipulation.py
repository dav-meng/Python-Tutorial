#Practising String manipulation techniques
x="Loving Loving Python" "Learning Basics"
y="Loving Loving Python"
print(x[0:6])

#upper and lower case manipulation
print(x.upper())
print(x.lower())

#replacing string text manipulation
print(x.replace("Loving" , "I Love"))


#using strip() to remove white spaces
print(x.strip())


#spltting strings
print(y.split())

#joining or concatenating strings together
a = "Hi"
b =" This is Fun"
#a + b = c
c = a + b

print(c)

#formatting string format

age =27
my_age = "My age is: {}"

print(my_age.format(age))

prices = 45.07
itemsno = 2093
quantity = 689

my_order = "I want item {}, I want about {}, set at a price of {} pounds."
print(my_order.format(itemsno, quantity, prices))
print(my_order.center(100))
print("========================================================================")
#Practise using escape characters
#\' single quote
#\\ Backslash
#\n New line
#\r Carriahe Return
#\t Tab
#\b Backspace
#\f Form Feed
#\ooo Octal Value
#\xhh   Hex Value 

python_coding = "I am going to get through this course as fast as possible"
python_coding = "I am going to get through this course as fast as \"possible"
#python_coding = "I am going to get through this course as fast as \\possible"
#python_coding = "I am going to get through this course as fast as \npossible"
#python_coding = "I am going to get through this course as fast as \rpossible"
#python_coding = "I am going to get through this course as fast as \tpossible"
#python_coding = "I am going to get through this course as fast as \bpossible"
#python_coding = "I am going to get through this course as fast as \fpossible"
#python_coding = "I am going to get through this course as fast as  possible"
#python_coding = "I am going to get through this course as fast as  possible"
print(python_coding)
print("========================================================================")

txt = "My name John"
print(txt.encode(encoding='UTF-8' , errors='ignore'))

print("Python"[::-1])

###############################################################
print("========================================================================")
print("========================================================================")
print("========================================================================")
#creation of string manipulation tool
print("String Manipulation Tool".center(70))
#1. Prompt the user to enter a string.

#2. Display a menu of string manipulation options:

#Option 1: Convert the string to uppercase
#Option 2: Convert the string to lowercase
#Option 3: Slice the string from a start index to an end index
#Option 4: Calculate the length of the string
#Option 5: Loop through each character in the string and display it on a new line
##3. Prompt the user to enter their choice.

#4. Perform the selected string manipulation operation and display the result.
print("========================================================================")
input_string=input("Please enter a string value:  ")

#Create string input menu and available choices
print("\nString Manipulation Menu: ")
print("Option 1: Convert string to uppercase")
print("Option 2: Convert string to lowercase")
print("Option 3: Slice the string from a start index to an end index")
print("Option 4: Calculate the length of the string")
print("Option 5: Loop through each character in the string and display it on a new line")

choice=int(input("Enter your choice from (1-5):  "))
#perform the string manipulation
if choice == 1:
    result = input_string.upper()
    print("Uppercase: ", result)
elif choice == 2:
    result = input_string.lower()
    print("Lowercase: ", result)
elif choice == 3:
    start = int(input("Enter start index: "))
    end = int(input("Enter end index: "))
    result = input_string[start:end]
    print("Sliced string: ", result)
elif choice == 4:
    length = len(input_string)
    print("Length: ", length)
elif choice == 5:
    print("Characters: ")
    for character in input_string:
        print(character)
else:
    print("That is an Invalid Choice!")

