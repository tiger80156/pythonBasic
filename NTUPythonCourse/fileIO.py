a = open("test.txt","w")
y = []
x = input().split()

for item in x:
    item = eval(item)

    if item == -1:
        break
        
    y.append(item)
    


for item in y:
    print(item, end = " ")
    a.write(str(item) + " ")

a.close()