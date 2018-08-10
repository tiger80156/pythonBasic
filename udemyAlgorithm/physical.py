import csv
output = []
x = ''
y = ''
while y != 'q':
    y = input("Input Topic : ")
    item = [y]

    while x!= 'q':
        x = input("Input Keyword : ")
        item.append(x)
    output.append(item)


out = csv.writer(open("physcial.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
out.writerow(output)



