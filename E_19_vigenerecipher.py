import E_9A_decrypt_transposition_cipher

#implementation of the vigenere cipher 

length = 128

def main():
    message = E_9A_decrypt_transposition_cipher.fetchmessage()
    key = get_word_key()
    mode = E_9A_decrypt_transposition_cipher.fuctionality()
    if ( mode):
        new_mes =encrypt_mes(message, key) 
        print("Encrypted message is : %s " %new_mes)
        print("Decrypted message is : %s " % decrypt_mes(new_mes, key))
    else:
        print("Decrypted message is : %s " % decrypt_mes(message, key))

def get_word_key():
    return (str(raw_input('enter key : ')))

def encrypt_mes(mes, ke):
    return translateMessage(mes, ke, 'E')

def decrypt_mes(mes, ke):
    return translateMessage(mes, ke, 'D')

def translateMessage(message, key, mode):
    translated = []
    key_in = 0
    for symbol in message:
        h=ord(symbol) # returns ASCII value
        if ( mode == 'E'):
            new_sym = h+ord(key[key_in])
        elif ( mode == 'D'):
            new_sym = h-ord(key[key_in])
    
        if ((new_sym < 0) or (new_sym > length)):
            new_sym %= length # takes care of the wrap around cases where the number is outside of the ascii value range

        translated.append(chr(new_sym))
        
        key_in +=1
        if (key_in == len(key)): #need to check if we need to restart the key 
            key_in =0 

    return ''.join(translated)

if __name__ == '__main__':
    main()
