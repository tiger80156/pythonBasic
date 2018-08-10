string1 = input("Please input string one : ")
string2 = input("Please input string two : ")
stringList1 = []
stringList2 = []
for i in string1.lower():
     if i.isalpha(): stringList1.append(i)
for i in string2.lower():
    if i.isalpha(): stringList2.append(i) 

print(stringList1.sort() == stringList2.sort())





# char1 = list(string1.lower())
# char2 = list(string2.lower())
# result1 = {}
# result2 = {}
# for a in char1:
    # if a.isalpha():
        # result1[a] = result1[a] + 1 if a in result1 else 1 

# for a in char2:
#     if a.isalpha():
#         result2[a] = result2[a]+1 if a in result2 else 1


# print(result1==result2)