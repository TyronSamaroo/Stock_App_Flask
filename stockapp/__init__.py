from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aa7b78e1935378061106cfbd12e774b3'
app.config['SQLALCHEMY_DATABASE_URI'] = "DATABASE_URL"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

#Avoid Circular Imports
from stockapp import routes 