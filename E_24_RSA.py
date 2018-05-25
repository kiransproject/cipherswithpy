import random, sys, os, E_23_RM, cryptomath

def main():
    keysize = fetchsize()
    filename = fetchname()
    makekeyFiles(filename, keysize)

def makekeyFiles(name, key):
    #creates two files x_pubkey and x_privkey where x is defined in named, with n,e and d,e written to file, delimitted by a comma

    if os.path.exists('%s_pubkey.txt' %(name)) or os.path.exists('%s_privkey.txt' % (name)):
        name = name+str(_2)

    pubkey, privkey = genkeys(key)
    
    print('The public key is a %s and a %s digit number.' % (len(str(pubkey[0])), len(str(pubkey[1]))))
    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (key, pubkey[0], pubkey[1]))
    fo.close()

    print('The private key is a %s and a %s digit number.' % (len(str(privkey[0])), len(str(privkey[1]))))
    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (key, privkey[0], privkey[1]))
    fo.close()


def genkeys(key):
    print "Generating two primes"
    p = E_23_RM.generateLargePrime(key)
#    print "p produced"
    q = E_23_RM.generateLargePrime(key)
#    print "q produced"
    n = p*q

    #create a number relatively prime to (p-1)*(q-1), this will be e
    while True:
 #       print "generating...."
        e=random.randrange(2**(key-1), 2**(key)) # create random number e
        if cryptomath.gcd(e, (p-1)*(q-1)) ==1: #check if e relatively prime
            break

    #find the mod inverse
    d = cryptomath.findModInverse(e, ((p-1)*(q-1)))

    pubkey = (n,e)
    privkey = (n,d)

    print ("public key is %s and the private key is %s" % (pubkey, privkey))

    return (pubkey, privkey)


def fetchsize():
    try:
        keys= (int(raw_input('enter key size: ')))
    except:
        keys=1024
        pass
    finally:
        return keys

def fetchname():
    
    try:
        file_name = (raw_input('enter file name: '))
    except:
        file_name='default'+str(random.randint(1,200))
        pass
    finally:
        return file_name
    

if __name__ == '__main__':
    main()
    
    
