import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import config
from datetime import date, datetime
import pytz

app = Flask(__name__)

app.config["MONGO_DBNAME"]=config.CONFIG['MONGO_DBNAME']
app.config["MONGO_URI"]=config.CONFIG['MONGO_URI']

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")






if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'),  debug=True)