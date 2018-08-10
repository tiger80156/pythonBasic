x = input("Please entry a string : ")

# rev = ""
# for char in x:
#     rev = char + rev

rev2 = list(x)
rev2.reverse()
rev = "".join(rev2)
print(rev)


