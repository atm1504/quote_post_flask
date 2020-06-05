from flask import render_template, url_for, flash, redirect, request
from quote_post import app,db,bcrypt
from quote_post.forms import RegistrationForm, LoginForm
from quote_post.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
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
    },
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
    if current_user.is_authenticated==False:
            return redirect(url_for("login"))
    return render_template("home.html", posts=posts, title="ATM")

@app.route('/about')
def about():
    return render_template("about.html", posts=posts)

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user= User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can now log in!', "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash(f'Failed to login. CHeck email and password', "danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/account")
@login_required
def account():
    image_file = url_for('static', filename="profile_pics/" + current_user.image_file)
    return render_template("account.html", title="Account", image_file=image_file)