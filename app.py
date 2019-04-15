import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import config
from datetime import date, datetime
from pprint import pprint


app = Flask(__name__)

app.config["MONGO_DBNAME"]=config.CONFIG['MONGO_DBNAME']
app.config["MONGO_URI"]=config.CONFIG['MONGO_URI']
app.config["SECRET_KEY"]=config.CONFIG['SECRET_KEY']

mongo = PyMongo(app)


def recipe_database():
    data = {
        "name": request.form.get('name'),
        "cuisine": request.form.getlist('cuisine'),
        "allergens": request.form.getlist('allergens'),
        "description": request.form.get('description'),
        "ingredients": request.form.getlist('ingredient'),
        "instructions": request.form.getlist('instructions'),
        "serving_size": request.form.get('servings'),
        "image": request.form.get('image'),
        "username": session['user']
    }
    return data

def if_user_in_session():
    username = ""
    if 'user' in session:
        username = session['user']
    return username


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recipes')
def recipes():
    recipes=mongo.db.recipes.find().sort('name', pymongo.ASCENDING)
    return render_template("recipes.html", recipes=recipes, title='Recipes')
    
@app.route('/recipe/<recipe_id>', methods=['GET','POST'])
def recipe(recipe_id):
    
    a_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    pprint(recipe)
    return render_template('recipe.html', recipe=a_recipe)


    

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'),  debug=True)