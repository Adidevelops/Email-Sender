## PYTHON BASICS
a= 10
b=a**9   #** is for power 
print (b) 
b=a//6   #// is for floor division = does the division and returns the integer part only
print (b)

name = "aady is a student of coding"

print (name[::-1]) #reversing the string
# print (name is name1) #check if two strings are equal


# String FUnctions 
# isAlpha - checks if the string contains only alphabets 
# isDigit - checks if the string contains only digits
# isalnum - checks if the string contains only alphabets or digits
# islower - checks if the string contains only lower case alphabets
# isupper - checks if the string contains only upper case alphabets
# isspace - checks if the string contains only spaces
# istitle - checks if the string contains only title case
# isdecimal - checks if the string contains only decimal numbers
# totitle - converts the string to title case
# tolower - converts the string to lower case
# toupper - converts the string to upper case
# capitalize - capitalizes the first letter of the string
# swapcase - swaps the case of the string
# title - capitalizes the first letter of each word in the string
# lower - converts the string to lower case
# contains - checks if the string contains the specified substring

book1 = True
book2 = False

print(any([book1, book2])) #checks if any of the elements in the list is true

print(all([book1, book2])) #checks if all the elements in the list are true

complex = 2+3j # you can also use complex(2,3)
print(complex.real) #returns the real part of the complex number
print(complex.imag) #returns the imaginary part of the complex number
#  Enum Classes -> you can import the enum class from the Enum module  
students =["aady","a","b","c","d"]
students += ["e","f"] #adds the elements to the list
students.append("g",) #adds the element to the list
students.extend(["h","i"]) #adds the elements to the list
students.remove("i")    #removes the element from the list
students.insert(1,"Adi Vamsi") #inserts the element at the specified index
students[1:1]= ["Adi2","Adi3"] #inserts the element at the specified index
print(students[::-1])
section2 = [21,2,32,4,5,46,72,85,92,410]
print(sorted(section2,reverse=True)) #sorts the list in ascending order and reverses it
friends=("aady","yash","subbu","abhishek") #TUPLES are immutable that means there is no way to change the elements
friendswithage= {"aady":21,"yash":22,"subbu":23,"abhishek":24} #DICTONARY are mutable and can be used to store key value pairs
aadysage=friendswithage["aady"] #you can use the key to get the value
print(aadysage)

friends2 = {"aady","yash","subbu","abhishek"} #SETS are mutable and can be used to store unique elements
friends3 ={"Tom","Jerry","Sally","Jack","aady"}
friends4= friends2.union(friends3) #union of two sets
print(sorted(friends4))

count = 0
while count <friends.__len__():
    print(friends[count])
    count += 1  
for index,i in enumerate(friends):
    print(i)

class Animal:
    def walk():
        return("walks")
class Dog(Animal):
    def __init__(self,name,work):
        self.name=name
        self.work=work


    def bark(self):
        return ("woof!")

class Cat(Animal):
    def __init__(self,age):
        self.age = age
        print(age)
crock=Dog("crock","eating")
Dog.walk()
rock1= Dog("rock","spilling")
print(rock1.bark())
chalk=Cat(2)

