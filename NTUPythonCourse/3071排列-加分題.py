def P(n,m):
    a = 1
    for i in range(1,n+1):
        a *= i

    b = 1
    for i in range(1,n-m+1):
        b *= i

    return (a/b)
        
n = eval(input())
m = eval(input())
print(P(n,m))
