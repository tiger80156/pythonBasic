# -*- coding: utf8 -*-
itemsA = {"蘋果","香蕉","鳳梨","芭樂"}
itemsB = {"鳳梨","蘋果","水梨","蓮霧"}

a = input()
b = input()
c = input()
d = input()

itemsA.add(a)
itemsA.add(b)
itemsA.remove("蘋果")

itemsB.add(c)
itemsB.add(d)
itemsB.remove("蓮霧")

e = itemsA.intersection(itemsB)
e = list(e)
e.sort()

f = itemsA.difference(itemsB)
f = list(f)
f.sort()

g = itemsB.difference(itemsA)
g = list(g)
g.sort()

h = itemsA.union(itemsB)
h = list(h)
h.sort()

i = itemsA.union(itemsB) - itemsA.intersection(itemsB)
i = list(i)
i.sort()

itemsA = list(itemsA)
itemsA.sort()
itemsB = list(itemsB)
itemsB.sort()

print("iA:",itemsA)
print("iB:",itemsB)
print("union:",h)
print("intersection:",e)
print("A diff B:",f)
print("B diff A:",g)
print("A xor B",i)



