import os
import math
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from pprint import pprint
from forms import RegistrationForm, LoginForm


app = Flask(__name__)


app.secret_key = os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)


def if_user_in_session():
    username = ""
    if 'username' in session:
        username = session['username']
    return username

#Route logic for login process
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def user_login():
    """Function for handling the logging in of users"""
    if 'logged_in' in session:  # Check is already logged in
        return redirect(url_for('recipes'))

    form = LoginForm()

    if form.validate_on_submit():
        user = mongo.db.user_information
        logged_in_user = user.find_one({
            'username': request.form['username'].title(),
            'password': request.form['password']
        })

        if logged_in_user is None:
            flash('Incorrect username or password, please try again')
            return redirect(url_for('user_login'))
        session['username'] = request.form['username']
        session['logged_in'] = True
        return redirect(url_for('recipes'))

    return render_template('login.html', form=form, title='Login')

#Logic for sign up
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'logged_in' in 'session':
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():

        user = mongo.db.user_information
        dup_user = user.find_one(
            {'username': request.form['username'].title()})

        if dup_user is None:
            user.insert_one({
                'username': request.form['username'].title(),
                'email': request.form['email'],
                'password': request.form['password']
            })
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('recipes'))

        flash('Sorry, username already taken. Please try another.')
        return redirect(url_for('signup'))

    return render_template('signup.html', form=form, title="Sign Up")

#Logic for logout
@app.route('/logout')
def logout():
    """Logs the user out and redirects to home"""
    session.clear()  # Kill session
    return redirect(url_for('user_login'))

#Logic for retrieving and displaying recipes from the database
@app.route('/recipes', methods=['POST', 'GET'])
def recipes():
    #Credit to Shane Muirhead, a student at Code Institute, for this pagination code
    page_limit = 6  # Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipes.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    recipes = mongo.db.recipes.find().sort(
        'name', pymongo.ASCENDING).skip(
        (current_page - 1) * page_limit).limit(page_limit)
    return render_template(
        "recipes.html",
        recipes=recipes,
        title='Recipes',
        current_page=current_page,
        pages=pages)

#Displays a single recipe from the database
@app.route('/recipe/<recipe_id>', methods=['GET', 'POST'])
def recipe(recipe_id):

    a_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    pprint(a_recipe)
    return render_template(
        'recipe.html',
        recipe=a_recipe,
        title=a_recipe['name'])

#Renders the form for adding recipes
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    return render_template('add_recipe.html', title='Add Recipe')

#Inserts the new recipe in to the database
@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():

    recipes = mongo.db.recipes
    if request.method == "POST":
        recipes.insert_one({
            'name': request.form.get('name'),
            'image': request.form.get('image'),
            'description': request.form.get('description'),
            'instructions': request.form.getlist('instruction'),
            'difficulty': request.form.get('difficulty'),
            'ingredients': request.form.getlist('ingredient'),
            'allergens': request.form.getlist('allergen'),
            'categories': request.form.getlist('category'),
            'cooking_time': (request.form.get('cooking_time')),
            'servings': int(request.form.get('servings')),
            'author': session['username']
        })
        flash('Recipe Added!')
        return redirect(url_for('recipes', title=recipes['name']))

#Brings up a form template that shows the current information of a
#recips and allows the user to edit it
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    # get the recipe that matches the recipe id '_id' is the key
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template(
        "edit_recipe.html",
        recipe=recipe,
        title='Edit Recipe')

#Submits the new information to the database and updates the
#specified recipe by its id
@app.route('/update_recipe/<recipe_id>', methods=["GET", "POST"])
def update_recipe(recipe_id):

    recipes = mongo.db.recipes
    if request.method == "POST":
        recipes.update({'_id': ObjectId(recipe_id)},
                       # match form fields to keys in the recipes collection
                       {
            'name': request.form.get('name'),
            'image': request.form.get('image'),
            'description': request.form.get('description'),
            'instructions': request.form.getlist('instruction'),
            'difficulty': request.form.get('difficulty'),
            'ingredients': request.form.getlist('ingredient'),
            'allergens': request.form.getlist('allergen'),
            'categories': request.form.getlist('category'),
            'cooking_time': (request.form.get('cooking_time')),
            'servings': int(request.form.get('servings')),
            'author': session['username']
        })
        flash('Recipe Updated!')
        return redirect(url_for('recipe', recipe_id=recipe_id))

#Removes a recipe from the database
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    flash('Recipe has been deleted!')
    return redirect(url_for('recipes'))

#Logic for allowing the user to exclude certain allergens
@app.route('/exclude_allergen', methods=['GET', 'POST'])
def exclude_allergen():

    recipes = mongo.db.recipes
    if request.method == 'POST':
        recipes = mongo.db.recipes.find(
            {"allergens": {"$nin": request.form.getlist("allergens")}})
        return render_template(
            "results.html",
            recipes=recipes,
            title='Results')
    return render_template('results.html', title='Results')

#Logic for allowing the user to find recipes by difficulty
@app.route('/filter_difficulty', methods=['GET', 'POST'])
def diff_search():
    recipes = mongo.db.recipes
    if request.method == 'POST':
        difficulty = request.form.get("difficulty")
        recipes = mongo.db.recipes.find(
            {"difficulty": {"$eq": request.form.get("difficulty")}})
        return render_template(
            "results.html",
            recipes=recipes,
            title='Results',
            difficulty=difficulty)
    return render_template('results.html', title='Results')

#Logic for finding recipes with a given ingredient
@app.route('/find_ingredient', methods=['GET', 'POST'])
def ing_search():
    recipes = mongo.db.recipes
    if request.method == 'POST':
        ingredient = request.form.get("ingredient")
        recipes = mongo.db.recipes.find({"$text": {"$search": ingredient}})
        return render_template(
            "results.html",
            recipes=recipes,
            title='Results')
    return render_template('results.html', title='Results')

#Displays the results based on the search method used
@app.route('/results')
def results():
    return render_template('results.html', title='Results')


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=False)
