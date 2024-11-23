#Boolean practise
print(10>9) #returns as True
print(4>29) #returns as false
print(4==4) #returns as true

# logical operators and the conditions they return true
# and
# or
# not

x = True
y = False 

result_and = x and y #
print(result_and)

result_or = x or y #
print(result_or)

result_not = not y # not x will return True
print(result_not)


# Boolean functions
number =6 

def is_even(number): 
    return number % 2 == 0   
print("=================")
result = is_even(6)
print(result)
print("=================")
print(bool("Hello!"))
print(bool(20))

x="Hello"
y=35
print(bool(x))
print(bool(y))
print("======================================")
print("======================================")
# Boolean test Recommending movies based on peoples tastes
print("==================Movie Preferences====================")
# List all the movie genre options
action = input("Do you like action movies? (yes/no): ").lower() == "yes"
comedy = input("Do you like comedy movies? (yes/no): ").lower() == "yes"
fantasy = input("Do you like fantasy movies? (yes/no): ").lower() == "yes"
romance = input("Do you like romance movies? (yes/no): ").lower() == "yes"
drama = input("Do you like drama movies? (yes/no): ").lower() == "yes"
kdrama = input("Do you like kdrama movies? (yes/no): ").lower() == "yes"

# Combine booleans using logical operators
if action and comedy and fantasy and romance and drama and not kdrama:
    genre = "Action-Comedy-Fantasy-Romance-Drama Movie"
elif action and comedy and fantasy and romance and kdrama and not drama:
    genre = "Action-Comedy-Fantasy-Romance-KDrama Movie"
elif action and comedy and fantasy and kdrama and drama and not romance:
    genre = "Action-Comedy-Fantasy-Drama-KDrama Movie"
elif action and comedy and kdrama and drama and romance and not fantasy:
    genre = "Action-Comedy-Romance-Drama-KDrama Movie"
elif action and fantasy and kdrama and drama and romance and not comedy:
    genre = "Action-Fasntasy-Romance-Drama-KDrama Movie"
elif fantasy and kdrama and drama and romance and comedy and not action:
    genre = "Comedy-Fantasy-Romance-Drama-KDrama Movie"
elif action and fantasy and kdrama and drama and romance and comedy:
    genre = "Action-Comedy-Fantasy-Romance-Drama-KDrama Movie"
elif action:
    genre = "Action"
elif comedy:
    genre = "Comedy"
elif fantasy:
    genre = "Fantasy"
elif romance:
    genre = "Romance"
elif drama:
    genre = "Fantasy"
elif kdrama:
    genre = "Kdrama"
else:
    genre = "Unknown"

# Recommend Movies based on preferences

if genre == "Action-Comedy-Fantasy-Romance-Drama Movie":
    print("Recommended Movies: \"Everything\" ")
elif genre == "Action-Comedy-Fantasy-Romance-KDrama Movie":
    print("Recommended Movies: \"Everything\" ")  
elif genre == "Action-Comedy-Fantasy-Drama-KDrama Movie":
    print("Recommended Movies: \"Everything\" ")
elif genre == "Action-Comedy-Romance-Drama-KDrama Movie":
    print("Recommended Movies: \"Everything\" ")
elif genre == "Action-Fasntasy-Romance-Drama-KDrama Movie":
    print("Recommended Movies: \"Everything\" ")
elif genre == "Comedy-Fantasy-Romance-Drama-KDrama Movie":
    print("Recommended Movies: \"Everything\" ")
elif genre =="Action-Comedy-Fantasy-Romance-Drama-KDrama Movie":
    print("Recommended Movies: \"Everything\" ")
elif genre == "Action":
    print("Recommened Movies: 'Place Holder 1', 'Place Holder 1', 'Place Holder 1' ")
elif genre =="Comedy":
    print("Recommened Movies: 'Place Holder 2', 'Place Holder 2', 'Place Holder 2' ")
elif genre == "Fantasy":
    print("Recommened Movies: 'Place Holder 3', 'Place Holder 3', 'Place Holder 3' ")
elif genre == "Kdrama":
    print("Recommened Movies: 'Place Holder 4', 'Place Holder 4', 'Place Holder 4' ")
elif genre == "Romance":
    print("Recommened Movies: 'Place Holder 5', 'Place Holder 5', 'Place Holder 5' ")
else:
    print("Sorry, there are no Movies available with those movie preferences.")
