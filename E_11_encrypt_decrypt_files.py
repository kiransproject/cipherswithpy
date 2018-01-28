#!/usr/bin/python

#encrypting and decrypting files

import time, os, sys, E_10_test_transposition_cipher

def main():
    name = (getFileName())
    fileName =name+str('.txt')
    outputfileName = name+str('_output.txt')
    key = (E_10_test_transposition_cipher.fetchkey())
    if (E_10_test_transposition_cipher.fuctionality()): #functionality defines true for encryption and false for decryption
        writefile(outputfileName, (E_10_test_transposition_cipher.method_enc(key, (readfile(fileName)))))
    else:
        writefile(outputfileName, (E_10_test_transposition_cipher.method_dec(key, (readfile(fileName)))))


def getFileName():
    input = raw_input('Enter the file name to encrypt or decrypt, excluding extension : ')
    if not os.path.exists(input+str('.txt')):
        print ('the file  %s  does not exit, terminating..' %input)
        sys.exit()
    elif os.path.exists((input+str('_output.txt'))):
        print('This will overwrite the file %s ') % (input+str('_output.txt'))
        return input
    else:
        return input

def readfile(filename):
    f = open(filename, "r")
    content = f.read()
    f.close() 
    return content

def writefile(filename, text):
    k = open(filename, "w")
    k.write(text)
    k.close()

if __name__ == '__main__':
    main()


