def P(n,m):
    for i in range(1,n+1):
        a = 1
        a *= i
    for i in range(1,n-m+1):
        b = 1
        b *= i
    for i in range (1,m+1):
        c = 1
        c *= i
    return (a/(b*c))
        
n = int(input())
m = int(input())
print (P(n,m))
