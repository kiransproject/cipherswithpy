import E_9A_decrypt_transposition_cipher, E_12_English_detect

def main():
    message = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn""" # triple quoutes allows quotes within
    possibleOutput = brutetranspos(message)

    if possibleOutput == None:
        print 'Failed to brute force'
    else:
        print possibleOutput

def brutetranspos(mes):
    print 'Hacking...'

    for key in range(1, len(mes)): #try all possible keys
        print('Attempting key #%s' %key)

        decryptText =E_9A_decrypt_transposition_cipher.method_dec(key,mes, len(mes))
        
        #print decryptText

        if E_12_English_detect.isEnglish(decryptText):
            print('Possible hack: \n key %s: %s' %(key, decryptText[:100]))
            response = raw_input('\n Enter D for done or any other key to continue:')
            #response = input('> ')

            if response.strip().upper().startswith('D'): #stip removes any whitespace before or after, equating to tabs, newlines and spaces
                return decryptText
    

    return None

if __name__ == '__main__':
     main()

