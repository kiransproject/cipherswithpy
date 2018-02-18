import E_15_Affine_Cipher, E_12_English_detect, cryptomath, sys, E_9A_decrypt_transposition_cipher

def main():
    
#    mes = "hello 458 this is a message"
#    myMessage =E_15_Affine_Cipher.encrypt(mes, 2032, True)
    myMessage = E_9A_decrypt_transposition_cipher.fetchmessage()
    enc_mes = E_15_Affine_Cipher.encrypt(myMessage, 2192, True) 
    hackedMessage = hackAffine(enc_mes)
#    print( E_15_Affine_Cipher.decrypt(myMessage, 2192, False)) #False sent to determine decryption mode

    if (hackedMessage != None):
        print("decrypted message is: %s " % hackedMessage)
    else:
        print("Failed to decrypt")


def hackAffine(message):
    print("Hacking .....")

    for key in range (0,E_15_Affine_Cipher.ascii_length**2): # ** represents to the power of, its to the power of 2, as same as multiplying by two, as A and B have the same range
        keyA = E_15_Affine_Cipher.getKeySections(key)[0] # 0, only takes the first element, as we just need to check A is valid to speed up the programme
#        print   (E_15_Affine_Cipher.getKeySections(key))
        if ((cryptomath.gcd(keyA, E_15_Affine_Cipher.ascii_length)) != 1):
            continue # if the key is not coprime then continue back at the for loop, i.e. break from currnet iteration but continue onto the next
        
#        print( E_15_Affine_Cipher.decrypt(message, key, False)) #False sent to determine decryption mode

        plaintext = E_15_Affine_Cipher.decrypt(message, key, False) #False sent to determine decryption mode
        
        if (E_12_English_detect.isEnglish(plaintext)):
            print("tried key %s giving plain text : %s " % (key , plaintext))
            happy = raw_input('English detected, enter D for done or N to continue hacking')

            if (happy.strip().upper().startswith('D')):
                    return plaintext

    return None

if __name__ == '__main__':
    main()
