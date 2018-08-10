x = input("Please entry string : ")
x = x.split()
Len = len(x)

if Len%2 == 0:
    for i in range(0,Len,2):
        tem = x[i]
        x[i] = x[Len-i-1]
        x[Len-i-1] = tem

else:
    for i in range(0,int(Len/2)):
        tem = x[i]
        x[i] = x[Len-i-1]
        x[Len-i-1] = tem

print()