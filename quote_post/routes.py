from flask import render_template, url_for, flash, redirect
from quote_post import app
from quote_post.forms import RegistrationForm, LoginForm
from quote_post.models import User, Post
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
