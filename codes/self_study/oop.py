#Constructor in pythonClass
class Dog:

   # tricks = []
    
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)



dog_1 = Dog("fido")
dog_2 = Dog("mika")

dog_1.add_trick("roll over.")
dog_2.add_trick("play dead.")

print(dog_1.tricks)
print(dog_2.tricks)



class BankAcount:
     def __init__(self, balance: int, owner: str):
         self.balamce = balance
         self.owner = owner

def open_account(name:str):
    new_account = BankAcount(0 , name)
    return new_account

def deposit_money(account:BankAcount, amount: int):
    account.balamce += amount

saman_account = open_account("ali mousavi")
meli_account = open_account("ali mousavi")

deposit_money(saman_account, 300)
print(saman_account.balamce)


#inheritance

class Animal:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    def eat(self):
        print("i can eat")

class Cat(Animal):

    def __init__(self, name, type, age, bread):
        super().__init__(name, type, age)
        self.bread = bread

    def eat(self):
        print("i love eat bones!")


cat = Cat("pinky" , "cat" , 2, "persian")
cat.eat()


#Composition

class Engine:
    def start(self):
        print("engine start")

    def stop(self):
        print("engine stop")

class Lights:
    def on(self):
        print("Lights on")

    def off(self):
        print("Lights off")

class Car:
    def __init__(self):
        self.engine = Engine()
        self.lights = Lights()
    def start(self):
        self.engine.start()
        self.lights.on()

    def stop(self):
        self.engine.stop()
        self.lights.off()

car = Car()
car.start()
car.stop()

#Encapsulation

class Tree:

    def __init__(self, hieght):
        self.__hieht = hieght
        

    def get_hieght(self):
        return self.__hieht
    
    def set_hieght(self, new_hieght):
        self.__hieht = new_hieght

#Polymorphism

class Shape:
    def area():
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    
class Squere(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
def print_area(shape):
    print("Area: " , shape.area())

circle = Circle(12)
squere = Squere(10)

print_area(circle)
print_area(squere)