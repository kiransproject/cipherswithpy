import enchant, E_11_encrypt_decrypt_files
#detecting english

def main():
    output()

def output():
    fileContents = readfilesplit("dictionary.txt")
    print '{0:.0f}%'.format(float(lookup(fileContents))/float(len(fileContents))*100) #prints the percentage of words in the file that are english words


def readfilesplit(filename):
    f = open(filename, "r")
    content ={}#defines as dictionary, as the in function works quicker for checking a dictionary over a list
    content = f.read().splitlines() # read in the variables with each line as an individual item in the dictionary, remvoing the /n in the process
    f.close()
    return content

def splitmessage(message):
    mes = {}
    mes = message.split() # splits on space instead of line
    return mes

def isEnglish(messa):
    message = splitmessage(messa)
    try :
        if ((float(lookup(message)/float(len(message))*100)) > 80):
            return True
        else:
            return False
            
    except:
        pass
    return False

def lookup(posswords):
    match =0
    d = enchant.Dict("en_GB") #load the GB dictionary
    for  word in posswords:
        if (d.check(word)): #check each value from the list to see if its a word
            match +=1
    return match

if __name__ == '__main__':
        main()
