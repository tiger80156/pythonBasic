b = 0

while True:

    a = input()

    if a == "q":
        break
    try:
        a = float(a)%1
    except:
        continue

    b += a
try:
    print (round(b,2))    

except:
    pass
#我不懂為什麼a的值沒辦法加進去b    
        
