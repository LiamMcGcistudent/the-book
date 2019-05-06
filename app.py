import os, math
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
    return render_template("index.html", title='Home')

@app.route('/recipes')
def recipes():
    page_limit = 6 #Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipes.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    recipes = mongo.db.recipes.find().sort('_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(page_limit)
    return render_template("recipes.html", recipes=recipes, title='Recipes', current_page=current_page, pages=pages)
    
@app.route('/recipe/<recipe_id>', methods=['GET','POST'])
def recipe(recipe_id):
    
    a_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    pprint(a_recipe)
    return render_template('recipe.html', recipe=a_recipe, title=a_recipe['recipe_name'])

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'logged_in' in 'session':
        return redirect(url_for('index'))
    
    form = RegistrationForm() 
    if form.validate_on_submit():
            
        user = mongo.db.user_information
        dup_user = user.find_one({'name' : request.form['username'].title()})
            
        if dup_user is None:
            user.insert_one({
                'name' : request.form['username'].title(),
                'email': request.form['email'],
                'password' : request.form['password']
            })
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
        logged_in_user = user.find_one({
            'name' : request.form['username'].title(),
            'password' : request.form['password']
        })
        
        if logged_in_user is None:
            flash('Incorrect username or password, please try again')
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
    return render_template('add_recipe.html', title='Add Recipe')
    
@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    
    recipes=mongo.db.recipes
    recipes.insert_one({
        'recipe_name':request.form.get('recipe_name'),
        'recipe_image':request.form.get('recipe_image'),
        'description':request.form.get('description'),
        'instructions':request.form.getlist('instruction'),
        'difficulty':request.form.get('difficulty'),
        'ingredients':request.form.getlist('ingredient'),
        'allergens':request.form.getlist('allergen'),
        'categories':request.form.getlist('category'),
        'cooking_time':(request.form.get('cooking_time')),
        'servings':int(request.form.get('servings'))
    })
    flash('Recipe Added!')
    return redirect(url_for('recipes', title=recipes['recipe_name']))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    #get the recipe that matches the recipe id '_id' is the key 
    recipe = mongo.db.recipes.find_one({'_id':ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe, title='Edit Recipe')

@app.route('/update_recipe/<recipe_id>', methods=["GET", "POST"])
def update_recipe(recipe_id):
    
    recipes = mongo.db.recipes
    
    recipes.update({'_id':ObjectId(recipe_id)},
        #match form fields to keys in the recipes collection
        {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_image':request.form.get('recipe_image'),
        'description':request.form.get('description'),
        'instructions':request.form.getlist('instruction'),
        'difficulty':request.form.get('difficulty'),
        'ingredients':request.form.getlist('ingredient'),
        'allergens':request.form.getlist('allergen'),
        'categories':request.form.getlist('category'),
        'cooking_time':(request.form.get('cooking_time')),
        'servings':int(request.form.get('servings'))
        })
    return redirect(url_for('recipe', recipe_id=recipe_id))
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id':ObjectId(recipe_id)})
    return redirect(url_for('recipes'))
    


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'),  debug=True)