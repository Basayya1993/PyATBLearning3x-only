# ✅ Anagrams String s1 = "silent"; String s2 = "listen"; namo - mano - onam
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase

str1 = input("Enter the String1:")
str2 = input("Enter the String2:")

str3 = sorted(str1)
str4 = sorted(str2)

if str3 == str4:
    print("Both are Anagrams")
else:
    print("Both are not Anagrams")

