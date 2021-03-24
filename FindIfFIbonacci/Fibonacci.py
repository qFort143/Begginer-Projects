def fibo(a):
    x = 1
    y = 1
    while(True):
        x = x+y
        if(a == x):
            print(a, "belongs to the Fiboncci sequence")
            break
        y = x+y
        if(a == y):
            print(a, "belongs to the Fibonacci sequence")
            break
        if(x > a or y > a):
            print("The number does not belong to the Fibonacci sequence")
            break


a = input("Please enter a number: ")

fibo(int(a))
