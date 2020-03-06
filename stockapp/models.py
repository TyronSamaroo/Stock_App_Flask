from stockapp import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))


class User(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(20), unique=True, nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)
   password = db.Column(db.String(60), nullable=False)
   transaction = db.relationship('Transaction', backref='buyer', lazy=True)
   
   def __repr__(self):
      return f"User('{self.username}','{self.email}')"

class Transaction(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   
  
   def __repr__(self):
      return f"Transaction('{self.title}','{self.date_posted}')"

