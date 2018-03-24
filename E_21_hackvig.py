import E_19_vigenerecipher, operator, collections, pdb, E_20_freq, E_12_English_detect

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
        nthLetter = getnthsubkeyletters(nth, keylen, message)

        freqScores = []
        for possiblkey in range (ASCIILEN):
            pk = chr(possiblkey) # convert to ascii character
            decryptedtext = E_19_vigenerecipher.decrypt_mes(message, pk)
            freqScores.append((pk, E_20_freq.englishFreqMatch(decryptedtext))) # append a tuple containing the key and the score relating to the english frequency match

        sorted_freqscores = sorted(freqScores.items(), key=operator.itemgetter(1), reverse=True) #sort by english freq matcher score
        
        allfreqscores.append(sorted_freqscores[:nummostfreqletters])
    
    if (PRINT):
        for i in range(len(allfreqscores)):
            print "possible letters for letter %s of the key: " %(i+1) # add one , so we dont start at 0
            for freqscore in allfreqscores[i]: # the above is cycling through letter posistion, we are now cycling through the possible mappings
                print("%s " %freqscore[0])
            print"\n"

    #try every combination of the most likely letters for each posistion
    for indexes in itertools.product(range(nummostfreqletters), repeat=keylen):# produces all possible every possible combination of items in a list or list-like value, such as a string or tuple, i.e. if the range is 8 and repeat =5, it creates all possible 5 digit combinations using 0 and 8 i,e 0,0,0,0,0 to 7,7,7,7,7
        posskey = ""
        for i in range (keylen):
            posskey += allfreqscores[i][indexes[i]][0] # cycle through all possible keys

        if (PRINT):
            print"attempting with key: %s" %posskey

        decrypttext =E_19_vigenerecipher.decrypt_mes(message, posskey)

        if (E_12_English_detect.isEnglish(message)):
            print "english detected using %s as a key, %s" %(posskey,decypttext[:500])
            response = raw_input("enter D if correct or enter to continue:")
            if (respnse.upper()[0] == 'd'):
                return decrypttext

    return None



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
        #pdb.set_trace()

    if hackedmessage == None:
        print "unable to hack message with likely key lengths, brute force key length"

        for keylen in range(1,maxkeylen+1):
            if keylen not in allkeylenghts:# dont recheck kasiski checked lengths
                print"attempting hack with key length %s (%s possible keys) " %(keylen, nummostfreqletters**keylen)
                hackedmessage = attempthackwithkeylength(mes, keylen)
                if hackmessage != None:
                    break

    return hackedmessage

if __name__ == '__main__':
    main()
