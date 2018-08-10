ans = input("Please entry answer: ")

guess = input("Please entry guess: ")

a = 0
for i in guess:
    if i in ans:
        a += 1 

b = 0
for i in range(len(guess)):
    if ans[i] == guess[i]:
        b += 1

print(a-b,"A",b,"B", sep = "")
