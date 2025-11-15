#L1_Variables
print("\n================== L1_Variables  ===============\n")
print("Hello, world!")

a = 20
b = 5.5
print(type(a))
print(type(b))

name = "ali"
print(type(name))

string = "you can't read this."

print(21 // 4)

#L2_String
# stings are immutable
print("\n================== L2_String  ===============\n")

str1 = "hello "
str2 = "world!"

print(str1 + str2)
print("hello " "world!")

duc_string = """
this is
a ducString
for test
"""

print(duc_string)

whatsup = "how are you? my name is ali. "\
            "nice to meet you."
whatsup2 = ("how are you? my name is ali. "\
            "nice to meet you.")
print(whatsup2)

address = r"\D\python\tamrin"
print(address)

name1 = "my name is ali."
x = name1[3:7]
print(x)
print(len(name1))

#L3_List
# list is mutable.
print("\n================== L3_List   ===============\n")

list1 = ["ali" , "asghar", "ahmad"]
list2 = ["kevin", "ann" , "matilda"]
list2.append("jack")
list2[:-1] = []
print(list1[:] + list2)
print(len(list2))

#L4_while loop
print("\n================== L4_while loop  ===============\n")

counter = 0

while counter < 10:
    print(counter , end=", ")
    counter+=1

print("done")

#L5_if Statements
print("\n================== L5_if Statements  ===============\n")

age = 19

if age < 18:
    print("you can't access")
elif age == 18:
    print("18")
else:
    print("welcom!")

#L6_for loop
print("\n================== L6_for loop  ===============\n")

names = ["ali" , "asghar", "ahmad", "kobra"]

for n in names:
    print(n , len(n))

#L7_range
print("\n================== L7_range  ===============\n")

for x in range(5, -16, -2):
    print(x, end=", ")

#L8_break-continue-pass
print("\n================== L8_break-continue-pass  ===============\n")

namess = ["ali" , "asghar", "ahmad", "kobra" , "soghra"]

for x in namess:
    if x == "kobra":
        continue
    print(x)

else:
    print("end.")

#L9_functions
print("\n================== L9_functions  ===============\n")

def helloToUser(name = "user"):
    return "hello " + name

print(helloToUser("ali"))

#L10_more-on-list
print("\n================== L10_more-on-list  ===============\n")

names1 = ["ali" , "asghar", "ahmad", "kobra" , "soghra", "ali"]

names1.append('reza')
names1.extend(["zahra" , "maryam"])
names1.insert(1,"qazanfar")
names1.remove("ali")
print(names1.pop())
print(names1.index("ali"))
print(names1.count("ali"))
names1.sort()

print(names1)

#L11_tuple
#tuple is immutable.
print("\n================== L11_tuple  ===============\n")

tuple1 = ("ali",)
print(type(tuple1))

#L12_set
print("\n================== L12_set  ===============\n")

setOfnames = {"kevin" , "amir", "ali" , "amir"}
print(setOfnames)
if "ali" in setOfnames:
    print("yes")
if "ahmad" not in setOfnames:
    print("no")

letters = set()
print(letters)

#L13_dictionary
print("\n================== L13_dictionary  ===============\n")

dictOfAges = {
    "amir":20,
    "ali":24,
    "ahmad":30
}

dictOfAges["anna"] = 20
dictOfAges["ali"] = 20
del dictOfAges["amir"]

print(dictOfAges)
print("ali" in dictOfAges)

for k,v in dictOfAges.items():
    print(k,v)

#L14_module
print("\n================== #L14_module  ===============\n")

import two
from two import number as num

two.say_something_to_user()
print(num)

#L15_fstring
print("\n================== #L15_fstring  ===============\n")

name3 = "ali"
age3 = 34

print(f"{name3:8} is {age3:2} years old")

#L16_format
print("\n================== #L16_format  ===============\n")

print("{} is {} years old".format(name3,age3))

info = {"name":"ali" , "age":12}
print("{0[name]} is {0[age]} years old".format(info))


#L17_files
print("\n================== #L17_files  ===============\n")

with open(r"D:\Projects\CODE\python code\noor\text.txt") as f:
    print(f.read(22))
    print(f.read(22))
    print(f.seek(22))
    print(f.tell())

print(f.closed)

#L18_scope
print("\n================== #L18_scope  ===============\n")

num18 = 12 #global scope

def show():
    num18 = 13 #local scope
    print(num18)

print(num18)


#L19_class
print("\n================== #L19_class  ===============\n")

class Car:
    pass
car1 = Car()
car2 = Car()

car1.name = "pride"
car2.name = "benz"

car1.price = 100
car2.price = 900

print(f"{car1.name} costs {car1.price}")

#L20_methods
print("\n================== #L20_methods  ===============\n")

class Carr:
    def __init__(self, n , p):
        self.name = n
        self.price = p
        print(f"{self.name} costs {self.price}")

c1 = Carr("pride" , 100)
c2 = Carr("benz" , 900)

#L21_calss-variable
print("\n================== #L21_calss-variable ===============\n")

class Car1:
    obj_num = 0
    wheel = 4
    def __init__(self, n , p):
        self.name = n
        self.price = p
        Car1.obj_num +=1
        
    def show_wheel(self):
        print(f"{self.name} has {self.wheel} wheels")

    def show(self):
        print(f"i have a {self.name}")

c1 = Car1("pride" , 100)
c2 = Car1("benz" , 900)

print(Car1.obj_num)
c1.show_wheel()


#L22_calss-static-method
print("\n================== #L22_calss-static-method ===============\n")

import datetime

class Person:
    def __init__(self , name , height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name} is {self.height} and {self.age} yearsOld")

    @classmethod
    def from_birth(cls , name , height, age):
        return cls(name , height , datetime.datetime.now().year - age )
    
    @staticmethod
    def is_adult(age):
        if age>18:
            print("yes")
        else:
            print("no")


person1 = Person.from_birth("ali" , 177 , 1990)
person1.show()
Person.is_adult(23)


#L23_inheritance
print("\n================== #L23_inheritance ===============\n")

class Motor(Car1):
    wheel = 2

    def show(self):
        super().show()
        print(f"i ride a {self.name}")

m = Motor("honda" , 80)
m.show()

#L24_special-method
print("\n================== #L23_inheritance ===============\n")

class Motor1(Car1):
    wheel = 2

    def __str__(self):
        return f"{self.name} - {self.price}"
    
    def __add__(self , other):
        return self.price + other.price


motor1 = Motor1("honda" , 80)
motor2 = Motor1("honda120" , 120)
print(motor1)
print(motor1 + motor2)


#L25_access-point
print("\n================== #L25_access-point ===============\n")

class Person25:
    name = "amir"   #public
    _age = 12       #protected
    __height = 190  #private


class Man(Person25):
    def show(self):
        print(self.name)



man = Man()
man.show()


#L26_property
print("\n================== #L26_property ===============\n")

class Person26:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lanme = lname

    @property
    def full_name(self):
        return f"{self.fname} {self.lanme}"
    

person26 = Person26("amir" , "alavi")
print(person26.full_name)
        

#L27_exceptions
print("\n================== #L27_exceptions ===============\n")

try:
    f = open("amir.txt")
    print(str.upper(32))
except TypeError:
    print("name must be string.")
except FileNotFoundError:
    print("file not found")
else:
    print("this code worked correctly")
finally:
    print("i dont care")


#L28_standard-library
print("\n================== #L28_standard-library ===============\n")

import jdatetime

print(jdatetime.datetime.now())


#L29_docString
print("\n================== #L29_docString ===============\n")

class Cat:

    """
    this is a doc string for cat class
    """
    
help(Cat)


#L30_venv
print("\n================== #L30_venv ===============\n")

"""
python -m venv name
name/Scripts/activate.bat
"""


