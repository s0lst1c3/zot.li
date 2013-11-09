# imports
import sys, os

from flask import Flask, request, render_template, redirect, url_for

# initializations
app = Flask(__name__)

# configurations
app.debug = True
URL = '127.0.0.1:5000?'

@app.route('/', methods=['POST','GET'])
def index():

    if request.method == 'POST':

        shortUrl = db_update(request.form['longUrl'])
        return render_template('index.html', shortUrl=URL+shortUrl)

    elif request.method == 'GET':

        shortUrl = db_retrieve(request.query_string)
        if shortUrl == None:
            return render_template('index.html')
        return redirect(shortUrl)
    
if __name__ == '__main__':
    app.run()


