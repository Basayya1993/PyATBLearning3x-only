# Palindrome of String i/p = naman , nitin, level,kamak,kayak
# deified, rotator, repaper, deed, peep, wow, noon, civic, racecar, mom ,birdrib
# o/p = true i/p = pramod o/p = false

name = input("Enter the String:")
rev_string = ""

for i in name:
    rev_string = i + rev_string
print("Palindrome of string is:", rev_string == name)
