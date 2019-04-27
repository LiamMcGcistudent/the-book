from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Optional

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    
class RecipeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    allergens = TextAreaField('Allergens', validators=[Optional()])
    categories = TextAreaField('Categories', validators=[Optional()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    cooking_time = IntegerField('Cooking Time', validators=[DataRequired()])
    servings = IntegerField('Servings', validators=[DataRequired()])
    difficulty = IntegerField('Difficulty', validators=[DataRequired()])
    image = StringField('Copy Image Address Link', validators=[DataRequired()])