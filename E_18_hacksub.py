import os, E_17_sub_cipher, E_18_makeWordpatt, wordPatterns, copy

if not os.path.exists('wordPatterns.py'):
        makeWordPatterns.main() # create the wordPatterns.py file

def main():
    message = E_17_sub_cipher.encrypt_message('Hi its me just another person that is here, !', 20)
    
    print'Hacking......'
    hackedmessage = hacksub(message)


def getCanditatemap():
    return (dict.fromkeys("{:03}".format(i) for i in range(128))) # returns a dictionary with None as the value https://stackoverflow.com/questions/45465125/initialize-an-empty-dictionary-and-print-to-txt

def hacksub(mess):
    matchedMap = getCanditatemap() # creates a blank map
    cipherwordlist = mes.split() # split the message into a list
    for cipherword in cipherworldlist:
        wordpatt = E_18_makeWordpatt.getWordPattern(cipherword) # get the word pattern for the cipher word
        letmap = getCanditatemap()
        if wordpatt not in wordPatterns.allPatterns:
            continue # Word is not in our dictioniary so continue onto the next word

        for canditate in wordPatterns.allPatterns[wordpatt]: # cycles through the canditates that match the word pattern
            letmap = addLetttoMap(letmap, cipherword, canditate) # adds each candidates letters to the mapping so that we can analyse the pattern

        matchedMap = intersectMap(matchedMap, letmap) #create a central mapping

def letmap(wordMap, ciphword, candidate):

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



