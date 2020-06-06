from flask import render_template, request, Blueprint, redirect, url_for
from quote_post.models import Post
from flask_login import current_user
main = Blueprint('main', __name__)

@main.route('/')
@main.route("/home")
def home():
    if current_user.is_authenticated==False:
            return redirect(url_for("users.login"))
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template("home.html", posts=posts, title="ATM")

@main.route('/about')
def about():
    return render_template("about.html")