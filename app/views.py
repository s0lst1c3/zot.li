# imports
import sys, os
from app import app
from flask import request, render_template, redirect
from db_ops import db_retrieve, db_update

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


