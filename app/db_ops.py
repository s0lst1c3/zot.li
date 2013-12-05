# imports
from pymongo import MongoClient
from url_key import generate, sanitize, increment

# initializations
client = MongoClient()
db = client.url_db
collection = db.collection

def db_update(rawUrl):
    global collection

    # check if longUrl already in database
    longUrl = sanitize(rawUrl)
    url = collection.find_one({'longUrl':longUrl})
    if url == None:

        # if longUrl is not in database, generate new shortUrl
        shortUrl = generate(longUrl)

        # increment duplicate shortUrls
        while collection.find_one({'shortUrl':shortUrl}) != None:
            shortUrl = increment(shortUrl)
        
        # store the url in the database
        collection.insert({'longUrl':longUrl,'shortUrl':shortUrl})

    else:

        # if longUrl is in database, retrieve shortUrl
        shortUrl = url['shortUrl']

    return shortUrl

def db_retrieve(shortUrl):
    global collection

    # return longUrl only if shortUrl in database
    url = collection.find_one({'shortUrl':shortUrl})
    if url == None:
        return None
    else:
        return url['longUrl']
