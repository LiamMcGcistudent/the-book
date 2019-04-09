import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import config
from datetime import date, datetime
import pytz

app = Flask(__name__)

app.config["MONGO_DBNAME"]=config.CONFIG['MONGO_DBNAME']
app.config["MONGO_URI"]=config.CONFIG['MONGO_URI']
app.config["SECRET_KEY"]=config.CONFIG['SECRET_KEY']

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recipes')
def recipes():
    recipes=mongo.db.recipes.find().sort('name', pymongo.ASCENDING)
    return render_template("recipes.html", recipes=recipes, title='Recipes')
    
@app.route('/recipe/<recipe_id>', methods=['GET', 'POST'])
def recipe(recipe_id):
    recipes=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipes=recipes, page_title=recipe['name'], recipe_id=recipe_id)




if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'),  debug=True)