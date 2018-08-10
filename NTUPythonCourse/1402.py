personId = input("Please input your person ID : ")

engKey = {'A':10,'J':18,'S':26,'B':11,'K':19,'T':27,
 'C':12,'L':20,'U':28,'D':13,'M':21,'V':29,
 'E':14,'N':22,'W':32,'F':15,'O':35,'X':30,
 'G':16,'P':23,'Y':31,'H':17,'Q':24,'Z':33,
 'I':34,'R':25}

if len(personId) == 10 and personId[0] in engKey:
    y = personId[0]
    x = 0
    x += int(engKey[y.upper()]/10)
    x += (engKey[y.upper()]%10)*9

    for i in range(1,10):
        if i < 8:
            x += int(personId[i]) * (9-i) 
        else:
            x += int(personId[i]) 
    
    if x%10==0:
        print("real")
    else:
        print("fake")

else:
    print("fake")
