n = eval(input("number n : "))

#printNum, printStr
printNum = 0
printStr = ""

# n stack 
for i in range(1,n+1):
    #Add number 1~15
    for j in range(i):
        printNum += 1
        printStr += str(printNum)+" "
    printStr += "\n" 

print(printStr)

