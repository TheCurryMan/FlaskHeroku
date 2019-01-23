from flask import Flask, render_template, redirect, request, url_for
from forms import SignUpForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

@app.route('/')
def home():
    return 'Hello World'

@app.route('/about')
def about():
    return 'The About Page'

@app.route('/blog')
def blog():
    posts = [{'title': 'Technology in 2019', 'author': 'Avi'},
             {'title': 'Expansion of oil in Russia', 'author': 'Bob'}]
    return render_template('blog.html', author="Bob", sunny=False, posts=posts)

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is blog post number ' + blog_id

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
     x   return render_template('user.html', result=result)
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run()
