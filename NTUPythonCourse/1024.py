n = eval(input ("n = "))

x = ""
for l in range(int((2*n-1)/2)):
    x += "-"
for l in range(1):
    x += "*"
for l in range(int((2*n-1)/2)):
    x += "-"
print(x)

i = 1
x = ""

while i < 2*n-3:
    k = 0
    for j in range(3): 
        for l in range(int((2*n-1-k-i)/2)):
            x += "-"
        for l in range(i+k):
            x += "^"
        for l in range(int((2*n-1-k-i)/2)):
            x += "-"
        x += "\n"
        k += 2 

    i += 2   

print(x, end= "")

out = []
x = ""
for i in range(n-2):
    for l in range(int((2*n-4)/2)):
        x += "-"
    for l in range(3):
        x += "#"
    for l in range(int((2*n-4)/2)):
        x += "-"
    if i < n-2:
        x += "\n"

print(x)

