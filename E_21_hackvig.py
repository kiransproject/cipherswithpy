import E_19_vigenerecipher, operator, collections, pdb

maxkeylen = 16
nummostfreqletters = 4
PRINT = True
ASCIILEN = 128

def main():
    
    key = "this"

    ciphertext = E_19_vigenerecipher.encrypt_mes("hi its me Kiran         ", key)
    
    hackedmessage = hackVig(ciphertext)

    if hackedmessag != None:
        print hackedmessage
    else:
        print "Failed to hack encyrption"

def mostCommonLetter(mess): # returns the most common character, which we will assume is a space
    return (collections.Counter(mess).most_common(1)[0][0])


def getRepeatedSeqSpacing(mess):

    seqlower = 3
    sequpper = 6

    seqSpacings = {}
    for seqlen in range(seqlower, sequpper):
        for seqstart in range(((len(mess))-seqlen)): # take away the the value of sequence we are looking for as have to finish seq - seqlen from the end
            seq = mess[seqstart:seqstart+seqlen] # get the sequence to look for
    
            for i in range(seqstart+seqlen, len(mess) - seqlen): #look for the sequence in the rest of the message
                if (mess[i:i + seqlen] == seq):
                    if seq not in seqSpacings :
                        seqSpacings[seq] = [] # create a blank list

                    seqSpacings[seq].append(i-seqstart) # append the spacing distance between the repeated seqency
    
    return seqSpacings
                        
def getFactors(num):
    # returns a list of useful factors, that are less then the mex key length + 1

    if num <2:
        return [] # no useful factors

    factors = []

    for i in range(2,maxkeylen+1): # need to add 1 as range goes up to max key length
        if num % i == 0:
            factors.extend([i,(int(num/i))])
    if 1 in factors:
        factors.remove(1)

    return list(set(factors))
    
def getMCF(Factors):
    
    factorCounts = {} # key is a factor, value is how many times it occurs

    for seq in Factors: #cycle through all the factors and add them to the list
        factorList = Factors[seq] 
        for factor in factorList:
            if factor not in factorCounts and factor <= maxkeylen:
                factorCounts[factor] =0
            factorCounts[factor] +=1
    
    # to sort the factors https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    sorted_factorCounts = sorted(factorCounts.items(), key=operator.itemgetter(0), reverse=True)
    
    return sorted_factorCounts


def kasiskiFunc(message):

    repeatedSeqSpacing = getRepeatedSeqSpacing(message)

    seqFactors = {}

    for seq in repeatedSeqSpacing:
        seqFactors[seq] = []
        for spacing in repeatedSeqSpacing[seq]:
            seqFactors[seq].extend(getFactors(spacing))

    factorsbyCount = getMCF(seqFactors) #get the most common factors

    # get a list of the factors
    likelykeylengths = []
    for item in factorsbyCount:
        likelykeylengths.append(item[0])

    return likelykeylengths

def getnthsubkeyletters(num, keylength, message): #seperate the cipher text into seperate streams, with the number of streams based on the keylength
    
    chars = []
    for i in xrange (0,len(message),keylength): # use xrange to define step size https://stackoverflow.com/questions/2990121/how-do-i-loop-through-a-list-by-twos
        chars.append(message[i])

    return ''.join(chars)

def attempthackwithkeylength(message, keylen):
    
    allfreqscores = []
    for nth in range(1, keylen+1):
        nthLetter = getnthsubkeyletters(nth, keylen, message)A

        freqScores = []
        for possiblkey in range ASCIILEN:
            pk = chr(possiblkey) # convert to ascii character
            decryptedtext = E_19_vigenerecipher.decrypt_mes(message, pk)
            


def hackVig(mes):
    
    allkeylengths= kasiskiFunc(mes) #a function that determines the likely key lengths
    if (PRINT):
        print "The following key lengths are being tried: %s " %allkeylengths
    
    for keylength in allkeylengths:
        if (PRINT):
            print "Attempting hack with key length %s (%s possible keys)..." % (keylength,nummostfreqletters**keylength)   # ** represents to the power of
        hackedmessage = attempthackwithkeylength(mes, keylength)
        if hackedmessage != None:
            break
        pdb.set_trace()

if __name__ == '__main__':
    main()
