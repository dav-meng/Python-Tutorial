# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y

a=10
b=3

addition = a + b
subtraction = a -b 
multiplication = a*b
divison= a/b
modulus = a%b
exponentiation = a**b
floor_division = a//b

print(addition)
print(subtraction)
print(multiplication)
print(divison)
print(modulus)
print(exponentiation)
print(floor_division)

# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y

# using in and not in operators to see if a statement is true or false

number_list=[1,2,3,4,5,6]
is_not_in= 10 not in number_list
is_in= 10 in number_list # when a number is not in the list, it returns a false statement
print(number_list)
print(is_not_in)
print(is_in)
print("======================================")



# Operator	Name	                Description
# & 	    AND	                    Sets each bit to 1 if both bits are 1
# |	        OR	                    Sets each bit to 1 if one of two bits is 1
# ^	        XOR	                    Sets each bit to 1 if only one of two bits is 1
# ~ 	    NOT	                    Inverts all the bits
# <<	    Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	    Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

a = 3
b = 5 
result=a&b
print(result)
result=a>>b
print(result)
print("====================================")
number_list.append(10) # adds an additional number onto the end of the list, this time this one being 10
print(number_list)
print(number_list[6]) #prints the number that is in the 6th position, from the list

number_list.insert(1,3) # insert numver 3 at position 1 in the list
print(number_list)

number_list.remove(5) # removes exactly one instance of that number in the list
print(number_list)

print("=================================")



len(number_list)
print(len(number_list))
number_list.sort()
print(number_list)
number_list.reverse()
print(number_list)

number_list.count(3)
total_count_no3 = number_list.count(3)
#print(number_list)
print(total_count_no3)
list_index = number_list.index(1)
print(list_index)
print(~5)



