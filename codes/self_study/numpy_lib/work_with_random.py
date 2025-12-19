from numpy import random

x = random.randint(100, size=(3, 5))

print(x)



from numpy import random

x = random.choice([3, 5, 7, 9])
print(x)

y = random.choice([3, 5, 7, 9], size=(3, 5))
print(y)


#RecursionError: maximum recursion depth exceeded


#  WHY?!


# --> file name is random and python is confieused to import witch module :)))