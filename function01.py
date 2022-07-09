#creates/defines a function
from socket import INADDR_ALLHOSTS_GROUP

print("\n")
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there')

hello() # calls/executes defined functions

# def with parameters
def name(name):
    print("Hello, " + name)
a = input("ENter your  name: ")
name(a)

def sayHello(name):
    print('Hello' + name)

sayHello('Al')


# chooses a random integer number from 2 to 9
import random 
r = random.randint(2,9)
print(r)


# A lucky draw
import random
def game(ans):
    if r == val:
        return 'You just won, $1000 '
    else:
        return 'Better luck next time'
r = random.randint(2,2)
print(r)
val = input("WHat's your ticket Number? \n Note: Ticket Number lies from 2 to 2  :")
res = game(r)
print(res)