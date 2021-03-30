import random
def randInt():
    num = random.random()
    return num
print(randInt())# should print a random integer between 0 to 100
import random
def randInt(max=50):
    num = random.random()
    return num
print(randInt(50))# should print a random integer between 0 to 50
import random
def randInt(min=50):
    num = random.random()
    return num
print(randInt(50))# should print a random integer between 50 to 100
import random
def randInt(min=50 , max=500):
    num = random.random()
    return num
print(randInt(50,500))# should print a random integer between 50 and 500
