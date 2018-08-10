m = int(input())
n = int(input())

for a in range (1,m+1):
    for b in range (1,n+1):
        c = a*b
        d = "{}*{}={:2d}".format(a,b,c)
        # e += str(c)
        print (d,end=" ")
    print(end = "\n")
        

