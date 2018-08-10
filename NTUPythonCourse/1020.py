money = eval(input("Entry money : "))

caps = money
bottle = money

while caps >= 4:
    bottle += int(caps/4)
    caps = int(caps/4) + caps%4

if caps == 3:
    bottle += 1

print(bottle)




