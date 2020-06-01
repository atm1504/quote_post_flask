from flask import Flask, render_template
app = Flask(__name__)

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
def hello():
    return render_template("home.html", posts=posts, title="ATM")

@app.route('/about')
def about():
    return render_template("about.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)