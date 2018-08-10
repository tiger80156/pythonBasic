n = int(input())

x = [i for i in range(n,0,-1)]

for item in x:
    print(item)


while x:
    print(x.pop())

