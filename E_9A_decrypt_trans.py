#!/usr/bin/python

import pdb, math

def main():
    nb = fetchmessage() #fetch the message to encrypt of decrypt
    chars = list(nb) #changes the string of text into an individual list
    key = fetchkey()
    #kryption = fuctionality()
    in_length = len(nb) #defines the length of the string/message
    if (fuctionality()):
        print((method(key,nb, in_length)))
    else:
        print((method_dec(key,nb,in_length)))

def method_dec(key, message, messagelength):
    
    columns = math.ceil((messagelength/(float(key))))
    nb_array = ['']*int(columns)
    rows = key
    shadowboxes = (columns*rows) - messagelength # gives the number of blank boxes
    col =0
    ro=0

    for symbol in message:
        nb_array[col] += symbol
        col += 1
            
        if ((col == columns) or ((col == columns-1) and (ro >= rows-shadowboxes))): #if you reach the final column, reset it and increment the row or if you reach a shadow box
                col =0
                ro +=1

    return ''.join(nb_array)
            
def method(key, message, messagelength):

    new_nb =['']*key #creates multiple columns 

    for j in range(0,(key)):
        i =j
        #covers translating to all columns, cycles through each column, completing it before moving on through the for loop to the next column
        while ( i < messagelength):
            new_nb[j] += message[i]
            i = i +key

    #print new_nb

    #pdb.set_trace() - this is a breakpoint function

    #joins together the columns as a string from a list, the ' ' means join the list together as a string with a space seperating the contents, can change this to an  , or word for example 
    output=''.join(new_nb)
    return output


def fetchmessage():
    input = raw_input('Text to encrypt or decrypt : ')
    return input

def fetchkey():
    return (int(raw_input('enter key length : ')))

def fuctionality():
    function = (raw_input('Enter E for Encryption or D for Decryption : '))
    if (function == 'E'):
        return True
    else:
        return False
        
if __name__ == '__main__':
    main()
