import random, sys, os, cyrptomath, E_23_RM

def main():
    keysize = fetchsize()
    filename = fetchname()

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
        file_name='default'+
        pass
    finally:
        return file_name
    


    
    
