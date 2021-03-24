x = input("Please enter the year: ")

print(int(x)/4)

if(int(x) % 4 != 0):
    print("It's a common year")
elif (int(x) % 100 != 0):
    print("It's a leap year")
elif (int(x) % 400 != 0):
    print("It's a common year")
else:
    print("It's a leap year")
