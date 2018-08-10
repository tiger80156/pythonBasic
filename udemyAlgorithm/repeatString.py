#Input the string
string1 = input("Please input string one : ")
string2 = input("Please input string two : ")

x = set(string1)
y = set(string2)

print(x.intersection(y))
print(x.difference(y))

