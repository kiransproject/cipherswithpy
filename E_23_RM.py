import random

def rabmiller(num):
    #implementation of the Rab Miller algorithm https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    s = num - 1 
    t = 0 #the number of increments

    while s%2 ==0:
        s = s/2 
        t += 1 # count the number of times we half the value

    for trial in range(5): 
        a = random.randrange(2, num-1)
        v = pow(a, s, num) # a to the power s, mod n
        if v!=1:
            i =0
            while v != (num-1): # if v = num-1 then the number is prime according tot the method/algorithm
                if i == t-1:
                    return False # return False if you reach the number of times you haved halved, meaning that you cant create num anymore
                else: # try the next iteration
                    i +=1
                    v=(v**2)%num # to the power two as we then move up one more in the sequence, same as a^(2s)
    return True # return true if not found to be false with 5 different random numbers

def isprime(num):

    if (num <2):
        return False # 0,1 and ngetaive numbers are not prime

    #about 1/3 of the time we can determine if num is not prime, by dividing by the first few dozen prime numbers, which is quicker then running through rab miller
    
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True

    for prime in lowPrimes:
        if(num%prime ==0):
            return False

    #if all else fails, call rabbin miller, to determine if num is a prime
    return rabmiller(num)


def generateLargePrime(keysize=1024):

    while True:
        num = (random.randrange(2**(keysize-1),2**(keysize)))
        if isprime(num):
            return num
