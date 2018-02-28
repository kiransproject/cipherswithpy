import os, E_17_sub_cipher, E_18_makeWordpatt, wordPatterns, copy, pprint

# as my encrypt functions encrypts the first 128 ascii characters including spaces, this means that word patterns cannot be recongnised without decrypting spaces, which cannnot be done without working out the word length and where the spaces are located which would make this form of encyrption defunct, so the code has been written but will not work with my encrypt function

if not os.path.exists('wordPatterns.py'):
        makeWordPatterns.main() # create the wordPatterns.py file

def main():
    message = E_17_sub_cipher.encrypt_message('Hi its me just another person that is here, !', E_17_sub_cipher.gen_key())
    
    print'Hacking......'
    mapping= hacksub(message)
    print message
    print " "
    pprint.pprint(mapping)
    print " "
    print decodemessage(mapping, message)


def decodemessage(mapping, mes):
    key  = ['x'] * 128
    for letter in range (128):
        letter = chr(letter)
        if (len(mapping[letter]) == 1):
            keyIndex = ord(mapping[letter][0]) # if one letter add it to the key
            key[keyIndex] = letter
        else:
            mes = mes.replace(letter, '_')
   
    return E_17_sub_cipher.decrypt_message(mes, key)


def getCanditatemap():
    #return (dict.fromkeys(chr(i) for i in range(128))) # returns a dictionary with None as the value https://stackoverflow.com/questions/45465125/initialize-an-empty-dictionary-and-print-to-txt
    dict1 = {}
    for i in range (128):
        dict1[chr(i)] = []
    return dict1

def hacksub(mess):
    matchedMap = getCanditatemap() # creates a blank map
    cipherwordlist = mess.split() # split the message into a list
    print mess
    print cipherwordlist
    for cipherword in cipherwordlist:
        wordpatt = E_18_makeWordpatt.getWordPattern(cipherword) # get the word pattern for the cipher word
        letmap = getCanditatemap()
        if wordpatt not in wordPatterns.allPatterns:
            continue # Word is not in our dictioniary so continue onto the next word

        for canditate in wordPatterns.allPatterns[wordpatt]: # cycles through the canditates that match the word pattern
            letmap = addLetttoMap(letmap, cipherword, canditate) # adds each candidates letters to the mapping so that we can analyse the pattern

        matchedMap = intersectMap(matchedMap, letmap) #create a central mapping

    return removeSolvedLetters(matchedMap)

def removeSolvedLetters(matchmap):
    
    matchedmap = copy.deepcopy(matchmap)
    loop = True
    while loop:
        loop = False # assume we wont need to loop again

        solvedletters = []
        for j in range(128):
            j = chr(j)
            if len(matchedmap[j]) == 1: # if there is only one letter present then we have a match
                solvedletters.append(matchedmap[j][0]) # append match to solved letters


        # if we have determined a mapping we then need to remove it as a possibility from other mappings
        for j in range(128):
            j = chr(j)
            for s in solvedletters:
                if len(matchedmap[j]) !=1 and s in matchedmap[j]:
                    matchedmap[j].remove(s)
                    if len(matchedmap[j]) == 1:
                        loop = True # now need to loop agin as we have solved another

    return matchedmap

def addLetttoMap(wordMap, cipherword, candidate):
    print cipherword
    wordMap = copy.deepcopy(wordMap) # create a copy of wordMap that allows changes without altering the original, see https://www.python-course.eu/deep_copy.php
    for i in range(len(cipherword)):
        if candidate[i] not in wordMap[cipherword[i]]: #if the potential mapping doesnt already exist, create it
            wordMap[cipherword[i]].append(candidate[i])
    return wordMap

def intersectMap(mapA, mapB):
# creates a map containing potential decryption values only if they are in both
    matchMap = getCanditatemap()
    for i in range(128):
        i = chr(i)

        # An empty mapping means any value possible, so copy the other so that when it comes to match its takes the empty dict value into account
        if (mapA[i] == None):
            matchMap[i] = copy.deepcopy(mapB[i])
        elif (mapB[i] == None):
            matchMap[i] = copy.deepcopy(mapA[i])
        else:
             # If the letters in both Maps match add that to the matched mapped
             for mappedletter in mapA[i]:
                 if mappedletter in mapB[i]:
                     matchMap[i].append(mappedletter)
    return matchMap



if __name__ == '__main__':
    main()
