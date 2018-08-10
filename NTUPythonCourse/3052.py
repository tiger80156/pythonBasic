"""
請試著輸入一數字n並印出一高度為n之綾形
*號個數為奇數，每層之星號遞增/減二個
n = 5
  *
 ***
*****
 ***
  *
"""

n = eval(input("Entry a number : "))
x = []

for i in range(n):
    x.append(" ")

y = n//2 + 1

for i in range(y):
    x[y-i:y+1+i] = "*"
    print("".join(x))

# for i in range(1,n+1,2):
#     x += "-"*int((n-i)/2) 
#     x += "*"*i 
#     x += "-"*int((n-i)/2) 
#     x += "\n"

# for i in range(n-2,0,-2):
#     x += "-"*int((n-i)/2) 
    
#     x += "*"*i 
    
#     x += "-"*int((n-i)/2) 
    
#     x += "\n"


print(x)