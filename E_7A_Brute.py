#!/usr/bin/python

nb = raw_input('Text to encrypt or decrypt : ')
chars= list(nb)
length = len(nb)
#key = int(raw_input('enter key length : '))
#kryption = raw_input('Enter E for Encryption or D for Decryption : ')
kryption = 'D'

for key in range(26): #range function specifies to try all keys from 0 upto 26
# so this will then itterate through the possible keys, which are limited to 26 in this case, due to the fact we are not encrypting numbers

    ret = list()
    for k in chars:
        try:
            h=ord(k)
            if (h<65 or (90<h<97) or h>122): #this is if its not a letter, leave it as it is
                k =chr(ord(k))
            else: 
                k = (ord(k)-key)
                if ((k<65) or (h>96 and k<91)or ((90<k<97) and h>96)) :
                    k =chr(k+26)
                elif (k>122 or (h<91 and k>96)or ((90<k<97) and h<91)):
                    k = chr(k-26)
                else:
                    k = chr(k)
        
        
        except ValueError:
            pass
        ret.append(k) #perform operation on one letter at a time (one ascii value) and then append that value to the list ret
    output=''.join(ret) #join together each keys output as a string
    print ('Key #%s: %s' % (key, output)) # the % match the variables listed in the brackets, itterating through them each time
#    print (output) #print that output
