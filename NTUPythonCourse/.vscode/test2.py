x = [1,2,3,4,5]
y = iter(x)

while True:
    try:
        z = next(y)
        print(z)
    except StopIteration:
        break