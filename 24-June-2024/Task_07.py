# Right Triangle Star Pattern n = 5

n = int(input("Enter the Pyramid Value:"))  # Generic
for i in range(n):

    for j in range(i + 1):
        print("*", end=' ')
    print('')

# Reverse Pyramid
for i in range(n, 0, -1):

    for j in range(i - 1):
        print(j, end=' ')
    print('')
