import enchant, E_11

def main():
    fileContents = readfilesplit("dictionary.txt")
    print '{0:.0f}%'.format(float(lookup(fileContents))/float(len(fileContents))*100)
    

def readfilesplit(filename):
    f = open(filename, "r")
    content ={}#defines as dictionary, as the in function works quicker for checking a dictionary over a list
    content = f.read().splitlines() # read in the variables with each line as an individual item in the dictionary, remvoing the /n in the process
    f.close()
    return content

def lookup(posswords):
    match =0
    d = enchant.Dict("en_GB") #load the GB dictionary
    for  word in posswords:
        if (d.check(word)): #check each value from the list to see if its a word
            match +=1
    return match

if __name__ == '__main__':
        main()
