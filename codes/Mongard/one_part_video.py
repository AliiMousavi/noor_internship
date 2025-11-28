watched_video = ["f-string","polymorphism","duck typing",
"__str__","__ repr__","Lmabda","zip","pip","pprint","timeit",
"OSI","super","/","*","csv","arry","email","len","nested class",
"sort,sorted","enum","redus","filter","map", "solid" ,"solid2", "datetime", "oprational method",
"Json", "work with Json", "encapsulation", "abstract class", "multi inheritance",
"init", "if name == main", "itrate", "functions", "generator", "underscore",
"anakonda", "return","google python style", "pydantic", "atexit","contribute to open source",
"dns","monkey patch","proxy","NotImplemented","gc","init_subclass",
"singledispatch","missing","content types", "heapq", "pillow", "glob",
"math"," lru_cache", "http", "inheriting built-in object","stub file",
"getpass"]

print(f"i watched {len(watched_video)} of mongard's one part video")




#fstring
number1 = 10_000_000_000_000
print(f"price = {number1:,}")

string1 = "Hello"
print(f"{string1:>20}")
print(f"{string1:20}")
print(f"{string1:^20}")


from datetime import datetime
now = datetime.now()
print(f"{now:%d.%m.%y}")


number2 = 342342354556.956534834
print(f"{number2:,.0f}")


#polymorphism in python

class Bird:
    def sound(self):
        print("jik jik.")

class Cat:
    def sound(self):
        print("meow meow!")

class Dog:
    def sound(self):
        print("Hop Hop!")

def animal_sound(animal):
    animal.sound()

bird = Bird()
cat = Cat()
dog = Dog()

animal_sound(bird)
animal_sound(cat)
animal_sound(dog)

#duc typing

person = {"name":"ali",
           "age":23,
           "car":"BMW"}

def print_person(dic):
    try:
        print(dic["name"], dic["age"])
    except KeyError:
        print("Some keys are mising")

print_person(person)

#lambda

add = lambda x,y: x+y
print(add(4,5))

x = [1,2,3,4,5,6,7,8,9]
print(list(map( lambda x:x*x , x)))

#zip file

import zipfile

with zipfile.ZipFile("myzipfile.zip",
                     "w",
                     compression=zipfile.ZIP_DEFLATED) as myzip:
    myzip.write(r"D:\Projects\CODE\python code\noor\two.py")



    






