# Prompt the user for the inputs to the profile generator
print("================================================")
print("User Profile Generator".center(50))
print("================================================")
input_string= print("Please Enter the following information in this order. \n1.First name \n2.Last name \n3.Age \n4.City \n5.Occupation ")
First_name = input("First Name: ")
Last_name = input("Last Name: ")
Age = input("Age: ")
City = input("City: ")
Occupation = input("Ocuppation: ")

# Concatenate first name and last name

Full_Name = First_name +" "+ Last_name

# Use string methods to modify the full name and profile description
mod_full_name= Full_Name.title()

Profile_desc = f"{mod_full_name} is {Age} years old, lives in {City} and \nworks as a {Occupation}."

# Add escape characters to include quotation marks and a new line
profile_info = "Profile information: \n" + Profile_desc

mod_desc= profile_info.replace("a","an") if Occupation.startswith(("a", "e", "i", "u", "o")) else profile_info

# Display the User Profile
print("====================User Profile==================")
print(mod_full_name)
print(mod_desc)
print("==================================================")

