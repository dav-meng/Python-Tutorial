#Disctionaries are a fundamental data Structure in Python that allow you to store and retreieve data in key-value pairs.
#Each disctionary is unique and you can use it to access the corresponding value vquickly. Disctionaries are also know as 
# associative arrays or hash maps in other programming languages.
print("===============================================")
#Creating an empty dictionary
empty_dictionary={}
print(empty_dictionary)

newyork_dict={
    "name":"James",
    "age":30,
    "city":"New York"
}
print(newyork_dict)

name = newyork_dict["name"]="John"
age=newyork_dict["age"]
city=newyork_dict["city"]="New Jersey"
print(name)
print(age)
print(city)

#keys()
#values()
#items()
print(newyork_dict.keys())
print(newyork_dict.values())
print(newyork_dict.items())
print("===============================================")
for key in newyork_dict:
    print(key,newyork_dict[key])
print("===============================================")
for value in newyork_dict:
    print(value,newyork_dict[value])
print("===============================================")
for items in newyork_dict:
    print(items,newyork_dict[items])
print("===============================================")
for key, value in newyork_dict.items():
    print(value, key) #print(key,value) for the same placement of data in previous example. Variable placement in brackets important for printing of info

print("===============================================")
#to make a copy of the data it can be done 2 ways SHOWN BELOW using .copy() 
print("Copy of Data being Taken")
mycopy=newyork_dict.copy()
print(mycopy)
dict_copy=dict(newyork_dict)
print(dict_copy)
print("===============================================")
###
#Conditional Statements
###
#Functions
##

def greet(name):
    print(f"Hello!" + " How are you " + name + "?" )

greet("Jon")
##
#Recursive Functions
##
#Word Frequencey Counter
print("=========================================================")
print("================Word Frequency Counter===================")
print("=========================================================")

def word_fdictionary(text):
    if not text:
        return{}

    text = text.lower().replace(",","").replace(".","").replace("!","").replace("?","")

    words=text.split()
   
    frequency={}

    def process_words(words,index):
        if index==len(words):
            return
    
    #Gets the current word
        word = words[index]

        if word in frequency:
            frequency[word] +=1
        else:
            frequency[word] =1 

        process_words(words,index+1)

    process_words(words,0)
    return frequency

text = "Here is my sentence, lots of words are repeated in this sentence and it is in my interest  to repeat these words for this test! Lots of the same words appear again!"
frequency_dict = word_fdictionary(text)

sorted_words = sorted(frequency_dict.items(),key=lambda item: item[1],reverse=True)

print("============== Unsorted List =============================")
for word, count in frequency_dict.items():
    print(f"{word} : {count}") 
print("==========================================================")
print("=============== Sorted List ==============================")
for word, count in sorted_words:
    print(f"{word} : {count}")    








