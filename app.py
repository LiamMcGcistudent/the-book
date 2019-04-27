import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from datetime import date, datetime
from pprint import pprint
from forms import RegistrationForm, LoginForm
import logging

app = Flask(__name__)


if app.debug == True:
    app.secret_key = os.environ.get('SECRET_KEY')
    app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
else:
    app.config["MONGO_DBNAME"]='thebook'
    app.config["MONGO_URI"]='mongodb+srv://liammcg:J43joong@projects-fyjqy.mongodb.net/thebook?retryWrites=true'
    app.config["SECRET_KEY"]='Secret_Key'

mongo = PyMongo(app)


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
    pprint(a_recipe)
    return render_template('recipe.html', recipe=a_recipe)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'logged_in' in 'session':
        return redirect(url_for('index'))
    
    form = RegistrationForm() 
    if form.validate_on_submit():
            
        user = mongo.db.user_information
        dup_user = user.find_one({'name' : request.form['username'].title()})
            
        if dup_user is None:
            user.insert_one({'name' : request.form['username'].title()})
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('index'))
        
        flash('Sorry, username already taken. Please try another.')
        return redirect(url_for('signup'))
                
    return render_template('signup.html', form=form, title="Sign Up")
    
@app.route('/login', methods=['GET', 'POST'])
def user_login():
    """Function for handling the logging in of users"""
    if 'logged_in' in session: #Check is already logged in
        return redirect(url_for('index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = mongo.db.user_information
        logged_in_user = user.find_one({'name' : request.form['username'].title()})
        
        if logged_in_user is None:
            flash('Incorrect username, please try again')
            return redirect(url_for('user_login'))
        session['username'] = request.form['username']
        session['logged_in'] = True
        return redirect(url_for('index'))
        
    return render_template('login.html', form=form, title='Login')
    
@app.route('/logout')
def logout():
    """Logs the user out and redirects to home"""
    session.clear() # Kill session
    return redirect(url_for('index'))
    
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    return render_template('add_recipe.html')
    
@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    
    recipes=mongo.db.recipes
    recipes.insert_one({
    'name' : "My new recipe" , #request.form['recipe-name'] 
    'servings' : "" , 
    'cooking-time': 0, # Always change to int if its need to be int ...
    'categories': [] ,
    'allergens': [],
    'description': "A short explanation of the dish",
    'image' : "",
    'ingredients' : [], # This data further in code will be converted from string to list where "," is separator
    })
    flash('Recipe Added!')
    return redirect(url_for('recipes'))
    
    
    

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'),  debug=True)