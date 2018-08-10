x = input("")

isSpace = True
y = ""

for char in x:
    if isSpace:
        y += char.upper()

    else:
        y += char

    isSpace = False

    if char == " ":
        isSpace = True

print(y)

# x = input("Please input the string : ")

# y = x.split(" ")

# cap = []
# for item in y:
#     cap.append(item[0].upper()+item[1:])

# print(" ".join(cap))


