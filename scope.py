#def outer_function():
#   first_variable = 10
#    print(first_variable)
#outer_function()

def outer_function():
    outer_variable = 20
    def inner_function():
        print(outer_variable)
    inner_function()
outer_function()


global_variable=30
def global_function():
    print(global_variable)
global_function()


#THE LGB RULE
x=1
def f1():
    x=50
    def innfunction():
        x=60
        print(x)
    innfunction()
f1()
print(x)


global_var=90

def myfunction():
    global global_var
    global_var=80   
myfunction()
print(global_var)

#Python Modules











