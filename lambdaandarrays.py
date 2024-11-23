#Lambda Function, It is a small Anonymous function 
# A lambda function can take any number of arguments, but can only have one expression.
x=lambda a , g , b: a*g + b
print("My Random numbers Equal:")
print(x(3,6,11))

def number(n):
    return lambda f:f*n

check = number(4)
another = number(6)
print(check(1))
print(another(12))

from array import array
myarray = array("i",[1,2,3,4,5,6]) # Currently in 1 dimension



#pip install numpy
import numpy as np

myarray=np.array([1,2,3,4,5,6])
array1=np.array([1,2,3,4])
array2=np.array([4,5,6,7])

result=array1+array2

print(result)

element1=myarray[0]
sliced=myarray[1:4]
print(sliced)

array3=np.array([[4,5,6,7,8,9],[1,2,3,4,5,6]])
myarray1=np.array([8,3,7,2,9])
print(array3)
sorted=np.sort(myarray1)
mean=np.mean(array3)
print(sorted)
print(mean)

for element in myarray1:
    print(element)

###########################################
class Myclass:
    class_variables="I am class variable"

def init (self, attribute1,attribute2):
    self.attribute1= attribute1
    self.attribute2= attribute2

    def instant_method(self):
        return "I am an instance method"
    object = Myclass("Value1","Value2")

    object.attribute1 #accessing instance attribute
    Myclass.class_variables

    object.instance.method() 

#inheritance allows a class to use methods and properties from a parent class
#class newclass(ParentClass):
#    attributes 
#def instance_method(self)
#    self.attributes

#@classmethod

#def class_method(cls)
    
#@staticmethod
#def static_method()
    
###### Variable Scope





































































