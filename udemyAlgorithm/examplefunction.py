import pprint
y = [('Hello1','Word'),('Hello2','Gaston'),('Hello3','Jessica')]

newdict = {'key':[],'value':[]}

for item in y:
    newdict['key'].append(item[0])
    newdict['value'].append(item[1])

pprint.pprint(newdict)

