# imports
from pymongo import MongoClient()
from url_key import generate, sanitize, increment

# initializations
client = MongoClient()
db = client.url_db
collection = db.collection

def db_update(rawUrl):
    global collection

    longUrl = sanitize(rawUrl)
    url = collection.find_one({'longUrl':longUrl})
    if url == None:
        shortUrl = generate(longUrl)
        while collection.find_one({'shortUrl':shortUrl}) != None:
            shortUrl = increment(shortUrl)
        
        collection.insert({'longUrl':longUrl,'shortUrl':shortUrl})
    else:
        shortUrl = url['shortUrl']

    return shortUrl

def db_retrieve(shortUrl):
    global collection

    url = collection.find_one({'shortUrl':shortUrl})
    if url == None:
        return None
    else
        return url['shortUrl']
