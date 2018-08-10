step = eval(input(""))

for i in range(step):
    
    char = ""

    for c in range(step):
        if c <= i:
            char += "#"
        else:
            char += "_"

    print(char)
