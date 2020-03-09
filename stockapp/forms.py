from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from stockapp.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), 
                                       Length(min=2, 
                                              max=20)])
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()])
    
    password = PasswordField('Password', 
                             validators=[DataRequired()])
    
    confirm_password = PasswordField('Password', 
                                     validators=[DataRequired(),
                                                 EqualTo('password')]) 
    submit = SubmitField('Sign Up')
    
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is Taken. Please try another')
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is Taken. Please try another')
    

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Email()])
    
    password = PasswordField('Password', 
                             validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
    
class TransactionForm(FlaskForm):
    ticker = StringField('Ticker',
                         validators=[DataRequired(),
                                     Length(min=1, 
                                            max=6)])
    quantity = IntegerField('Quantity',
                            validators=[DataRequired(),
                            NumberRange(min=1)])
    
    submit = SubmitField('Buy')
    
    def validate_ticker(self,ticker):
        pass

