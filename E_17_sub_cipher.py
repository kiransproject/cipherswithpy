import sys,  E_9A_decrypt_transposition_cipher, pprint, pdb
from random import shuffle


def main():
    key = gen_key()
    myMessage = E_9A_decrypt_transposition_cipher.fetchmessage()
    mode = E_9A_decrypt_transposition_cipher.fuctionality()
    if (mode):
        enc_mes = (encrypt_message(myMessage, key))
        print"encrypted message is : ", enc_mes
        print"decrypted message is : " ,(decrypt_message(enc_mes, key))

def gen_key():
    x = [i for i in range(128)] # define all 127 values that need mapping between for ASCII
    shuffle(x) # shuffle all values, changing the make up of x in the process, x will not act as our key
#    print x
    return x

def encrypt_message(mes, key):
    return translate(mes, key, 'E')

def decrypt_message(mes, key):
    return translate(mes, key, 'D')

def translate(mes, key, mode):
    translated = ''
    if mode == 'E':
        for symbol in mes:
            symindex = ord(symbol) #take ascii value of symbol
            translated += chr(key[symindex]) #pick the value at symbol index in the key
        return translated
    elif mode == 'D':
#        replace = chr(129)
        for symbol in mes:
            symindex = ord(symbol) 
            '''
            pprint.pprint(key)
            print symindex
            print key[symindex]
            pdb.set_trace()
            '''
#            pprint.pprint(key)
            try:
                keyindex = key.index(symindex) #for decrypt find the index in the key that the symbol is from
                translated += chr(keyindex) #map back
            except:
                pass
        return translated



if __name__ == '__main__':
        main()
