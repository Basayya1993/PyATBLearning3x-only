# Fibonacci series
# Ex : Input ---> n = 7
# Output : 0,1,1,2,3,5,8,13

num = int(input("Enter the Value:"))
a = 0
b = 1

for i in range(0, num + 1):
    if num < 0:
        print("Incorrect value")
    elif num == 0:
        print(a)
    elif num == 1:
        print(b, end=',')
    else:
        c = a + b
        a = b
        b = c
        print(b,end=',')

print("\nFibonacci Value is :", b)
