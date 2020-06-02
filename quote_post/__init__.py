from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SECRET_KEY"] = '2097b16c8ef76e7ca87118d18db06281'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from quote_post import routes