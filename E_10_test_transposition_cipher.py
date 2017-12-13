#!/usr/bin/python
#program to test our decription program and encryption
import pdb, math, os, random, sys

def main():
    random.seed(200)
    numbera = raw_input('attempts: ')
    message_rand(int(numbera))


def message_rand(attempts): #generate a random message and then encrypt and decrypt, ensuring its the same 
    for i in range(attempts):
        message = os.urandom(random.randint(10, 50))
        for key in range(1, len(message)):
            enc = method_enc(key, message)
            dec = method_dec(key, enc)

            if message != dec:
                print('mismatch between encrypted and decrypted message, encyrpted %s and decrypted %s' % (enc, dec))
                sys.exit()
            else:
                print('original: %s encryptede: %s and decrypted: %s' % (message, enc,dec))

    print ("Success")


def method_dec(key, message):
    
    messagelength = len(str((message)))
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
            
def method_enc(key, message):

    messagelength =  len(((message)))
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
