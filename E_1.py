#!/usr/bin/python

nb = raw_input('Text to encrypt or decrypt : ')
chars= list(nb)
key = int(raw_input('enter key length : '))
kryption = raw_input('Enter E for Encryption or D for Decryption : ')

ret = list()
for k in chars:
    try:
        h=ord(k)
        if (h<65 or (90<h<97) or h>122): #this is if its not a letter, leave it as it is
            k =chr(ord(k))
        else: 
            if (kryption == 'E'):
                k = (ord(k)+key)
                if ((k<65) or (h>96 and k<91)or ((90<k<97) and h>96)) :
                    k =chr(k+26)
                elif (k>122 or (h<91 and k>96) or ((90<k<97) and h<91)):
                    k = chr(k-26)
                else:
                    k = chr(k)
            elif(kryption == 'D'):
                k = (ord(k)-key)
                if ((k<65) or (h>96 and k<91)or ((90<k<97) and h>96)) :
                    k =chr(k+26)
                elif (k>122 or (h<91 and k>96)or ((90<k<97) and h<91)):
                    k = chr(k-26)
                else:
                    k = chr(k)
    
    
    except ValueError:
        pass
    ret.append(k)
output=''.join(ret)

print (output)
