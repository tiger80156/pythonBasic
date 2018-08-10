x = eval(input("Num : "))
y = input("Money : ")
c = eval(input("Num : "))
d = input("Position : ")

y = y.split()
d = d.split()

for i in range(c):
    pos = int(d[i]) - 1
    y[pos] = "0"


maxNum = 0

for i in range(len(y)):
    num = int(y[i])
    if maxNum < num :
        maxNum = num
        maxNumPostion = i+1

print(maxNum)
print(maxNumPostion)



