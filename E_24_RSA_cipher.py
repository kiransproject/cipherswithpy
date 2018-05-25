import sys, E_24_RSA, E_23_RM, os, random, E_9A_decrypt_transposition_cipher

BLOCKSIZE = 128

def main():

    filename = getFilename()
    mode = E_9A_decrypt_transposition_cipher.fuctionality()

    if (mode):
        message = E_9A_decrypt_transposition_cipher.fetch_message()
        print 'Encrypting and writing to %s...' % (filename)
        Encrypted = encrypt(filename, getpfile(),message)

        print 'Encrypted text is ' + Encrypted
    else:
        print('Reading from %s and decrypting...' % (filename))
        Decrypted = decrypt(filename, getpfile())

        print 'Decrypted text is ' + Decrypted

def getFilename():
        
    input = raw_input('Enter the file name to read or write to, including extension : ')
    if not os.path.exists(input):
        print ('the file  %s  does not exit, terminating..' %input)
        sys.exit()
    elif os.path.exists(input):
        print('This will overwrite the file %s ') % (input)
        return input
    else:
        return input

def getpfile():
    input = raw_input('Enter the public or private key file name to read from, including extension : ')
    if not os.path.exists(input):
        print ('the file  %s  does not exit, terminating..' %input)
        sys.exit()
    else:
        return input

def readkeyfile(pkey):
    fo = open(pkey)
    content = fo.read()
    fo.close()
    keysize, n, e = content.split(',')

    return (int(keysize), int(n), int(e))

def getBlocksFromText(message):



def encryptBLOCKS(message, n,e):
    encryptedBlocks = [] 

    for block in getBlocksFromText(message):


def encrypt (filen, pkeyname, message):

    keysize, n,e = readkeyfile(pkeyname)

    if keysize < BLOCKSIZE*8:
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size. Either increase the block size or use different keys.' % (blockSize * 8, keySize))

    encryptedBlocks = encBLOCKS(message, n,e)
