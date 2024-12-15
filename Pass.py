num=int(input("Please enter a number"))
for i in range(1,num):
    if num%20==0:
        print("Twist")
    elif num%15==0:
        pass
    elif num%5==0:
        print("Fizz")
    elif num%3==0:
        print("Buzz")
    else:
        print(i)