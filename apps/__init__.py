from flask import Flask

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


#define WSGI
app = Flask(__name__)

#config
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


from apps.auth.view import mod_auth


#regist blueprint
app.register_blueprint(mod_auth)