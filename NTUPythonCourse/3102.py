n = eval(input("input a number : "))


for isPrime in range(2,n+1):
    primeFlag = True
    for test in range(2,isPrime):
        if isPrime % test == 0:
            primeFlag = False
    
    if primeFlag:
        print(isPrime, "is prime")
    