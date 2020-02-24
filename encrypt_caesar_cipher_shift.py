def encrypt(string, shift):
    cipher = ''
    WJHJSYNWFSNFSFYYFHPXTSFRJWNHFSGFSPXGZXNSJXXJXFSILTAJWSRJSYFLJSHNJXMFAJGJJSRTWJJCYJSXNAJYMFSUWJANTZXQDWJUTWYJIITEJSXTKHTWUTWFYNTSXFSIRZQYNUQJZSNYJIXYFYJXFLJSHNJXMFAJGJJSMNYFHHTWINSLYTXJAJSUJTUQJGWNJKJITSYMJJUNXTIJXBMTBJWJSTYFZYMTWNEJIYTINXHZXXYMJRUZGQNHQD
    for char in string:
        if char not in alphabet: # avoiding the punctuation marks and numbers.
            cipher= cipher
        elif char == ' ':
            cipher = cipher + char # avoiding white spaces.
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65) # shifting operation
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher.upper()

alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

text = input("Enter the text that you want to encrypt : ")
s=0
while True :
    try: # if user try to type something else instead of int , exception hepls to not break the program.
        s = int(input("Shift number must be  between 1 to 25: "))
        while (s<0 or s>26): # we have 26 letter in english alphabet. (no meaning 26 of shifting ignore it)
            s = int(input("Shift number must be between 1 to 25: "))
        break
    except ValueError:
        print("You typed invalid character!")

print("original string: ", text.upper()) # You don't have to make it uppercase. It is optional.
print("after encryption: ", encrypt(text, s))

