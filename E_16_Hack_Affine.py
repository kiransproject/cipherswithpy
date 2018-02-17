import E_15_Affine_Cipher, E_12_English_detect, cryptomath, sys

def main():
    
    #myMessage = """U&'<3dJ^Gjx'-3^MS'Sj0jxuj'G3'%j'<mMMjS'g{GjMMg9j{G'g"'gG '<3^MS'Sj<jguj'm'P^dm{'g{G3'%jMgjug{9'GPmG'gG'-m0'P^dm{LU'5&Mm{'_^xg{9"""
    mes = "hello 458 this is a message"
    myMessage =E_15_Affine_Cipher.encrypt(mes, 2032, True)
    
    hackedMessage = hackAffine(myMessage)

    if (hackedMessage != None):
        print("decrypted message is: %s " % hackedMessage)
    else:
        print("Failed to decrypt")


def hackAffine(message):
    print("Hacking .....")

    for key in range (E_15_Affine_Cipher.ascii_length ** 2): # ** represents to the power of, its to the power of 2, as same as multiplying by two, as A and B have the same range
        keyA = E_15_Affine_Cipher.getKeySections(key)[0] # 0, only takes the first element, as we just need to check A is valid to speed up the programme
        if ((cryptomath.gcd(keyA, E_15_Affine_Cipher.ascii_length)) != 1):
            continue # if the key is not coprime then continue back at the for loop, i.e. break from currnet iteration but continue onto the next

        plaintext = E_15_Affine_Cipher.decrypt(message, key, False) #False sent to determine decryption mode
#        print key

#        if (key == 2032):
 #           print("tried key giving plain text : " ,plaintext[:50])
 #          print(plaintext)
            #if key > 3000:
           # sys.exit();
        
        if (E_12_English_detect.isEnglish(plaintext)):
            print("tried key %s giving plain text : %s " % (key , plaintext))
            happy = raw_input('English detected, enter D for done or N to continue hacking')

            if (happy.strip().upper().startswith('D')):
                    return plaintext

    return None

if __name__ == '__main__':
    main()
