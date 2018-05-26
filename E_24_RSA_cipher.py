import sys, E_24_RSA, E_23_RM, os, random, E_9A_decrypt_transposition_cipher

BLOCKSIZE = 128
BYTESIZE = 256

def main():

    mode = E_9A_decrypt_transposition_cipher.fuctionality()
    filename = getFilename(mode)

    if (mode):
        message = E_9A_decrypt_transposition_cipher.fetchmessage()
        print 'Encrypting and writing to %s...' % (filename)
        Encrypted = encrypt(filename, getpfile(),message)

        print 'Encrypted text is ' + Encrypted
    else:
        print('Reading from %s and decrypting...' % (filename))
        Decrypted = decrypt(filename, getpfile())

        print 'Decrypted text is ' + Decrypted

def decrypt(filen, privkey):
    keysize, n,d = readkeyfile(privkey)

    fo = open(filen)
    content=fo.read()
    messLen, blocksize, encryptedmess = content.split('_')
    messLen = int(messLen)
    blocksize = int(blocksize)

    if keysize < blocksize*8:
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size. Did you specify the correct key file and encrypted file?' % (blocksize * 8, keysize))

    encryptedblocks = map(int,encryptedmess.split(',')) #map string array back to integer array
    
    return decryptblocks(encryptedblocks, messLen,n,d,blocksize)

def decryptblocks(encblocks, messlen, n,d, size):
    
    #decryptedblocks = map(pow, encblocks,d,n)
    decryptedblocks = [pow(block,d,n) for block in encblocks]
    return gettextfromblocks(decryptedblocks, messlen, size)

def gettextfromblocks(blockints,messLen, blocksize):
    #converts back from a list of block integers to the original message string

    message=[]
    for blockint in blockints:
        blockmess = []
        for i in range(blocksize-1,-1,-1):
            if (len(message) +i <messLen):#check that you are still decoding the message and not stretched over
                asciiNumber = blockint // (BYTESIZE**i) # do opposite of block encoding, to get the ascii value again
                blockint = blockint % (BYTESIZE**i) #this decrements the current blockint for the next iteration, as we have no decoded it , with the mod used to calculate the remainder
                blockmess.insert(0,chr(asciiNumber)) #this inserts at the beginning of the message as we are working bacwards
        message.extend(blockmess)
    return ''.join(message)

def getFilename(mode):
        
    input = raw_input('Enter the file name to read or write to, including extension : ')
    if (not mode) and (not os.path.exists(input)):
        print ('the file  %s  does not exit, terminating..' %input)
        sys.exit()
    elif (mode) and (os.path.exists(input)):
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
    
    messageBytes = bytearray(message) # maps the message to a byte array, which if listed shows the individual ascii values, can use encode for python3 i think, https://stackoverflow.com/questions/27657570/how-to-convert-bytearray-with-non-ascii-bytes-to-string-in-python

    blockints= []
    for blockstart in range(0,len(messageBytes), BLOCKSIZE):
        #calculate the block integer for this block of text, with the for loop iterating over the entire message each blocksize at a time
        blockint =0
        for i in range(blockstart, min(blockstart+BLOCKSIZE, len(messageBytes))): # the range in this case checks whether we are at the end of the byte message
                blockint +=messageBytes[i]*(BYTESIZE**(i%BLOCKSIZE)) # gives the position relative to the blocksize , i.e i is the position in the overall message, by multiplying by the byte size (256^(i mod 128)) - as 128 is the blocksize it will give you relative the position in the block, multiplying the ascii value by the bytesize ^ position is the way RSA translates ascii characters into large values ready to encrypt
        blockints.append(blockint) # add the block integers to the array of all block integers
    return blockints
    

def encBLOCKS(message, n,e):
    encryptedBLOCKS = [] 

    for block in getBlocksFromText(message):
       encryptedBLOCKS.append(pow(block,e,n)) # encrypt the block using (block**e) mod n, using pow is more efficient for larger integers
    return encryptedBLOCKS


def encrypt (filen, pkeyname, message):

    keysize, n,e = readkeyfile(pkeyname)

    if keysize < BLOCKSIZE*8:
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size. Either increase the block size or use different keys.' % (blockSize * 8, keySize))

    encryptedBlocks = encBLOCKS(message, n,e)
    
    encryptedBlocksSTR = ','.join(map(str, encryptedBlocks))#converts the integer array to an individual string array using map and then joins it all together as one string, seperate by commas

    encryptedContent = '%s_%s_%s' % (len(message), BLOCKSIZE, encryptedBlocksSTR)
    fo = open(filen, 'w')
    fo.write(encryptedContent)
    fo.close()

    return encryptedContent

if __name__ == '__main__':
    main()
