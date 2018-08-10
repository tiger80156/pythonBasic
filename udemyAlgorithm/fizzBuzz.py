n = eval(input("Please input number : "))

# for i in range(1,n+1):
#     if i%3 is 0 and i%5 is 0:
#         print('bizzFuzz')
    
#     elif i%3 is 0:
#         print('bizz')

#     elif i%5 is 0:
#         print('fuzz')

#     else:
#         print(i)


for i in range(1,n+1):
    x = '' 
    if i%3 is 0:
        x += 'bizz'
    if i%5 is 0:
        x += 'Fuzz'
    if x is '':
        x  = i
    print(x)





    
