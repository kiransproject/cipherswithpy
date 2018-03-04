import E_12_English_detect,E_19_vigenerecipher, E_9A_decrypt_transposition_cipher

# Brute force the vigenere cipher is the key word used is an english word

def main():
    message = E_9A_decrypt_transposition_cipher.fetchmessage()
    key = E_19_vigenerecipher.get_word_key()
    ciphertext = E_19_vigenerecipher.encrypt_mes(message, key)
    
    hackedMessage, hackedkey = bruteForceVig(ciphertext)

    if hackedMessage != None:
        print "the hacked message is: " + hackedMessage + " and the key is: " + hackedkey
    else:
        print "unable to brute force, keyword not stored in reference dictionary"


def bruteForceVig(text):
    words = E_12_English_detect.readfilesplit("dictionary.txt")

    for word in words:
        decryptedText = E_19_vigenerecipher.decrypt_mes(text, word)
        if (E_12_English_detect.isEnglish(decryptedText)):
            print"possible encryption break"
            print 'Key ' + str(word) + ': ' + decryptedText[:100]
            happy = raw_input('English detected, enter D for done or N to continue hacking: ')
            if (happy.strip().upper().startswith('D')):
                return decryptedText, word

if __name__ == '__main__':
        main()
