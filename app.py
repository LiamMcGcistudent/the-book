import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import config
from datetime import date, datetime
import pytz

app = Flask(__name__)

app.config["MONGO_DBNAME"]=config.CONFIG['MONGO_DBNAME']
app.config["MONGO_URI"]=config.CONFIG['MONGO_URI']
app.config["SECRET_KEY"]=config.CONFIG['SECRET_KEY']

mongo = PyMongo(app)

user_information=mongo.db.user_information
recipe_collection=mongo.db.recipes

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recipes')
def recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
@app.route('/login', methods=['POST'])
def login():
   if request.method == "POST":
        username = request.form['username']

        try:
            user_in_db = user_information.find_one({"username": username})
        except:
            flash("Sorry there seems to be problem with the data")
            return redirect(url_for('index'))
        if user_in_db:
            flash("Logged in as {username}")
            return_url = request.referrer
            return redirect(return_url)
        else:
            flash("Sorry no profile {request.form['username']} found")
            return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'),  debug=True)