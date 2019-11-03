
x=input("Please Enter your String:")

x= x.lower()

alphabet= "abcdefghijklmnopqrstuvwxyz"

count={}

for letter in x:
    if letter in alphabet:
        if letter in count:
            count[letter]=count[letter]+1
        else:
            count[letter]=1
key= count.keys()

for letter in sorted(key):
    print (letter,count[letter])


