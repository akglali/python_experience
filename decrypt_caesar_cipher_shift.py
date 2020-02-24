string = input('Enter the text that you want to decrypt : ')
string = str.upper(string) # only Work with uppercase letter.

for key in range(1,26):# We have 25 possible shifting operation not including 26.
    print("Key#", key) # get the key (shift) value
    for x in string:
        if(x==' '):
            print(' ',end='') # end use for to not go to next line.
        elif(ord(x)-ord('A')-key<0):
            print(chr(ord(x)-key+26), end='')
        else:
            print(chr(ord(x)-key), end='')
    print(' ')