# Import the builtins module 
import builtins 
# Get a list of all names in the builtins module 
all_builtins = dir(builtins) 
# Filter the list to show only functions 
builtin_functions = [name for name in all_builtins if callable(getattr(builtins, name))] 
# Print the list of built-in functions 
print(builtin_functions)


  
