import E_9A_decrypt_transposition_cipher

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
    return ((raw_input('enter key : ')))

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
    
        if ((new_sym < 0) or (new_sym > 255)):
            new_sym %= 255

        translated.append(chr(new_sym))
        
        key_in +=1
        if (key_in == len(key)):
            key_in =0

    return ''.join(translated)

if __name__ == '__main__':
    main()
