import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import config
from datetime import date, datetime
from pprint import pprint
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

if app(debug=True):
    app.secret_key = os.environ.get('SECRET_KEY')
    app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
else:
    app.config["MONGO_DBNAME"]=config.CONFIG['MONGO_DBNAME']
    app.config["MONGO_URI"]=config.CONFIG['MONGO_URI']
    app.config["SECRET_KEY"]=config.CONFIG['SECRET_KEY']

mongo = PyMongo(app)


def recipe_database():
    data = {
        "name": request.form.get('name'),
        "category": request.form.getlist('category'),
        "allergens": request.form.getlist('allergens'),
        "description": request.form.get('description'),
        "ingredients": request.form.getlist('ingredient'),
        "instructions": request.form.getlist('instructions'),
        "servings": request.form.get('servings'),
        "difficulty": request.form.get('difficulty'),
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
    doc = recipe_database()
    
    mongo.db.recipes.insert_one(doc)
    id_num = mongo.db.recipes.find_one(
        {'name': request.form.get('name')})
    
    recipe_id = ""
    for key, value in id_num.items():
        if key == "_id":
            recipe_id = ObjectId(value)
    
    return redirect(url_for('recipe', recipe_id=recipe_id))
    

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'),  debug=True)