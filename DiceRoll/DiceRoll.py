
import random

print("Welcome To My DiceRoll Simulator!")
x = 1
print("Please input how many faces you would like your dice to have: ")
y = input()
while x != 0:
    d = random.randint(int(x), int(y))
    print("The dice landed on:")
    print(d)

    x = input("To play again press 1,to stop press 0")
