# Count vowels and consonants in a String
# Vowels are: a, e, i, o, u .
# Consonants are the rest of the letters in the alphabet:
# b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y and z
# Ramanujan---> a,e,i,o,u

name = input("Enter the String:")

count = 0
for i in name:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count = count + 1
print("Number of Vowels Present in:", name)
print("Vowels:", count)

count = 0
for i in name:
    if i == "b" or i == "c" or i == "d" or i == "f" or i == "g" or \
            i == "h" or i == "j" or i == "k" or i == "l" or i == "m" or i == "n" or i == "o" or i == "p" or i == "q" or i == "r" or \
            i == "s" or i == "t" or i == "u" or i == "v" or i == "w" or i == "x" or i == "y" or i == "z":
        count = count + 1
print("Number of Consonants Present in:", name)
print("Consonants:", count)
