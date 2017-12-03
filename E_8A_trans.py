#!/usr/bin/python

import pdb

nb = raw_input('Text to encrypt or decrypt : ')
chars= list(nb)
key = int(raw_input('enter key length : '))
kryption = raw_input('Enter E for Encryption or D for Decryption : ')

in_length = len(nb)


new_nb =['']*key #creates multiple columns 

for j in range(0,(key)):
    i =j
    #covers translating to all columns, cycles through each column, completing it before moving on through the for loop to the next column
    while ( i < in_length):
        new_nb[j] += nb[i]
        i = i +key

#print new_nb

#pdb.set_trace() - this is a breakpoint function

#joins together the columns as a string from a list, the ' ' means join the list together as a string with a space seperating the contents, can change this to an  , or word for example 
output=' '.join(new_nb)

print (output)
