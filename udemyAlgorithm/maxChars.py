x = input("Input a string : ")

repeat = {}


for item in x:
    if item in repeat:
        repeat[item] += 1
    else:
        repeat[item] = 1

maxmum = 0

#Print the most common character
for maxchar in repeat:
    if repeat[maxchar] > maxmum:
        maxmum = repeat[maxchar]
        maxmumchar = maxchar

    elif repeat[maxchar] == maxmum:
        maxmumchar += " " + maxchar

print(maxmumchar)
