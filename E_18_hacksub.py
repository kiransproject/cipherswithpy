import os, E_17_sub_cipher, E_18_makeWordpatt, wordPatterns, copy, pprint, collections, pdb, E_9A_decrypt_transposition_cipher

# the message gets decrypted without any spaces included and doesnt map well, as it takes the full ascii set so too many variables, also cant map something to show it cant be decrypted , as replace wont work without a valid char, in text output you should be able to see bits of teen and what not, could add a function that records the spaces so where it was split and reinserts them

length = 128

if not os.path.exists('wordPatterns.py'):
        makeWordPatterns.main() # create the wordPatterns.py file

def main():
    k = E_17_sub_cipher.gen_key()
    #message = E_17_sub_cipher.encrypt_message("here is a lot of words that hopefully are within the file that has been provided to me in the form of a dictionary HELLO ITS ME KIRAN ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN ELEVENT TWELVE THIRTEEN FOURTEEN FIFTEEN ONCE I CAUGHT A FISH             ALIVE SIX SEVEN EIGHT NINE TEN THEN WE LET HIM GO AGAIN WHY DID YOU LET HIM GO BECAUSE HE BIT MY FINGER SO WHICH LITTLE FINGER DID HE BITE THIS LITTLE FINGER ON MY RIGHT                                                                                                                                                                                                                                                         ", k)
    message = E_9A_decrypt_transposition_cipher.fetchmessage()

    mostFreq = (collections.Counter(message).most_common(1)[0][0]) # find the most frequent symbol, we are going to assume this is a space
    print'Hacking......'
    mapping= hacksub(message, mostFreq)
    mapping[ord(" ")].append(mostFreq)
    
    print message
    print " "
    pprint.pprint(mapping)
    print " "
    print decodemessage(mapping, message, mostFreq)

def decodemessage(mapping, mes, mostFreq):
    translated = ''
    key  = [ord(mostFreq)] * length
    for num in range (length):
        if (len(mapping[num]) == 1):
            letter = ord(mapping[num][0]) # if one letter add it to the key
            key[letter] = num
        
        else: # else replace that letter in the message with a space
            mes = mes.replace(chr(num), mostFreq)
    ''' 
    print(set(key))
    print(mes)
    pdb.set_trace()
    '''

    for symbol in mes:
        symindex = ord(symbol)
        try:
            keyindex = key.index(symindex) #for decrypt find the index in the key that the symbol is from
            translated += chr(keyindex) #map back
        except:
            translated += chr(key.index(ord(mostFreq)))
    
    return translated 

def getCanditatemap():
    #return (dict.fromkeys(chr(i) for i in range(length))) # returns a dictionary with None as the value https://stackoverflow.com/questions/45465125/initialize-an-empty-dictionary-and-print-to-txt
    dict1 = {}
    for i in range (length):
        dict1[i] = []
    return dict1

def hacksub(mess, MFreq):

    matchedMap = getCanditatemap() # creates a blank map
    cipherwordlist = mess.split(MFreq) # split the message into a list
    for cipherword in cipherwordlist:
        wordpatt = E_18_makeWordpatt.getWordPattern(cipherword) # get the word pattern for the cipher word
        letmap = getCanditatemap()

        if wordpatt not in wordPatterns.allPatterns:
            continue # Word is not in our dictioniary so continue onto the next word

        for canditate in wordPatterns.allPatterns[wordpatt]: # cycles through the canditates that match the word pattern, only returns capital letters though but shouldnt make any difference 
            letmap = addLetttoMap(letmap, cipherword, canditate) # adds each candidates letters to the mapping so that we can analyse the pattern
 #           print letmap
        '''
        pprint.pprint(matchedMap)
        pdb.set_trace()
        '''
        matchedMap = intersectMap(matchedMap, letmap) #create a central mapping
        
    ''' 
    pprint.pprint(matchedMap)
    pdb.set_trace()
    pprint.pprint(removeSolvedLetters(matchedMap))
    pdb.set_trace()
    '''


    return removeSolvedLetters(matchedMap)

def removeSolvedLetters(matchmap):
    
    matchedmap = copy.deepcopy(matchmap)
    loop = True
    while loop:
        loop = False # assume we wont need to loop again

        solvedletters = []
        for j in range(length):
            #j = chr(j)
            if len(matchedmap[j]) == 1: # if there is only one letter present then we have a match
                solvedletters.append(matchedmap[j][0]) # append match to solved letters


        # if we have determined a mapping we then need to remove it as a possibility from other mappings
        for j in range(length):
            #j = chr(j)
            for s in solvedletters:
                if len(matchedmap[j]) !=1 and s in matchedmap[j]:
                    matchedmap[j].remove(s)
                    if len(matchedmap[j]) == 1:
                        loop = True # now need to loop agin as we have solved another

    return matchedmap

def addLetttoMap(wordMap, cipherword, candidate):
    wordMap = copy.deepcopy(wordMap) # create a copy of wordMap that allows changes without altering the original, see https://www.python-course.eu/deep_copy.php
    for i in range(len(cipherword)):
        '''
        print candidate[i]
        print wordMap
        print cipherword[i]
        print wordMap[ord(cipherword[i])]
        '''
        if candidate[i] not in wordMap[ord(cipherword[i])]: #if the potential mapping doesnt already exist, create it
            wordMap[ord(cipherword[i])].append(candidate[i])
            #print wordMap[cipherword[i]]
    return wordMap

def intersectMap(mapA, mapB):
# creates a map containing potential decryption values only if they are in both
    matchMap = getCanditatemap()
    '''
    pprint.pprint(mapA)
    pprint.pprint(mapB)
    
    pdb.set_trace()
    '''
    for i in range(length):
        #i = chr(i)

        # An empty mapping means any value possible, so copy the other so that when it comes to match its takes the empty dict value into account
        if (mapA[i] == []) :
            matchMap[i] = copy.deepcopy(mapB[i])
        elif (mapB[i] == [] ):
            matchMap[i] = copy.deepcopy(mapA[i])
        else:
             # If the letters in both Maps match add that to the matched mapped
             for mappedletter in mapA[i]:
                 if mappedletter in mapB[i]:
                     matchMap[i].append(mappedletter)
    return matchMap



if __name__ == '__main__':
    main()
