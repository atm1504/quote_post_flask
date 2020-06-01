from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = '2097b16c8ef76e7ca87118d18db06281'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

#-------------------
#User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

# Post Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}'')"
# Dummy data
posts = [
    {
        'author': 'Atreyee Mukherjee',
        'title': "B'Day Wish",
        'content': "Happy B'day Amartya Darling! ",
        'date_posted': '4th Jan, 2000'
    },
    {
        'author': 'Amartya Mondal',
        'title': "B'Day Wish",
        'content': "Happy B'day Atreyee Darling! ",
        'date_posted': '15th August, 2000'
    }
]

@app.route('/')
def home():
    return render_template("home.html", posts=posts, title="ATM")

@app.route('/about')
def about():
    return render_template("about.html", posts=posts)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Successfully logged in {form.email.data}!', "success")
        return redirect(url_for("home"))
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)