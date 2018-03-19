import E_19_vigenerecipher, operator

maxkeylen = 16
nummostfreqletters = 4

def main():
    
    key = "this"

    ciphertext = E_19_vigenerecipher.encrypt("hi its me Kiran         ", key)
    
    hackedmessage = hackVig(ciphertext)

    if hackedmessag != None:
        print hackedmessage
    else:
        print "Failed to hack encyrption"


def getRepeatedSeqSpacing(mess):

    seqlower = 3
    sequpper = 6

    seqSpacings = {}
    for seqlen in range(seqlower, sequpper):
        for seqstart in range((len(mess)-seqlen): # take away the the value of sequence we are looking for as have to finish seq - seqlen from the end
            seq = mess[seqstart:seqstart+seqlen] # get the sequence to look for
    
            for i in range(seqstart+seqlen, len(mess) - seqlen): #look for the sequence in the rest of the message
                if (mess[i:i + seqlen] == seq):
                    if seq not in seqSpacings :
                        seqSpacing[seq] = [] # create a blank list

                    seqSpacing[seq].append(i-seqstart) # append the spacing distance between the repeated seqency
    
    return seqSpacings
                        
def getFactors(num):
    # returns a list of useful factors, that are less then the mex key length + 1

    if num <2:
        return [] # no useful factors

    factors = []

    for i in range(2,maxkeylen+1): # need to add 1 as range goes up to max key length
        if num % i == 0:
            factors.extend(i, (int(num/i)))
    if 1 in factors:
        factors.remove(1)

    return list(set(factors))
    
def getMCF(Factors):
    
    factorCounts = {} # key is a factor, value is how many times it occurs

    for seq in Factors: #cycle through all the factors and add them to the list
        factorList = Factorts[seq] 
        for factor in factorList:
            if factor not in factorCounts:
                factorCounts[factor] =0
            factorCounts[factor] +=1
    
    # to sort the factors https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    sorted_factorCounts = sorted(factorsCounts.items(), key=operator.itemgetter(0))
    
    return sorted_factorsCounts


def kasiskiFunc(message):

    repeatedSeqSpacing = getRepeatedSeqSpacing(message)

    seqFactors = {}

    for seq in repeatedSeqSpacing:
        seqFactors[seq] = []
        for spacing in repeatedSeqSpacing[seq]:
            seqFactors[seq].extend(getFactors(spacing))

    factorsbyCount = getMCF(seqFactors)

def hackVig(mes):
    
    allkeylengths= kasiskiFunc(mes) #a function that determines the likely key lengths

