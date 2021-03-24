import random

print("welcome to my number guessing game!")

x = random.randint(1, 100)

print(x)

lives = 3

while(lives > 0):
    nr = input("make a guess!")
    nr = int(nr)
    if nr > x:

        print("WOAH THERE,too high!Lives: ", lives=lives-1)

    elif x == nr:
        print("Congrats! You guessed it! Score:", lives*1000)
        break

    else:
        print("Don't be afraid to thing bigger!")
        print("Lives:", lives=lives - 1)
        print(lives)

    if lives == 2:
        print("Little hint,the sum of the digits is :", nr % 10 + nr % 100)
    elif lives == 1:
        print("one of the digi")
