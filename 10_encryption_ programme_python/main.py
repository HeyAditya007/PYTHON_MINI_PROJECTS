# THIS IS SIMPLE ENCRYPTION PROGRAMME IN PYTHON 

import random
import string
#random.shuffle()

characters = " " +  string.punctuation + string.digits + string.ascii_letters
characters = list(characters)
key = characters.copy()
random.shuffle(key)


#print(f"characters : {characters}")
#print(f"key: {key}")


# ENCRYPTION
plain_text = input("enter a message to encryp:  ")
cipher_text = ""

for letter in plain_text:
    index = characters.index(letter)
    cipher_text += key[index]

print(f"original message:  {plain_text}")
print(f"encrypted message:  {cipher_text}")   





# DECRYPTION
cipher_text = input("enter a message to encryp:  ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += characters[index]





print(f"encrypted message:  {cipher_text}")    

print(f"original message:  {plain_text}")
                   
                   