from random import randint, seed

def generate(longUrl):

    # create an empty urlKey
    urlKey = []
    
    # seed the random number generator
    seed()

    i = [0, 0, 0]
    for x in range(0,7):
        
        i[0] = randint(48,57)
        i[1] = randint(65,90)
        i[2] = randint(97, 122)
    
        urlKey.append(chr(i[randint(0,2)]))
        
    return ''.join(urlKey)

def sanitize(longUrl):

    if longUrl[:7] != 'http://':
        return 'http://'+longUrl
    return longUrl
