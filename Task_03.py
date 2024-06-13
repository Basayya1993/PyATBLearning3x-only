# Factorial of Any Number
# Ex: input is n=5! then
# Output is : 5*4*3*2*1= 120 ---> Factorial of 5!

num = int(input("Enter the Value of Fibonacci series:"))  # Made Generic
fact = 1  # As the multiplier starts from value 1

for i in range(1, num + 1):
    fact = i * fact

print(num, "Factorial value is", fact)
