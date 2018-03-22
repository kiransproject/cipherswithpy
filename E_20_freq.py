import getCanditatemap() from E_18_hacksub

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

def getLettercount(mess):

    charcount = getCanditatemap()
    
    for char in mess:
        if char in charcount:
            charcount[char] +=1

    return charcount

def getFreqOrder(mess):

    lettertofreq = getLettercount(mess)

def englishFreqMatch(message):

    freqOrder = getFreqOrder(message)
