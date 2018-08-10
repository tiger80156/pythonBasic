score = []
for i in range(5):
    x = input("student {}: ".format(i+1))
    x = x.split()
    score.append(x)

for i in range(5):
    print("student",i)
    for j in range(3):
        print(j,": ",score[i][j])

for i in range(3):
    y = map(int,score[i])
    y = list(y)
    sumScore = sum(y)
    avg = round(sum(y)/len(score[i]),2)
    print(sumScore,"%.2f" % avg)
    
    
