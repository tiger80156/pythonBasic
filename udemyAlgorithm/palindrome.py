char = input("Entry string : ")

length = len(char)
palindrome = True

for a in range(length//2):
    if char[a] != char[length-a-1]:
        palindrome = False  

print(palindrome)
