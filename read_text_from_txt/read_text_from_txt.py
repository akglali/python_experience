myfile=open('random.txt','r')

newList=myfile.read().split()
dictionaries={}
print(newList)

for line in newList:
    if line in dictionaries:
        dictionaries[line]=dictionaries[line]+1
    else:
        dictionaries[line]=1
max=0
word=''
for (k,v) in dictionaries.items():
    if max < v:
        max=v
        word=k
print (max)
print (word)


myfile.close()