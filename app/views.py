# imports
import sys, os
from app import app
from flask import request, render_template, redirect
from db_ops import db_retrieve, db_update

URL = 'zot.li/?'

@app.route('/', methods=['POST','GET'])
def index():

    if request.method == 'POST':	

        longUrl = request.form['longUrl']
        shortUrl = db_update(longUrl)

        return render_template('index.html', shortUrl=URL+shortUrl)

    elif request.method == 'GET':

        shortUrl = db_retrieve(request.query_string)
        if shortUrl == None:
            return render_template('index.html',\
                                shortUrl='Your short url will appear here.')
        return redirect(shortUrl)


