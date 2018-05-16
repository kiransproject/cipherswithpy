import random, sys, os, cyrptomath, E_23_RM

def main():
    keysize = fetchsize()
    filename = fetchname()
    makekeyFiles(filename, keysize)

def makekeyFiles(name, key):
    print "Generating two primes"
    p = E_23_RM.generateLargePrime(key)
    q = E_23_RM.generateLargePrime(key)


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
    


    
    
