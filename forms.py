from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Optional

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    
