a = {"P":"Pikachu","M":"Mickey Mouse","H":"Hello kitty"} 

n = 0
while True:
    n = input()
    
    if n == "-1":
        break
    
    if n in a: #若輸入詞與字典內相符
        print (a[n])
    
    else:
        print (n,"does not exist. Enter a new one:")
        x = input()
        a[n] = x 
