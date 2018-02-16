# Affine Ciphea

import  E_9A_decrypt_transposition_cipher, cryptomath, sys

ascii_length = 128 #127 is the final value startinga at 0

def main():
    nb = E_9A_decrypt_transposition_cipher.fetchmessage()
    key =E_9A_decrypt_transposition_cipher.fetchkey()
    mode =E_9A_decrypt_transposition_cipher.fuctionality() 
    if (mode):
        mes = encrypt(nb, key, mode)
        print ("encrypted text is: %s" % mes)
        print("decrypted text is: %s" % decrypt(mes,key, False))
    else:
        print("decrypted text is: %s " % decrypt(nb, key, mode))


def getKeySections(kys):
    keyA = kys // ascii_length #gives integer division 
    keyB = kys % ascii_length #gives remaninder 
    return (keyA, keyB)

def encrypt(message, kys, mode):
    KeyA, KeyB = getKeySections(kys)
    checkKeys(KeyA, KeyB, mode)
    ciphertext = ''
    for symbol in message:
        ciphertext += chr(((ord(symbol) * KeyA)+KeyB) % ascii_length)
    return ciphertext

def checkKeys(key1, key2, mode):
    if ((mode) and (key1 == 1)):
        sys.exit('The affine cipher becomes incredibly weka when A is set to 1. Chose a different key.')
    if ((mode) and (key2 == 0)):
        sys.exit('The affine cipher becomes incredibly weka when B is set to 0. Chose a different key.')
    if ( key1< 0 or key2 <0 or key2> (ascii_length-1)):
        sys.exit(' Key A and B must be greater than 0 and key B must be less than %s ' % (ascii_length-1))
    if (cryptomath.gcd(key1, ascii_length) != 1):
        sys.exit(' Key A and the symbol set size %s are not relatively prime ' % ascii_length)

def decrypt(message, kys, mode):
    KeyA, KeyB = getKeySections(kys)
    checkKeys(KeyA, KeyB, mode)
    inveseA = cryptomath.findModInverse(KeyA, ascii_length) #finds the inverse of the key A
    plaintext = ''
    for symbol in message:
        plaintext += chr(((ord(symbol) -KeyB) *inveseA) % ascii_length)
    return plaintext
    

if __name__ == '__main__':
    main()
