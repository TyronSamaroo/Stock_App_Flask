from stockapp import app, db, bcrypt 
from flask import render_template, url_for, flash, redirect, request
from stockapp.forms import RegistrationForm, LoginForm, TransactionForm
from stockapp.models import User, Transaction
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, logout_user, login_required


   
   
   

@app.route('/')
def main():
   return render_template('main.html')

@app.route('/home')
@login_required
def home():
   return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html', title='About') 

@app.route('/register', methods=['GET','POST'])
def register():
   if current_user.is_authenticated:
      return redirect(url_for('home'))
   form = RegistrationForm()
   if form.validate_on_submit():
      
      hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=form.username.data, email=form.email.data.lower(), password=hashed_password)
      
      db.session.add(user)
      db.session.commit()
      
      flash(f'Account created for {form.username.data}!','success')
      return redirect(url_for('login'))
   return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
   if current_user.is_authenticated:
      return redirect(url_for('home'))
   form = LoginForm()
   if form.validate_on_submit():
      user = User.query.filter_by(email=form.email.data.lower()).first()
      if user and bcrypt.check_password_hash(user.password, form.password.data):
         login_user(user, remember=form.remember.data)
         next_page = request.args.get('next')
         return redirect(next_page) if next_page else redirect(url_for('home')) 
      else:
         flash('Login Unsuccessful. Check email and password','danger')
   return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('home'))
 
@app.route('/portfolio', methods=['GET','POST'])
@login_required
def portfolio():
   form = TransactionForm()
   
   return render_template('portfolio.html', title='Portfolio', form=form)

@app.route('/transaction')
@login_required
def transaction():
   return render_template('transaction.html', title='Transaction')

@app.route('/account')
@login_required
def account():
   return render_template('account.html', title='Account')

